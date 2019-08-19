# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:08:27 2019

@author: mohamedhozayen
"""

#import UE
import numpy as np
import pandas as pd
import UE
import InP

class VirtualNetworkOperator:
    """
        A class used to represent an instance for a Virtual Netowrk Operator 
    """
    

    def __init__(self, id_num, num_users=5):
        self.id = id_num
        self.num_users = num_users
        self.users = self.create_users()
        
    def create_users(self):
        return [UE.UserEquipment(id_num=i) for i in range(self.num_users)]


    

    def buildUsersPreferenceProfile(self, stations):
        """
        build VNO Preference Profile
        """
        for b in stations.stations:
            for c in b.v_rsc:
                print c.price
            
        return

    def printAbout(self):
        print
        print'VNO id: ', self.id
        for i in self.users:
            print'User ID: ', i.id
            print'User minimum data rate: ', i.min_data_rate
            print'User Location (x,y): ({:.2f},{:.2f})'.format(i.loc_x, i.loc_y)
            print 'User distance to BS: {:.2f}'.format(i.distance)



#def main():
#    print("Hello World!")
#
#if __name__ == "__main__":
#    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
