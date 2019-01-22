from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

for order in [1,2,3,4,6]:
    b,a=signal.butter(order,100,'low',analog=True)
    w,h = signal.freqs(b,a)
    plt.plot(w,20*np.log10(abs(h)),label = 'order=%d'%order)
    plt.xscale('log')
    plt.title('Butterworth Filter Frequency Response')
    plt.xlabel('Frequency(rad/s)')
    plt.ylabel('Amplitude in DB')
    plt.margins(0,0.1)
    plt.grid()
    plt.axvline(100,color='green')
    plt.legend(loc='best')
plt.show()

               
