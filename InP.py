# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:12:22 2019

@author: mohamedhozayen
"""
Import BS

class InP:
    """
        A class used to represent an instance for an Infrastructure Provider 
    """

    def __init__(self, bandwidth, price, num_BS):
        self.bandwidth = bandwidth
        self.price = price 
        self.num_BS = num_BS


    def buildVRPreferenceProfile(self):
        """
        build VNO Preference Profile
        """
        return
