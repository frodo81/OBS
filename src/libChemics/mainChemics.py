'''
Created on 25.09.2011

@author: bernd
'''

from math import pow

class Peukert(object):
    '''
    classdocs
    '''    
    def __init__(self, Capacity, I_discharge, Peukertnumber):
        '''
        Constructor
        '''
        self.Capacity = Capacity
        self.I_discharge = I_discharge
        self.Peukertnumber = Peukertnumber
    
    def PeukertQuotation(self):
        time = (self.Capacity / pow(self.I_discharge,self.Peukertnumber)) * pow(1,self.Peukertnumber-1)       
        return (time, time*self.I_discharge)
         
    
        