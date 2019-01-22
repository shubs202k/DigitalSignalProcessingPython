from scipy.signal import freqz,remez
import numpy as np
from matplotlib import pyplot as plt

#filter with passband 0.2-0.4Hz,stopband 0-0.1Hz and 0.45-0-0.5Hz
#minimizes the maximum error between desired gain and the realized gain in specified band

bpass = remez(72,[0,0.1,0.2,0.4,0.45,0.5],[0,1,0])
freq,response = freqz(bpass)
amp = abs(response)
plt.semilogy(freq/(2*np.pi),amp,'g-')
plt.grid()
plt.show()
