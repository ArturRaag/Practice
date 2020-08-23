# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:17:20 2020

@author: artur
"""
import math
import random
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sympy as sp



x=np.arange(-10,11)
y=2*x-10

plt.plot(x,y)
plt.xlabel("x-telg")
plt.ylabel("y-telg")
plt.annotate("0",(0,0)) # märgib vajaliku kohta (x,y) mingi stringi
plt.plot([0],[0],marker="o", markersize=3, color="red") # paneb punkti märgitud koordinaatidele
plt.grid()
plt.show()



# def function(x):
#     return np.log(x)/x

# count = 0
# in_area = 0

# while count<1000000:
#     x_coord=random.uniform(1,10)
#     y_coord=random.uniform()

