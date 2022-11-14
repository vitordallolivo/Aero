# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:49:43 2022

@author: Vitor
"""
import matplotlib.pyplot as plt
import numpy as np

npp = np.arange(50)+1
v= np.arange(6)+1
nt=np.arange(16)+1

pn1=[]
pn2=[]
pn3=[]
pn4=[]
pn5=[]
pn6=[]
pn7=[]
pn8=[]
pn9=[]
pn10=[]
pn11=[]
pn12=[]
pn13=[]
pn14=[]
pn15=[]
pn16=[]


for i in range(0,50):
    for t in range(0,16):
        temp=(0.6*(npp[i]+nt[t]*5))/6
        if(t==0):
            pn1.append(temp)
        if(t==1):
            pn2.append(temp)
        if(t==2):
            pn3.append(temp)
        if(t==3):
            pn4.append(temp)
        if(t==4):
            pn5.append(temp)
        if(t==5):
            pn6.append(temp)
        if(t==6):
            pn7.append(temp)
        if(t==7):
            pn8.append(temp)
        if(t==8):
            pn9.append(temp)
        if(t==9):
            pn10.append(temp)
        if(t==10):
             pn11.append(temp)
        if(t==11):
            pn12.append(temp)
        if(t==12):
            pn13.append(temp)
        if(t==13):
            pn14.append(temp)
        if(t==14):
            pn15.append(temp)
        if(t==15):
            pn16.append(temp)
           


plt.plot(npp,pn1,label='NT=1, V=6')
plt.plot(npp,pn2,label='NT=2, V=6')
plt.plot(npp,pn3,label='NT=3, V=6')
plt.plot(npp,pn4,label='NT=4, V=6')
plt.plot(npp,pn5,label='NT=5, V=6')
plt.plot(npp,pn6,label='NT=6, V=6')
plt.plot(npp,pn7,label='NT=7, V=6')
plt.plot(npp,pn8,label='NT=8, V=6')
plt.plot(npp,pn9,label='NT=9, V=6')
plt.plot(npp,pn10,label='NT=10, V=6')
plt.plot(npp,pn11,label='NT=11, V=6')
plt.plot(npp,pn12,label='NT=12, V=6')
plt.plot(npp,pn13,label='NT=13, V=6')
plt.plot(npp,pn14,label='NT=14, V=6')
plt.plot(npp,pn15,label='NT=15, V=6')
plt.plot(npp,pn16,label='NT=16, V=6')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
