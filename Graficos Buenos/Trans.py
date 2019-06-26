import numpy as np
import matplotlib.pyplot as plt
import matplotlib


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

    data["f"] = []
    data["abs"] = []
    data["pha"] = []
    #print(lines)

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

        while lines[i][pnt] != 'd':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '°':
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data

data = read_file_spice("Bode de modelo RC.txt")
data1 = read_file_spice("diodoBode.txt")
modulo = np.asarray(data["abs"])
fase = np.asarray(data["pha"])
frec = np.asarray(data["f"])
modulo1 = np.asarray(data1["abs"])
fase1 = np.asarray(data1["pha"])
frec1 = np.asarray(data1["f"])
#542
#for x in range (542,len(fase)):
#    fase[x] = fase[x]-360
plt.plot(frec,modulo,'b',label ='Modelo Diodo Modulo')
plt.plot(frec,fase,'b--',label = 'Modelo Diodo Fase')
plt.plot(frec1,modulo1,'r',label ='Modelo Capacitor Modulo')
plt.plot(frec1,fase1,'r--',label = 'Modelo Capacitor Fase')
#t = np.arange(30e3, 3e6, 100)
#Hcalc = np.full(29700, 43.82)
#dA 43.82
#plt.plot(t,Hcalc,'r',label ='Modulo Calculado')
legend = plt.legend(loc='lower left', shadow=True, fontsize='x-large')
plt.xscale('log')
plt.ylabel("Fase/Amplitud")
plt.xlabel("Frecuencia")
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
plt.show()