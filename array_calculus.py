#!/usr/bin/env python3
# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

import numpy as np
import matplotlib.pyplot as plt

def derivative(a,b,n):
    dx = (b-a)/(n-1)
    D = (np.eye(n,n,1)-np.eye(n,n,-1))
    D[0][0] = -2
    D[-1][-1] = 2
    D[0][1] = 2
    D[-1][-2] = -2
    D = D/(dx*2)
    return D
