# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:13:48 2019

@author: mohamedhozayen
"""

from numpy import random

class Channel:
    """
        A class used to represent an instance for an OFDMA Channel
    """

    
    def __init__(self, price=None, bandwidth=180):
        self.bandwidth = bandwidth   
        if price is None:
            price = random.randint(15, 85)
        self.price = price