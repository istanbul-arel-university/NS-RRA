# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:13:27 2019

@author: mohamedhozayen
"""
import Channel as ch

class BS:
    """
        A class used to represent an instance for a Base Station
    """

    def __init__(self, id_num, num_channels, transmit_power=43):
        self.id = id_num
        self.num_channels = num_channels
        self.transmit_power = transmit_power #dBm
        self.loc_x = 0
        self.loc_y = 0
        self.channels = self.create_channels()

    def create_channels(self):
        return [ch.Channel() for i in range(self.num_channels)]
       