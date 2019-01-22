from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import mysignals as sigs
from scipy import signal

#Easier to detect peaks using a median filter

median_filter_output = signal.medfilt(sigs.InputSignal_1kHz_15kHz,11)
#we use a 11 point median filter
style.use('dark_background')

f,plt_arr = plt.subplots(2,sharex=True)
f.suptitle('Median Filter')

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz,color ='red')
plt_arr[0].set_title("Input_Signal",color='red')

plt_arr[1].plot(median_filter_output,color ='magenta')
plt_arr[1].set_title("Output",color='magenta')

plt.show()
