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


def plot_impulses(t, x):
    # nan values won't be shown, but the x- axis will be spread to accomodate the array size
    base = np.zeros_like(t)
    for i in range(len(base)):
        base[i] = np.nan

    posisitve_indexes = np.where(x > 0)
    
    negative_indexes = np.where(x < 0)

    if np.any(posisitve_indexes):
        plt.stem(
            t[posisitve_indexes], x[posisitve_indexes], markerfmt="^", basefmt="k-"
        )

    if np.any(negative_indexes):
        plt.stem(t[negative_indexes], x[negative_indexes], markerfmt="v", basefmt="k-")

    plt.stem(t, base, basefmt="k-")


def sampled_to_discrete(x, discrete_Ts):
    return x[::discrete_Ts]


def rect(x):
    output = np.zeros_like(x)
    for i in range(len(x)):
        if abs(x[i]) < 0.5:
            output[i] = 1

    return output
