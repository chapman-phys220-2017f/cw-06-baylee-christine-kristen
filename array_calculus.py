#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    D2 = np.eye(n+1,n+1,0)*-2+np.eye(n+1,n+1,2)+np.eye(n+1,n+1,-2)
    D2[0][0]=2
    D2[0][1]=-4
    D2[0][2]=2
    D2[1][0]=2
    D2[1][1]=-3
    D2[1][3]=1
    D2[-2][-1]=2
    D2[-2][-2]=-3
    D2[-2][-4]=1
    D2[-1][-1]=2
    D2[-1][-2]=-4
    D2[-1][-3]=2
    D2 = D2/((2*dx)**2)
    return D2

def gen_f_array(a,b,n):
    x = np.linspace(a,b,n+1)
    f = x**2
    return x,f

def gen_s_array(a,b,n):
    x = np.linspace(a,b,n+1)
    s = np.sin(x)
    return x,s

def gen_g_array(a,b,n):
    x = np.linspace(a,b,n+1)
    g = np.exp((-x**2)/2)/(np.sqrt(2*np.pi))
    return x,g

def plot(x,y,D,D2,title):
    d1 = D@y
    d2 = D2@y
    plt.plot(x,y, "gray")
    plt.plot(x,d1, "hotpink")
    plt.plot(x,d2, "darkred")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title, fontsize =20)
    plt.legend(['function','first derivative','second derivative'])
    plt.show()