# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:11:07 2019

@author: mohamedhozayen
"""

import random
import math
import formulas

class UserEquipment:
    """
        A class used to represent an instance for a User Equipment 

        SINR values: 
           https://usatcorp.com/faqs/understanding-lte-signal-strength-values/
           excellent s > 12.5 
           good      10 < s < 12.5 
           fair      7 < s < 10 
           poor      s < 7
    """

    def __init__(self, id_num, minimum_data_rate=5):
        self.id = id_num
        self.binary_variable = None
        self.sinr = None
        self.min_data_rate = minimum_data_rate #bps/Hz
        self.loc_x = random.uniform(-500, 500)
        self.loc_y = random.uniform(-500, 500)
        self.distance = math.sqrt((self.loc_x - 0)**2 + (self.loc_y - 0)**2) 
        self.vrs_data = []
    
    def pk(self):
        if self.vrs_data == []:
            print "vrs_data is not yet assigned"
        
        #sort by price
        self.vrs_data = sorted(self.vrs_data, key = lambda i: i['vr-price'])
        
        #fliter -- NOT FULLY WORKING
        for i in self.vrs_data:
            if i['ach-rate'] < self.min_data_rate:
                self.vrs_data.remove(i)
      
        return self.vrs_data
    
    
    
    
    
    
    
    
    
    
    
    