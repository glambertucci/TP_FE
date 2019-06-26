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
df = pd.read_csv('mlr.csv')

tensionFuente = np.asarray(df['CH1'])
tiempo = np.arange(0, len(tensionFuente), 1)
tensionLed = np.asarray(df['CH2'])
corrienteRes = (tensionFuente - tensionLed) * 1/470
tensionLedSmooth = pd.DataFrame(tensionLed)
corrienteResSmooth = pd.DataFrame(corrienteRes)

{#plt.plot(tensionLedSmooth.ewm(com=20).mean(),corrienteResSmooth.ewm(com=20).mean())
#plt.plot(tensionLedSmooth,corrienteResSmooth)
#plt.ylabel("Corriente (A)")
#plt.xlabel("Tension (V)")
#plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
#plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
#plt.show()
}
data = read_file_spice("try.txt")
tensionDiodo = np.asarray(data["Vd"])
corrienteDiodo = np.asarray(data["Id"])
plt.plot(tensionDiodo,corrienteDiodo)
plt.plot(tensionLedSmooth.ewm(com=20).mean(),corrienteResSmooth.ewm(com=20).mean())
plt.ylabel("Corriente (A)")
plt.xlabel("Tension (V)")
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()










