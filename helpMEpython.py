import pylab
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft
import pandas as pd

csv = np.genfromtxt("20130601.csv", dtype="str", delimiter=';')
colomName = csv[0, ::]
colomName[0] += " " + colomName[1]
colomName = np.delete(colomName, (1), axis=0)  # well, fuck i know how this work
# OOP is SUCK! why i cant copy valley oof array not link! its stupid
csv = csv[1:, ::]  # suka blyat now i delete row like a dumb
firstcol = csv[:, 0]  # i need only first colomn in array

for i in range(len(firstcol)):
    firstcol[i] = str.replace(firstcol[i], '.', '-')  # + "T"+ csv[i,1]
    # print csv[i, 1]
    #firstcol[i] =(firstcol[i] + "T" + csv[i, 1])#blin hz no ne rabotaet tak kak nado
   # print firstcol[i]
# firstcol = np.delete(firstcol, (1), axis=0)

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
    print type(t[i, 6])
for i in range(len(t[:, 5])):
    t[i, 5] = float(str.replace(t[i, 5], ',', '.'))
    print type(t[i, 5])
for i in range(len(t[:, 1])):
    t[i, 1] = float(str.replace(t[i, 1], ',', '.'))
    print type(t[i, 1])
for i in range(len(t[:, 2])):
    t[i, 2] = float(str.replace(t[i, 2], ',', '.'))
    print type(t[i, 2])
for i in range(len(t[:, 3])):
    t[i, 3] = float(str.replace(t[i, 3], ',', '.'))
    print type(t[i, 3])
for i in range(len(t[:, 4])):
    t[i, 4] = float(str.replace(t[i, 4], ',', '.'))
    print type(t[i, 4])
for i in range(len(t[:, 7])):
        t[i,7] = float(str.replace(t[i,7], ',', '.'))
        t[i, 7] = float(t[i, 7])
        print type(t[i, 7])
for i in range(len(t[:, 8])):
        t[i,8] = float(str.replace(t[i,8], ',', '.'))
        t[i, 8] = float(t[i, 8])
        print type(t[i, 8])
for i in range(len(t[:, 9])):
        t[i,9] = float(str.replace(t[i,9], ',', '.'))
        t[i, 9] = float(t[i, 9])
        print type(t[i, 9])
for i in range(len(t[:, 10])):
        t[i,10] = float(str.replace(t[i,10], ',', '.'))
        t[i, 10] = float(t[i, 10])
        print type(t[i, 10])
pylab.figure(1)
pylab.plot((t[:, 1]), label="1")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,2]),label="2")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,3]),label="3")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,4]),label="4")#,t[:20,5],t[:20,6],t[:20,7],t[:20,8],t[:20,9],t[:20,10])
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,6]),label="6")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,7]),label="7")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,8]),label="8")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,9]),label="9")
pylab.legend()
pylab.figure(1)
pylab.plot((t[:,10]),label="10")
pylab.legend()

pylab.show()

#print colomName
#print  csv
#print firstcol
