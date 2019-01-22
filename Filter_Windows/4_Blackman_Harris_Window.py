from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs
import numpy as np
from scipy.fftpack import fft,fftshift

window = signal.blackmanharris(51)
plt.plot(window)
plt.title("Blackman Harris Window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

#frequency response

plt.figure()

A =fft(window,2048)/(len(window)/2.0)
freq = np.linspace(-0.5,0.5,len(A))
response = 20*np.log10(np.abs(fftshift(A/abs(A).max())))
plt.plot(freq,response)
plt.axis([-0.5,0.5,-120,0])
plt.title("Frequency Response of Blackman Harris Window")
plt.ylabel("Normalized Magnitude(dB)")
plt.xlabel("Normalized Frequency in cycles/sample")
plt.show()
