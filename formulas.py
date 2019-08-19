#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:54:09 2019

@author: mohamedhozayen
"""
import math
import numpy as np
from random import uniform

def achievable_data_rate(binary_variable, bandwidth, sinr):
    rate =  binary_variable * bandwidth * math.log10(1+sinr)
    return rate

def data_rate_temp():
    return uniform(3.5,6.5) #temporarily 

def pref_func(ach_rate, min_rate):
    diff = ach_rate - min_rate
    return max(diff, 0)

def channel_gain(ue_distance):
    return np.random.rayleigh() * (ue_distance**-3)

#not implemented!!
def SINR(channel_gain, channel_power = 8, noise_power = 10**-13):
    num = (dBm2mW(channel_power)*10**-3) * channel_gain 
    den = noise_power * 1.0000
    return num/den


# Function to convert from mW to dBm
def mW2dBm(mW):
    return 10.*math.log10(mW)


# Function to convert from dBm to mW
def dBm2mW(dBm):
    return 10**((dBm)/10.)