#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

import numpy as np
import matplotlib.pyplot as plt

def derivative(a,b,n):
    """derivative(a, b, n=1000)
    Generate a matrix used for obtaining the first derivative.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        D : A nxn matrix that represents the finite difference operation
    """
    dx = (b-a)/(n-1)
    D=(1/2)*(np.eye(n+1,n+1,1)-np.eye(n+1,n+1,-1))
    D[0][0] = -1
    D[-1][-1] = 1
    D[0][1] = 1
    D[-1][-2] = -1
    D = D/(dx)
    return D

def second_derivative(a,b,n):
    """second_derivative(a, b, n=1000)
    Generate a matrix used for obtaining the second derivative.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        D2 : A nxn matrix that represents the finite difference operation applied to itself
    """
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
     """gen_f_array(a, b, n=1000)
    Generate a discrete approximation of y = x^2, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, f) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            f  : [f(a), ..., f(b)] Array of the function's return value at each domain point x
    """
    x = np.linspace(a,b,n+1)
    f = x**2
    return x,f

def gen_s_array(a,b,n):
    """gen_f_array(a, b, n=1000)
    Generate a discrete approximation of sin, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            s  : [s(a), ..., s(b)] Array of the function's return value at each domain point x
    """
    x = np.linspace(a,b,n+1)
    s = np.sin(x)
    return x,s

def gen_g_array(a,b,n):
    """gen_f_array(a, b, n=1000)
    Generate a discrete approximation of a gaussian bellcurve, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of the function's return value at each domain point x
    """
    x = np.linspace(a,b,n+1)
    g = np.exp((-x**2)/2)/(np.sqrt(2*np.pi))
    return x,g

def plot(x,y,D,D2,title):
    """plot(x,y,D,D2,title)
    Generate a plot of a function and its first and second derivatives.
    
    Args:
        x (array)      : Numpy array of the domain, with evenly spaced points
        y (array)      : Numpy array of the range
        D (array)      : First derivative matrix
        D2 (array)     : Second derivative matrix
        title (string) : Title of the plot
    
    Returns:
        (x, y)  : Pair of numpy arrays of float64 representing the original function
        (x, d1) : Pair of numpy arrays representing the first derivative of the function
            d1  : The first derivative matrix multiplied with the range array (y)
        (x, d2) : Pair of nummpy arrays representing the second derivative of the function
            d2  : The second derivative matrix multiplied with the rage array (y)

    """
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