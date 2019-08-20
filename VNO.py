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
import formulas

class VirtualNetworkOperator:
    """
        A class used to represent an instance for a Virtual Netowrk Operator 
    """
    

    def __init__(self, id_num, num_users=5):
        self.id = id_num
        self.num_users = num_users
        self.users = self.create_users()
        self.sampl = np.random.uniform(low=4.2, high=6, size=(10000,))
        self.vrs_data = {"vrs-data":[]}

    def create_users(self):
        return [UE.UserEquipment(id_num=i) for i in range(self.num_users)]
    
    def add_vr(self, vr):
        self.vrs_data["vrs-data"].append(vr)

    def buildUsersPreferenceProfile(self, stations):
        """
        build VNO Preference Profile
        """

        for b in stations.stations:
            for c in b.v_rsc:
                vr = {}
                vr["base-id"] = b.id
                vr["vr-id"] = c.id
                vr["vr-price"] = c.price
                vr["ach-rate"] = None #for each user calculations
                self.add_vr(vr)
        
        for i in range(self.num_users):
            temp = list(self.vrs_data['vrs-data'])
            for y in temp:
                y["ach-rate"] = self.sampl[np.random.randint(len(self.sampl-1))] 
            self.users[i].vrs_data = temp
            self.users[i].pk()
#                
#        print self.vrs_data
#        opts[1].vrs_data['vrs-data'][2]['ach-rate']
#        print sorted(d, key = lambda i: i['vr-price'])  
#                l1 = opts[1].users
#                a = np.asarray(l1)
#                d = opts[1].vrs_data['vrs-data']
#                d1 = sorted(d, key = lambda i: i['vr-price'])

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
