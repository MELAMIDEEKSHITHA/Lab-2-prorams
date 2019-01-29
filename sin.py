import matplotlib.pyplot as plt
import numpy as np
fs=1000
f1=200
f2=100
n=100
x=np.arange(n)
a=np.cos(2*np.pi*f1/fs*x)
plt.subplot(212)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

b=np.cos(2*np.pi*f2/fs*x)
plt.subplot(211)
plt.plot(x,b)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()

