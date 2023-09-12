#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:45:20 2023

Auxiliary functions for the notebook. Takes inspiration from:
https://github.com/aldebaro/dsp-telecom-book-code

@author: eduardofilho
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_impulses(t, x, label = ''):

    posisitve_indexes = np.where(x > 0)
    
    negative_indexes = np.where(x < 0)

    if np.any(posisitve_indexes):
        plt.stem(
            t[posisitve_indexes], x[posisitve_indexes], markerfmt="^", basefmt="k-", label = label
        )

    if np.any(negative_indexes):
        plt.stem(t[negative_indexes], x[negative_indexes], markerfmt="v", basefmt="k-")

    plt.plot(t,np.zeros_like(t), color = 'k')


def sampled_to_discrete(x, discrete_Ts):
    # Could be made more complete through the following:
    # Divide the length of x by discrete_Ts
    # Find the first non-zero index, store this value and following
    # ones with discrete_Ts as step size, in case all of the estimated
    # Samples haven't been counted, now do the same process but backwards
    return x[::discrete_Ts]


def rect(x):
    output = np.zeros_like(x)
    for i in range(len(x)):
        if abs(x[i]) < 0.5:
            output[i] = 1

    return output
