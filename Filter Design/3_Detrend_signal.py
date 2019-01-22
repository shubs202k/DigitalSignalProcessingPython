import numpy as np
import scipy.signal as signal
from matplotlib import pyplot as plt

t = np.linspace(-10,10,20)
y = 1 + t + 0.01*t**2

#signal has upward moving trend
# we want to remove this trend

#constant detrending

yconst = signal.detrend(y,type='constant')

#linear detrending
ylin = signal.detrend(y,type='linear')

plt.plot(t,y,'-rx')
plt.plot(t,yconst,'-bo')
plt.plot(t,ylin,'-k+')
plt.grid()
plt.legend(['signal','constant detrend','Linear detrend'])
plt.show()
