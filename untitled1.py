from __future__ import division
import deltasigma as ds
import numpy as np
import matplotlib.pyplot as plt



order=6
OSR=128

H0 = ds.synthesizeNTF(order, OSR, opt=1)

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