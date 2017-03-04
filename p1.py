import pandas as pd
import pprint
import scipy

import pylab
import matplotlib.pyplot as plt


df=pd.read_csv('20130602.csv')

#pprint.pprint(df.head(5))

#pprint.pprint(df['direction1'].head(5))


def plotSpectrum(y, Fs):
    n = len(y)  # length of the signal
    k = scipy.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    print(range((int)(n / 2)))
    Y = scipy.fft(y) / n  # fft computing and normalization

    plt.plot(frq, abs(Y))
    pylab.xlabel('Freq (Hz)')
    pylab.ylabel('|Y(freq)|')


Fs = 1024.0

y=pd.DataFrame.as_matrix(df['speed2']).tolist()


print(y)
t = scipy.arange(0, len(y), 1)  # time vector

plt.subplot(2, 1, 1)
plt.plot(t, y)
pylab.xlabel('Time')
pylab.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plotSpectrum(y, Fs)
pylab.show()