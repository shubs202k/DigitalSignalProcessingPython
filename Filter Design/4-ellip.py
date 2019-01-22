import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style

b,a = signal.ellip(6,5,50,100,'high',analog=True)
w,h = signal.freqs(b,a)

plt.xscale('log')
plt.plot(w,20*np.log10(abs(h)))
plt.title('Elliptic Filter Frequency Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Amplitude in dB')
plt.margins(0,0.1)
plt.grid(which='both',axis='both')
plt.axvline(100,color = 'red')
plt.axhline(-50,color ='black')
plt.axhline(-5,color ='green')

plt.show()
