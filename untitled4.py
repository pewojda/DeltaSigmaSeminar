# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:50:51 2018

@author: Przemek
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#TODO
#Zintegruj f0
#Dodaj liczenie z funkcji

def func(t,f0,comp,w0):
    mag=abs(comp)
    phi=np.angle(comp)
    
    sum=f0
    for i in range(1,len(mag)+1):
        sum+=2*mag[i-1]*np.cos(i*w0*t+phi[i-1])
    return sum

    
fm=1
f0=fm/2
k=np.arange(1,15)
fk=fm*(1j/(k*2*np.pi))

comp=fk


    
#f0=5.5000
#phi=[-40.18833,-80.89146,-122.77563,-166.89482,144.88217,89.44875,24.74843,-42.41165,-103.16484,-158.65167]
#mag=[5.3369,4.8707,4.1672,3.3276,2.4799,1.7718,1.3484,1.2304,1.2361,1.1998]

#phi=[i*np.pi/180 for i in phi]

#comp=mag*np.exp(1j*np.real(phi))



print(comp)
print(np.append([f0],abs(comp)))
print(np.append([0],np.angle(comp)*180/np.pi))

plt.plot(np.append([f0],abs(comp)),'-*')
plt.grid()
plt.show()

plt.plot(np.append([0],np.angle(comp)*180/np.pi),'-*')
plt.grid()
plt.show()

plt.plot(np.linspace(0,2,2**16),func(np.linspace(0,2,2**16),f0,comp,2*np.pi*1))
plt.grid()
plt.show()