import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=100
f2=100
n=200
amp1=10
amp2=10
x=np.arange(n)
a=amp1*np.cos(2*np.pi*f1/fs*x)
plt.subplot(311)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

b=amp2*np.cos(2*np.pi*f2/fs*x)
plt.subplot(312)
plt.plot(x,b)
c=a+b
plt.subplot(313)
plt.plot(x,c)
plt.title('addition of two waves')
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()

