import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal

output_signal= signal.convolve(sigs.InputSignal_1kHz_15kHz,sigs.Impulse_response,mode='same')
style.use('ggplot')
f,plt_arr = plt.subplots(3,sharex=True)
f.suptitle("Convolution")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color="cyan")
plt_arr[0].set_title("Input Signal")
plt_arr[1].plot(sigs.Impulse_response, color="red")
plt_arr[1].set_title("Impulse Response")
plt_arr[2].plot(output_signal, color="green")
plt_arr[2].set_title("output_signal")
plt.show()
