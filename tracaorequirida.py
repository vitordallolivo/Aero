# -*- coding: utf-8 -*-
"""
e0 precisa ser revisado

13x6.5 SO e 9090 RPM

"""

import matplotlib.pyplot as plt  # plotar os graficos
import numpy as np


teta=[]
rc=[]
tr = []
v = []
cd = []
td =[]
pd= []
pr =[]
p = 1.225  # densidade do ar em kg/m³
s = 0.454  # área
cd0 = 0.021857  # coeficiente de arrasto inicial
pi = 3.14159265359  # pi
arw = 11.34  # razão de aspecto
w = 83.4  # Peso
e0 = 0.6  # pegar com a aerodinamica

p00 = -0.04286
p10 = -0.004896
p01 = 7.054e-05
p20 = 0.001271
p11 = -1.214e-05
p02 = 1.372e-08
p30 = 0.0001768
p21 = -2.129e-06
p12 = 5.302e-09
p03 = 2.404e-12
p40 = -7.498e-08
p31 = -2.942e-08
p22 = 3.041e-10
p13 = -7.452e-13
p04 = 8.064e-18
p50 = -2.449e-08
p41 = 1.99e-10
p32 = 8.88e-13
p23 = -1.266e-14
p14 = 3.072e-17
p05 = -4.023e-21

def kgfton(kgf):# transforma kgf para N
    N = kgf*9.80665
    return N

def polinomio(x):  # usa o polinomio para conseguir a tração estimada
    y=9090
    
    f = p00 + p10*x + p01*y + p20*x*x + p11*x*y + p02*y*y + p30*x*x*x + p21*x*x*y + p12*x*y*y + p03*y*y*y + p40*x*x*x*x + p31*x*x*x * \
        y + p22*x*x*y*y + p13*x*y*y*y + p04*y*y*y*y + p50*x*x*x*x*x + p41*x*x*x*x * \
        y + p32*x*x*x*y*y + p23*x*x*y*y*y + p14*x*y*y*y*y + p05*y*y*y*y*y

    f = kgfton(f)  # resultado do pol é em kgf
    
    return(f)


def calcd(vel):
    cl = 2*w/(p*vel*vel*s)
    temp = cd0 + (cl*cl)/(pi*e0*arw)
    return temp


for i in range(1, 350):
    v.append(i/10)
    td.append(polinomio(v[i-1]))    
    cd.append(calcd(v[i-1]))
    pd.append(td[i-1]*v[i-1])

for j in range(0, 349):
    temp = 0.5*p*v[j]*v[j]*s*cd[j]
    tr.append(temp)
    pr.append(temp*v[j])


#ax = plt.subplot(111)
#plt.title('Curvas de Tração')
#plt.ylim(0, 60)
#plt.plot(v,td,label='Tração disponivel')
#plt.plot(v, tr, label='Tração requerida')
#ax.legend(loc='upper center', bbox_to_anchor=(
#    0.5, -0.05), fancybox=True, shadow=True, ncol=5)
#plt.show()

ax = plt.subplot(111)
plt.title('Curvas de Potência')
plt.plot(v,pd,label='Potência disponivel')
plt.ylim(0,600)
plt.plot(v,pr, label='Potência requerida')
#plt.plot(*intersection.xy,'ro')
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.05), fancybox=True, shadow=True, ncol=5)
plt.show()

#ax = plt.subplot(111)
#plt.title('Polar de velocidade subida')
#plt.plot(v,rc,label='Razão de subida por m/s')
#plt.plot(v,teta,"-.")
#plt.ylim(0,4)
#ax.legend(loc='upper center', bbox_to_anchor=(
#    0.5, -0.05), fancybox=True, shadow=True, ncol=5)
#plt.show()

