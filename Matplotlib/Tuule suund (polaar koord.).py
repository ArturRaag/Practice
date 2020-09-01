# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:28:56 2020

@author: artur
"""

import numpy as np
import matplotlib.pyplot as plt

tuule_suund_kraadides =[52,59,50,45,43,46,48,45,53,52,51,48,51,48,49,50,55,52,59,56,62]
tuule_kiirus = [5.7,4.7,4.3,4.4,4.5,4.8,3.9,4.5,4.5,5.2,4.5,4.4,4.5,5.0,5.1,5.7,5.9,6.7,5.8,5.5,5.3]
# Adnmed on siit: https://www.ilmateenistus.ee/meri/vaatlusandmed/roomassaare/10-minuti-andmed/

ax=plt.subplot(polar=True)
ax.bar(tuule_suund_kraadides, tuule_kiirus,
    color="blue",
    # color=plt.cm.jet(tuule_kiirus),
    width=0.5,
    # width=heights,
    bottom=0.0,
    edgecolor='k',
    alpha=0.5,
    label='Tuule kiirus')

ax.set_ylim(0, 8)
ax.set_xticklabels(['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])

plt.grid(True)
plt.legend()
plt.title("Tuule suund ja kiirus X linnas")

plt.show()
