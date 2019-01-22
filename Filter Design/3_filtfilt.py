from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import mysignals as sigs
from scipy import signal

t = np.linspace(0,1.0,2001)

sig_5hz = np.sin(2*np.pi*5*t)
sig_250hz = np.sin(2*np.pi*250*t)

sig_5hz_250hz= sig_5hz + sig_250hz

#create coefficients of filter first
#8*0.125 is 1
#filter has cutoff freq 125Hz

b,a = signal.butter(8,0.125)
filtered_signal = signal.filtfilt(b,a,sig_5hz_250hz,padlen=150)

style.use('dark_background')

f,plt_arr = plt.subplots(4,sharex=True)
f.suptitle('Filt Filt')

plt_arr[0].plot(sig_5hz,color ='red')
plt_arr[0].set_title("Sig_5hz",color='red')

plt_arr[1].plot(sig_250hz,color ='red')
plt_arr[1].set_title("Sig_250hz",color='red')

plt_arr[2].plot(sig_5hz_250hz,color ='yellow')
plt_arr[2].set_title("Combined signal",color='yellow')

plt_arr[3].plot(filtered_signal,color ='cyan')
plt_arr[3].set_title("Filtered signal",color='cyan')

plt.show()
