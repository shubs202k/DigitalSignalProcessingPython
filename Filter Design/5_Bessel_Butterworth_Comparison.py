import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal

b,a = signal.butter(4,100,'low',analog=True)
w,h = signal.freqs(b,a)

plt.plot(w,20*np.log10(abs(h)),color = 'silver',ls='dashed')

b,a = signal.bessel(4,100,'low',analog=True)
w,h = signal.freqs(b,a)

plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Bessel Filter Frequency Response(with Butterworth)')
plt.xlabel('Frequency in Rad/s')
plt.ylabel('Amplitude in dB')
plt.margins(0,0.1)
plt.grid(which='both',axis='both')
plt.axvline(100,color = 'Black')
plt.show()
