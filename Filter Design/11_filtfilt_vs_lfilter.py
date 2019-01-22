from numpy import sin,cos,pi,linspace
from numpy.random import randn
from scipy.signal import lfilter,lfilter_zi,filtfilt,butter
from matplotlib.pyplot import plot,legend,show,grid,figure

#Generate a noisy signal to be filtered

t = linspace(-1,1,201)
#sampling rate 201

x1 = sin(2*pi*0.75*t*(1-t))
x2 = 2.1+0.1*sin(2*pi*1.25*t+1)
x3 = 0.18*cos(2*pi*3.85*t)

x = x1 + x2 + x3
#noisy signal generatation
xn = x + randn(len(t))*0.08

b,a = butter(3,0.05)
zi = lfilter_zi(b,a)

#lfilter Once
z,_ = lfilter(b,a,xn,zi=zi*xn[0])
#Lfilter twice
z2,_ = lfilter(b,a,z,zi=zi*z[0])

y = filtfilt(b,a,xn)
#we observe there is no change in phase when we use filtfilt to smoothen a signal

figure(figsize=(10,5))
plot(t,xn,'b',linewidth=1.75)
plot(t,z,'r--',linewidth=1.75)
plot(t,z2,'r',linewidth=1.75)
plot(t,y,'g',linewidth=2.2)

legend(('noisy signal','lfilter_once','lfilter_twice','filtfilt'),loc='best')
grid()
show()
