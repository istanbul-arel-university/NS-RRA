#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:15:39 2019

Script - Matching Game Algorithm 

@author: mohamedhozayen
"""
import InP
import VNO

num_vnos = 3

InP = InP.InfrastructureProvider(num_BS=1, num_channels=5)
opts = [VNO.VirtualNetworkOperator(id_num=i) for i in range(num_vnos)]