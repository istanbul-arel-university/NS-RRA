# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:13:27 2019

@author: mohamedhozayen
"""
import VR as vr

class BaseStation:
    """
        A class used to represent an instance for a Base Station
    """

    def __init__(self, id_num, num_channels, transmit_power=43):
        self.id = id_num
        self.num_channels = num_channels
        self.transmit_power = transmit_power #dBm
        self.loc_x = 0
        self.loc_y = 0
        self.v_rsc = self.create_channels()

    def create_channels(self):
        power = self.transmit_power/self.num_channels #each channel equal tranmit power
        return [vr.VirtualResource(id_num=i, transmit_power = power) for i in range(self.num_channels)]
       