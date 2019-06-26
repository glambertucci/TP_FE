import numpy as np
import matplotlib.pyplot as plt


def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1

def read_file_spice(filename):
    file = open(filename,'r')
    lines = file.readlines()

    data = dict()

    data["Vf"] = []
    data["Vd"] = []
    data["Id"] = []
    print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != '\t':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '\n':
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["Vf"].append(c1)
        data["Vd"].append(c2)
        data["Id"].append(c3)

    return data




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

#data = read_csv_bode("mlr.csv")
#rectificador
rectV =np.asarray([0,0.256,0.320,0.4,0.469,0.535,0.552,0.563,0.571,0.577,0.589,0.594,0.603,0.608,0.610,0.614,0.618,0.623,0.626,0.635,0.642,0.646,0.653,0.671,0.685])
rectI =np.asarray([0,0.001,0.003,0.017,0.1,0.4,0.6,0.8,1,1.1,1.4,1.5,1.9,2.1,2.1,2.3,2.5,2.8,2.9,3.6,4.1,4.4,5.1,7.5,10.2]) * 1/1000
plt.plot(rectV, rectI,'-bo',label = 'Medido')
#zener
#zenerV = np.asarray([-11.79,-11.71,-11.68,-11.62,-11.56,-11.53,-11.48,-11.3,-10.22,-9.36,0,0.52,0.64,0.67,0.69,0.72,0.74,0.76,0.77])
#zenerI = np.asarray([-7,-4.7,-3.8,-2.6,-1.1,-0.651,-0.216,-0.001,-0.001,0,0.001,0.001,0.056,0.168,0.274,0.792,1.636,4.1,5.1]) *1/1000
#plt.plot(zenerV,zenerI,'-bo',label = 'Medido')

data = read_file_spice("1N4007(ej3)_char.txt")
tensionDiodo = np.asarray(data["Vd"])
corrienteDiodo = np.asarray(data["Id"])
plt.plot(tensionDiodo,corrienteDiodo,'r',label= 'Simulado')
#plt.plot(tensionLedSmooth.ewm(com=20).mean(),corrienteResSmooth.ewm(com=20).mean())
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.ylabel("Corriente (A)")
plt.xlabel("Tension (V)")
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()










