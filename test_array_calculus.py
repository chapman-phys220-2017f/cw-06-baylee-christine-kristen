#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 6

"""Classwork 6 Tests"""

import nose
import array_calculus as calc
import numpy as np

def test_first_and_Second_derivatives():
    actual = calc.second_derivative(0,9,9)
    trial = calc.derivative(0,9,9)@calc.derivative(0,9,9)
    print("Testing first derivative: ",actual," ?= ",trial)
    np.testing.assert_array_almost_equal(actual, trial)
