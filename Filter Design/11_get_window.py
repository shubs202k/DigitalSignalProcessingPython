from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs
import numpy as np

triang_window = signal.get_window('triang',30)
kaiser_window = signal.get_window(('kaiser',4.0),30)
kaiser_widnow2 = signal.get_window(4.0,30)
hamm_window = signal.get_window('hamming',30)
black_window = signal.get_window('blackman',30)

style.use('dark_background')
f,plt_arr = plt.subplots(4, sharex=True)
f.suptitle("Windows")

plt_arr[0].plot(triang_window, color='Red')
plt_arr[0].set_title("Triangular Window",color='Red')
    
plt_arr[1].plot(kaiser_window, color='Red')
plt_arr[1].set_title("Kaiser_Window",color='Red')

plt_arr[2].plot(hamm_window, color='Red')
plt_arr[2].set_title("Hamming window",color='Red')

plt_arr[3].plot(black_window, color='Red')
plt_arr[3].set_title("Blackman Window",color='Red')
plt.show()
