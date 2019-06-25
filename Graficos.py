import numpy as np
import matplotlib.pyplot as plt

#rectificador
#rectV =np.asarray([0,0.256,0.320,0.4,0.469,0.428,0.535,0.552,0.563,0.571,0.577,0.589,0.594,0.603,0.608,0.610,0.614,0.618,0.623,0.626,0.635,0.642,0.646,0.653,0.671,0.685])
#rectI =np.asarray([0,0.001,0.003,0.017,0.1,0.2,0.4,0.6,0.8,1,1.1,1.4,1.5,1.9,2.1,2.1,2.3,2.5,2.8,2.9,3.6,4.1,4.4,5.1,7.5,10.2])
#plt.plot(rectV, rectI,'-bo')

#led
ledV = np.asarray([0,0.56 ,0.99   ,1.49 , 1.73, 1.83, 1.87,1.9,1.91,2   ,2.1,2.12,2.13,2.2 ,2.215, 2.23,2.23,2.23,2.23,2.24,2.26])
ledI = np.asarray([0,0.001,  0.02 ,0.003,0.043,0.05,0.072,0.2,0.3  , 0.72,1.2,1.32,1.35,1.4 ,1.42,1.560, 1.8 ,3.3 ,4.2 ,6,7.2])
plt.plot(ledV, ledI,'-bo')

#zener directa
#zenerdV = np.asarray([0.52,0.64,0.67,0.69,0.72,0.74,0.76,0.77])
#zenerdI = np.asarray([0.001,0.056,0.168,0.274,0.792,1.636,4.1,5.1])
#plt.plot(zenerdV,zenerdI,'-bo')

#Zener Inversa
#zeneriV = np.asarray([-0, -9.36, -10.22, -11.3,-11.48, -11.53, -11.56, -11.62, -11.68, -11.71, -11.79])
#zeneriI = np.asarray([-0, - 0.001, -0.001, -0.001, -0.216, -0.651, -1.1, -2.6, -3.8, -4.7, -7])
#plt.plot(zeneriV,zeneriI,'-bo')

#Zener Entera
#zenerV = np.asarray([-11.79,-11.71,-11.68,-11.62,-11.56,-11.53,-11.48,-11.3,-10.22,-9.36,0,0.52,0.64,0.67,0.69,0.72,0.74,0.76,0.77])
#zenerI = np.asarray([-7,-4.7,-3.8,-2.6,-1.1,-0.651,-0.216,-0.001,-0.001,0,0.001,0.001,0.056,0.168,0.274,0.792,1.636,4.1,5.1])
#plt.plot(zenerV,zenerI,'-bo')

plt.ylabel("Corriente en el diodo [mA]")
plt.xlabel("Tension en el diodo [V]")
# pongo una grilla
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
# muestro el grafico que prepare
plt.show()