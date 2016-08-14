# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:18:04 2016

@author: LY
"""


import math
import numpy as np
import matplotlib.pyplot  as plt

import os, re




########
path = r'D:\Users\LY\Documents\Ansoft\MyDesigns\Transmitarray\201608\0808'
#
file_name1 = r'angle_90deg_25_1.csv'
file_name2 = r'dB_90deg_25_1.csv'

file_path1 = path + '\\'+ file_name1
file_path2 = path +  '\\'+file_name2

f1 = open(file_path1, 'r')
col1 = []
for line in f1.readlines():
    line = line.replace('\n',' ').split(',')
    col1.append(line[1])
col1 =[eval(i)/180*np.pi for i in col1[1:-1]]

f2 = open(file_path2, 'r')
col2 = []
for line in f2.readlines():
    line = line.replace('\n',' ').split(',')
    col2.append(line[1])
col2 =[10**(eval(i)/20) for i in  col2[1:-1]]



f1.close()
f2.close()




###########


er = 2.5
gammar = (1-er**0.5)/(1+er**0.5)
beta_Ld = [45, 90, 135]
f = 13.58

lambda0 = 300/f
plt.figure(1)     #  利用 np.angle  和 np.abs 函数进行计算

N = len(beta_Ld)
theta = np.arange(0, 2*np.pi, 0.02)
plt.polar(theta, np.ones_like(theta), lw=2)

for i in range(N):
    S12 = S21 = (1-gammar**2)*np.exp(-1j*beta_Ld[i])/(1 - gammar **2 *np.exp(-1j*2*beta_Ld[i]))
    S11 = S22 = gammar*(1-np.exp(-1j*2*beta_Ld[i]))/(1 - gammar **2 *np.exp(-1j*2*beta_Ld[i]))
    mag_S21_c =np.abs( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) )))
    plt.polar(np.angle( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) ))),np.abs( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) ))))


#line1,= plt.polar(col1, col2, 'o', label = '2.5 90deg')
plt.rgrids(np.arange(0.2,1,0.2),angle =130)
plt.thetagrids(np.linspace(0,330, 12))


plt.show()


###########################



