import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

#Generate a Signal
#Signal sampling rate of 2000Hz,Nyquist = 1000hz
t= np.linspace(0,1.0,2001)

sig_5Hz = np.sin(2*np.pi*5*t)
sig_50Hz = np.sin(2*np.pi*50*t)
sig_250Hz = np.sin(2*np.pi*250*t)
sig_5Hz_50Hz_250Hz = sig_5Hz + sig_50Hz + sig_250Hz

#plt.plot(sig_5Hz_50Hz_250Hz)
#plt.show()

numtaps = 101
lpf_cutoff = 7
hpf_cutoff = 100
bp_cutoff1 = 40
bp_cutoff2 = 100

#Lowpass
#we calculate the low pass coefficients to get the impulse response
lowpass_coef = signal.firwin(numtaps,lpf_cutoff,nyq = 1000)
#Now we have the impulse response, we convolve the impulse response with input
lpf_output = signal.convolve(sig_5Hz_50Hz_250Hz,lowpass_coef,mode='same')


#Highpass
#we calculate the High pass coefficients to get the impulse response
highpass_coef =signal.firwin(numtaps,hpf_cutoff,pass_zero = False,nyq = 1000)
#pass_zero = False differentiates between a high pass and a low pass filter
hpf_output = signal.convolve(sig_5Hz_50Hz_250Hz,highpass_coef,mode='same')

#Bandpass
bandpass_coef = signal.firwin(numtaps,[bp_cutoff1,bp_cutoff2],pass_zero=False,nyq=1000)
bandpass_output = signal.convolve(sig_5Hz_50Hz_250Hz,bandpass_coef,mode='same') 

style.use('dark_background')
f,plt_arr = plt.subplots(7, sharex=True)
f.suptitle("FIR FILTER DESIGN")

plt_arr[0].plot(sig_5Hz, color='Yellow')
plt_arr[0].set_title("5hz Signal",color='Yellow')
    
plt_arr[1].plot(sig_50Hz, color='cyan')
plt_arr[1].set_title("50Hz Signal",color='cyan')

plt_arr[2].plot(sig_250Hz, color='Red')
plt_arr[2].set_title("250Hz Signal",color='Red')

plt_arr[3].plot(sig_5Hz_50Hz_250Hz, color='Blue')
plt_arr[3].set_title("Combined Signal",color='Blue')

plt_arr[4].plot(lpf_output, color='pink')
plt_arr[4].set_title("LPF Output",color='pink')

plt_arr[5].plot(hpf_output, color='teal')
plt_arr[5].set_title("HPF Output",color='teal')

plt_arr[6].plot(bandpass_output, color='Green')
plt_arr[6].set_title("Bandpass_output",color='Green')


plt.show()








