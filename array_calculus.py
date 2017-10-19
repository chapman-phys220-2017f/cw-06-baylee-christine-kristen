#!/usr/bin/env python3
# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

import numpy as np
import matplotlib.pyplot as plt

def derivative(a,b,n):
    dx = (b-a)/(n-1)
    D=(1/2)*(np.eye(n+1,n+1,1)-np.eye(n+1,n+1,-1))
    D[0][0] = -1
    D[-1][-1] = 1
    D[0][1] = 1
    D[-1][-2] = -1
    D = D/(dx)
    return D

def second_derivative(a,b,n):
    dx = (b-a)/(n-1)
    D = np.eye(n,n,1)