from __future__ import division
import deltasigma as ds
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as spw
from scipy import signal
from scipy.signal import firwin, freqz

import warnings
warnings.filterwarnings("ignore")

#TODO
#CIFB dla dow. rzedu

def plot_spec(x,N=None,SF=None, window=True):
    x=np.copy(x)
    x=x/len(x)
    if window==True:
        win=np.hamming(len(x))
        x*=win
    if N==None:
        N=len(x)
    if SF==None:
        SF=N
    f=np.linspace(0,int(SF/2+1),int(N/2+1))
    w=np.fft.fft(x,N)
    w=np.abs(w)
    w=w[0:int(N/2+1)]
    wlog=np.ones(len(w))*-300
    wlog[w!=0]=20*np.log10(w[w!=0])
    plt.plot(f,wlog)
    
def quant(x,B):
    x=np.copy(x)
    Q=1/float(2**(B-1))
    x[x<-1]=-1
    x[x>1-Q]=1-Q
    y=Q*np.floor(x/Q+0.5)
    #y=Q*np.floor(x/Q)+0.5
    if B==1:
        #y=np.floor(x/Q)+1
        #y=Q*np.floor(x/Q)+0.5
        y=np.sign(x)*2+1
    return y

def limit(x):
    x=np.copy(x)
    x[x<-1]=-1
    x[x>1]=1
    return x

def norm(x):
    x=np.copy(x)
    x=x/max(max(x),-min(x))
    return x
   
def CIFB(x,B,a,g,b,c): #6th order
    x=np.copy(x)
    a=np.copy(a)
    g=np.copy(g)
    b=np.copy(b)
    c=np.copy(c)
    
    out=np.zeros(len(x))
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    for i in range(len(x)):
        out[i]=quant((x6*c[5])+(x[i]*b[6]),B)
        x6=x6+(x[i]*b[5])+(out[i]*-a[5])+(x5*c[4])
        x5=x5+(x[i]*b[4])+(out[i]*-a[4])+(x4*c[3])+(x6*g[2])
        x4=x4+(x[i]*b[3])+(out[i]*-a[3])+(x3*c[2])
        x3=x3+(x[i]*b[2])+(out[i]*-a[2])+(x2*c[1])+(x4*g[1])
        x2=x2+(x[i]*b[1])+(out[i]*-a[1])+(x1*c[0])
        x1=x1+(x[i]*b[0])+(out[i]*-a[0])+(x2*g[0])
    return out

def polyphase_dec(x, m, f):
    x=np.copy(x)
    f=np.copy(f)
    
    x=np.append(x,[0]*(m-len(x)%m))
    f=np.append(f,[0]*(m-len(f)%m))
    
    p=np.zeros((m,int(len(x)/m)),dtype=x.dtype)
    
    for i in range(m):
        p[i,:]=signal.fftconvolve(x[i::m],f[i::m],'same')
    
    return sum(p)

def polyphase_int(x, m, f):
    x=np.copy(x)
    f=np.copy(f)
    
    x=np.append(x,[0]*(m-len(x)%m))
    f=np.append(f,[0]*(m-len(f)%m))
    
    p=np.zeros((m,len(x)),dtype=x.dtype)
    
    for i in range(m):
        p[i,:]=signal.fftconvolve(x,f[i::m],'same')
        
    out=np.zeros(p.shape[0]*p.shape[1])
    
    for i in range(m):
        out[i::m]=p[i,:]
    
    out*=m
    
    return out

def simpl_div(x,n):
    y=np.zeros(int(len(x)/n))
    for i in range(len(y)):
        for ii in range(0,n):
            y[i]+=x[ii+i*n]
    y[i]/=n
    return y
    

order=6
OSR=64
sampl=44100
B=1

H0 = ds.synthesizeNTF(order, OSR, opt=0)
#H0 = ds.synthesizeChebyshevNTF(order, OSR, opt=0)

f=np.linspace(0, 0.5, 2**16)
z=np.exp(2j*np.pi*f)
magH0=ds.dbv(ds.evalTF(H0, z))

plt.plot(f, magH0)
plt.plot([1/OSR*0.5,1/OSR*0.5],[-120,0],'g')
plt.plot([0,1/OSR*0.5],[-120,-120],'g')
plt.xscale('log')
plt.grid()
plt.show()

print(ds.pretty_lti(H0))
print("\n")

a, g, b, c = ds.realizeNTF(H0,form='CIFB')

print('a: ',a)
print('g: ',g)
print('b: ',b)
print('c: ',c)

wavin=np.sin(2*np.pi*2000*np.linspace(0,1,sampl))
#sampl,wavin=spw.read("0.wav")

sig=wavin*0.5

#del wavin

filt = firwin(2**15, 1/(OSR * 1.00), window='flattop')
sig=polyphase_int(sig,OSR,filt)

#spw.write('1.wav',sampl*OSR,sig)
sigq=quant(sig,B)
#spw.write('2.wav',sampl*OSR,sigq)
sigds=CIFB(sig,B,a,g,b,c)
#del sig, sigq
#spw.write('3.wav',sampl*OSR,sigds)
sigdsd=signal.fftconvolve(sigds,filt,'same')
#spw.write('4.wav',sampl*OSR,sigdsd)
#del sigds
sigdsd=simpl_div(sigdsd,OSR)
sigdsd/=OSR
#spw.write('5.wav',sampl,sigdsd)
#del sigdsd

plot_spec(sig)
plot_spec(sigq)
plot_spec(sigds)
plt.xscale('log')
plt.ylim([-120,0])
plt.grid()
plt.show()

plot_spec(sig)
plot_spec(sigq)
plot_spec(sigds)
plt.ylim([-120,0])
plt.grid()
plt.show()
    
plt.plot(sig,'-*')
plt.plot(sigq,'*r')
plt.plot(sigds,'*g')
plt.grid()
plt.show()