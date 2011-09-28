'''
Created on 25.09.2011

@author: bernd
'''

from math import pow, log10

class Constants(object):
    def __init__(self, R_gas=8.3144621, faraday=96485.3365):
        '''
        Constructor
        '''
        self.R_gas = R_gas # J/(mol K)
        self.faraday = faraday # (C / mol)


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
         
class Nernest(object):    
    '''
    classdocs
    '''
    def __init__(self):
        self.K = Constants()
        
    def commonForm(self, potenial, Q_reaction, n_elektrons=1, temp=25):            
        return potenial - (2.303 * self.K.R_gas * temp / n_elektrons * log10(Q_reaction))    
        