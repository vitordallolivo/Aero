# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:08:12 2022

@author: Vitor
"""

import matplotlib.pyplot as plt
import numpy as np

npp = np.arange(100)+1
v= np.arange(6)+1
nt=np.arange(16)+1

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]



for i in range(0,100):
    for j in range(0,6):
        temp=(0.6*npp[i])/v[j]
        print(v[j])
        if(j==0):
            p1.append(temp)
        if(j==1):
            p2.append(temp)
        if(j==2):
            p3.append(temp)
        if(j==3):
            p4.append(temp)
        if(j==4):
            p5.append(temp)
        if(j==5):
            p6.append(temp)


plt.plot(npp,p1,label='Volume=1')
plt.plot(npp,p2,label='Volume=2')
plt.plot(npp,p3,label='Volume=3')
plt.plot(npp,p4,label='Volume=4')
plt.plot(npp,p5,label='Volume=5')
plt.plot(npp,p6,label='Volume=6')
plt.legend()
plt.show()



