# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:11:07 2019

@author: mohamedhozayen
"""

import random


class UE:
    """
        A class used to represent an instance for a User Equipment 

        SINR values: 
           https://usatcorp.com/faqs/understanding-lte-signal-strength-values/
           excellent s > 12.5 
           good      10 < s < 12.5 
           fair      7 < s < 10 
           poor      s < 7
    """

    def __init__(self, id_num, binary_variable, SINR, minimum_data_rate=5):
        self.id = id_num
        self.binary_variable = binary_variable
        self.sinr = SINR
        self.min_data_rate = minimum_data_rate #bps/Hz
        #self.loc_x = random.randint(0, 500)
        #self.loc_y = random.randint(0, 500)
    
    
    
    
    
    
    
    
    
    
    
    
    