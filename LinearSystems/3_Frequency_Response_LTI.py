from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

s1 = signal.lti([],[1,1,1],[5])
#               Z  Poles    Gain

#freq response
w,H = signal.freqresp(s1)

#complex plot
plt.plot(H.real,H.imag,"b")
plt.plot(H.real,-H.imag,"r")
plt.show()
