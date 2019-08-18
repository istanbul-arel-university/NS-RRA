#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:54:09 2019

@author: mohamedhozayen
"""
import math
import numpy as np

def achievable_data_rate(binary_valuable, bandwidth, sinr):
    rate =  binary_valuable * bandwidth * math.log10(1+sinr)
    return rate

def SINR():
    #not implemented!!
    values = np.random.rayleigh()
    return values