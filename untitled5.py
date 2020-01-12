# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:21:17 2018

@author: Przemek
"""

import numpy as np
from scipy.signal import firwin, freqz
import scipy.io.wavfile as spw
import matplotlib.pyplot as plt
from scipy import signal
#from math import gcd #f1/gcd(f1,f2) f2/gcd(f1,f2)
#import scipy as sp

#TODO
#M/N w jednym

def plot_filter(f, cx=False):
    w, h = freqz(f)
    plt.plot(w / max(w), np.abs(h), color="steelblue")
    if cx:
        plt.plot(-w / max(w), np.abs(h), color="darkred")
    plt.show()
    
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
    
def norm(x):
    x=np.copy(x)
    x=x/max(max(x),-min(x))
    return x

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
    
    
    
smpl,sig=spw.read("0.wav")
filt = firwin(16384, 1/(160 * 1.05), window='flattop')
filt1 = firwin(16384, 1/(147 * 1.05), window='flattop')
duppa=polyphase_int(sig,160,filt)
duppa=polyphase_dec(duppa,147,filt1)
spw.write('1.wav',int(smpl*(160/147)),duppa)