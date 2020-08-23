# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:16:13 2020

@author: artur
"""


# Real time täringu veeretamise jaotusgraafik.

import random
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


katsed=1
valikud=["1","2","3","4","5","6"]
tulemused=[]

plt.style.use("fivethirtyeight")

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)


x_values=[]
y_values=[]

def animate(i):
    
    for i in range(katsed):
        a=random.choice(valikud)
        tulemused.append(a)
        loend=Counter(tulemused)
        saame=loend.most_common(10)
    
    x_values=[]
    y_values=[]
    
    for values in saame:
        x_values.append(values[0])
        y_values.append(values[1])
    
    locs, labels = xticks()
    xticks([0, 1, 2], ['January', 'February', 'March'], rotation=20)
    
    ax1.clear()
    ax1.bar(x_values,y_values)
 
ani =FuncAnimation(plt.gcf(), animate, interval= 1000)
    
plt.tight_layout()
plt.show()