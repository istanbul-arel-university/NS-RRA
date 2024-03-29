#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:15:39 2019

Script - Matching Game Algorithm 

@author: mohamedhozayen
"""
import InP
import VNO
import numpy as np

num_vnos = 3

InP = InP.InfrastructureProvider(num_BS=1, num_channels=5)
opts = [VNO.VirtualNetworkOperator(id_num=i, num_users=5) for i in range(num_vnos)]

#InP.printAbout()
#[opts[i].printAbout() for i in range(len(opts))]

[i.buildUsersPreferenceProfile(InP) for i in opts]

for i in range(num_vnos):
    for y in opts[i].users:
        for k in y.vrs_data:
            if k['ach-rate'] < 5:
                print k
#print opts[1].vrs_data['vrs-data'][2]['ach-rate']
#for i in range(50):
#    print(np.random.rayleigh())
