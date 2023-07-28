#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:22:01 2023

@author: eduardofilho
"""
import numpy as np
import matplotlib.pyplot as plt
from sampling_utils import *


def sinc_interpolation(x_discrete,t,Ts):
    
    time_axis = t - t[0]
    x_sinc_reconstructed = np.zeros_like(time_axis)

    for i in range(len(x_discrete)):
        x_sinc_reconstructed += x_discrete[i]*np.sinc((time_axis-i*Ts)/Ts)
    
    return x_sinc_reconstructed
    

#Discrete time signal
plt.subplot(311)
max_n = 4
xn = np.array([1,-3,3])
N = len(xn)
xn_extended = np.zeros(2*max_n + 1)
xn_extended[max_n:max_n+N] = xn
plt.stem(np.arange(-max_n,max_n+1), xn_extended)


plt.grid()
plt.xlabel('Discrete-time n')
plt.ylabel('x[n]')


plt.subplot(312)
Ts = 0.2
time_axis = Ts*np.arange(-max_n,max_n+1)
plot_impulses(time_axis, xn_extended)
plt.plot(time_axis, np.zeros(len(time_axis)))

plt.subplot(313)
t = np.linspace(0, len(xn_extended)*Ts) + time_axis[0]# 
xt = sinc_interpolation(xn_extended,t, Ts)
x_parcels = np.zeros((len(xn),len(t)))

for i in range(4,7):
    single_sample = np.zeros_like(xn_extended)
    single_sample[i] = xn_extended[i]
    x_parcels[i-4] = sinc_interpolation(single_sample, t, Ts)
    


#t = t + time_axis[0]
plt.plot(t, xt)
plt.plot(t,x_parcels[0], linestyle='dashed')
plt.plot(t,x_parcels[1], linestyle='dashed')
plt.plot(t,x_parcels[2], linestyle='dashed')

plt.show()





