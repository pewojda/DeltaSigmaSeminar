import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.io.wavfile as spw
import deltasigma as ds

def plot_spec(x,N=None,SF=None):
    x=np.copy(x)
    x=x/len(x)
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

sig=sp.randn(50)
sig=norm(sig)

sig=np.sin(2*np.pi*1*np.linspace(0,1,44100))
sigq=quant(sig,3)

spw.write('1.wav',44100,sig)
spw.write('2.wav',44100,sigq)

plot_spec(sig)
plot_spec(sigq)
plt.xscale('log')
plt.ylim([-120,0])
plt.grid()
plt.show()
    
plt.plot(sig,'-*')
plt.plot(sigq,'*r')
plt.grid()
plt.show()