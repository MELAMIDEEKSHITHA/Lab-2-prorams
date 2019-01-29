import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=100
n=200
amp1=10
amp2=20
amp3=30
amp4=40
p1=90
p2=0
p3=30
p4=60
x=np.arange(n)
a=amp1*np.cos(2*np.pi*f1/fs*x+p1)
plt.subplot(511)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

b=amp2*np.cos(2*np.pi*f1/fs*x+p2)
plt.subplot(512)
plt.plot(x,b)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

r=amp3*np.cos(2*np.pi*f1/fs*x+p3)
plt.subplot(513)
plt.plot(x,r)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

l=amp4*np.cos(2*np.pi*f1/fs*x+p4)
plt.subplot(514)
plt.plot(x,l)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
c=a+b+r+l
plt.subplot(515)
plt.plot(x,c)
plt.title('addition of four waves')

plt.show()

