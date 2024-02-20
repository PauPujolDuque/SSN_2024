import numpy as np
import matplotlib.pyplot as plt

s = 2000
ts = 1.0/s
t = np.arange(0,1,ts)

x = np.cos(2 * np.pi * 15 * t) - np.sin(2 * np.pi * 40 * t)

X = np.fft.fft(x)
N = len(X)
n = np.arange(N)
T = N/s
freq = n/T 

plt.subplot(211)
plt.plot(t, np.fft.ifft(X), 'r')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitud')

plt.subplot(212)

plt.plot(freq, np.abs(X), 'b')
plt.xlabel('Freqüència (Hz)')
plt.ylabel('Amplitud FT')
plt.xlim(0, 100)


plt.tight_layout()
plt.show()