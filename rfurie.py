from __future__ import division
import pylab
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft
import pandas as pd

p = pd.read_csv("20130601.csv", dtype="str", delimiter=';')
del p['date']
#print p
t = p.values
print t
j=1
# while j<=10:
#         for i in range( len(t[:,j])):
#             t[i,j] = float (str.replace(t[i,j],',','.'))
#             print type(t[i,j])
#             j+=1
#             print j


for i in range(len(t[:, 6])):
    t[i, 6] = float(str.replace(t[i, 6], ',', '.'))

for i in range(len(t[:, 5])):
    t[i, 5] = float(str.replace(t[i, 5], ',', '.'))

for i in range(len(t[:, 1])):
    t[i, 1] = float(str.replace(t[i, 1], ',', '.'))

for i in range(len(t[:, 2])):
    t[i, 2] = float(str.replace(t[i, 2], ',', '.'))

for i in range(len(t[:, 3])):
    t[i, 3] = float(str.replace(t[i, 3], ',', '.'))

for i in range(len(t[:, 4])):
    t[i, 4] = float(str.replace(t[i, 4], ',', '.'))

for i in range(len(t[:, 7])):
        t[i,7] = float(str.replace(t[i,7], ',', '.'))
        t[i, 7] = float(t[i, 7])

for i in range(len(t[:, 8])):
        t[i,8] = float(str.replace(t[i,8], ',', '.'))
        t[i, 8] = float(t[i, 8])

for i in range(len(t[:, 9])):
        t[i,9] = float(str.replace(t[i,9], ',', '.'))
        t[i, 9] = float(t[i, 9])

for i in range(len(t[:, 10])):
        t[i,10] = float(str.replace(t[i,10], ',', '.'))
        t[i, 10] = float(t[i, 10])
time_step = 1/30
while j!=11:
    ps = 20 * np.log10(np.abs(np.fft.rfft(t[:, j])) ** 2)
    freqs = np.fft.rfftfreq((t[:, j]).size, time_step)
    idx = np.argsort(freqs)
    pylab.figure(j)
    pylab.plot(freqs[idx], ps[idx], label="1")
    pylab.legend()
    j = j + 1
pylab.show()