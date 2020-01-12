# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:07:42 2018

@author: Przemek
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as spw

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
    
    
    
    

#x=np.arange(10.0)
smpl=44100
x=np.sin(2*np.pi*1000*np.linspace(0,1,smpl))
#smpl,x=spw.read("0.wav")
#print(x)
SR=2





y=np.zeros(len(x)*SR)
for i in range(len(x)):
    y[i*SR]=x[i]
#print(y)

y1=np.zeros(len(x)*SR)
for i in range(len(x)):
    for ii in range(0,SR):
        y1[ii+i*SR]=x[i]
#print(y1)

ym=y

z=np.zeros(int(len(ym)/SR))
for i in range(len(z)):
    z[i]=ym[i*SR]
#print(z)

q=np.zeros(int(len(ym)/SR))
for i in range(len(q)):
    for ii in range(0,SR):
        q[i]+=ym[ii+i*SR]
    #q[i]/=SR
#print(q)
    
w=np.zeros(int(len(x)/SR))
for i in range(len(w)):
    w[i]=x[i*SR]
#print(z)

r=np.zeros(int(len(x)/SR))
for i in range(len(r)):
    for ii in range(0,SR):
        r[i]+=x[ii+i*SR]
    r[i]/=SR
#print(q)

plot_spec(x,SF=smpl)
plot_spec(z,SF=smpl)
plot_spec(q,SF=smpl)
plt.grid()
plt.show()

plot_spec(y,SF=smpl*SR)
plot_spec(y1,SF=smpl*SR)
plt.grid()
plt.show()
    
plt.plot(x,'*b')
plt.plot(z,'*r')
plt.plot(q,'*g')
plt.grid()
plt.show()

plt.plot(y,'*r')
plt.plot(y1,'.g')
plt.grid()
plt.show()

spw.write('1.wav',smpl,x)
spw.write('2.wav',smpl,z)
spw.write('3.wav',smpl,q)
spw.write('4.wav',smpl*SR,y)
spw.write('5.wav',smpl*SR,y1)
spw.write('6.wav',int(smpl/SR),w)
spw.write('7.wav',int(smpl/SR),r)