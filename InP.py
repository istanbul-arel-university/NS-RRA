# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:12:22 2019

@author: mohamedhozayen
"""
import BS

class InfrastructureProvider:
    """
        A class used to represent an instance for an Infrastructure Provider 
    """

    def __init__(self, num_BS, num_channels):
        self.num_BS = num_BS
        self.num_channels = num_channels
        self.stations = self.create_BaseStations()

    def create_BaseStations(self):
        return [BS.BaseStation(id_num=i, num_channels=self.num_channels) for i in range(self.num_BS)]
    
    def buildVRPreferenceProfile(self):
        """
        build VNO Preference Profile
        """
        return

    def printAbout(self):
        for i in self.stations:
            print'Base Station ID: ', i.id
            print'Base Station Transmit Power: ', i.transmit_power
            print'number of channels: ', i.num_channels
            for j in i.v_rsc:
                print
                print'VR id:', j.id
                print'VR price: {:.2f}'.format(j.price)
                print'VR bandwidth:', j.bandwidth
                print 'VR transmit power:', j.transmit_power
            