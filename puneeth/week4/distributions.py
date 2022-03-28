#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:27:31 2022

@author: puneeth
"""

import random as rnd 
import math

class normal :
    def __init__(self, m = 0.0, var = 1.0 ):
        self.mean = m
        self.var = var 
        self.sd = math.sqrt(self.var)
    
    def random_list(self, n = 1):
        out = [] 
        while len(out) < n: 
            x = rnd.random() 
            y = rnd.random() 
            xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*self.sd)+self.mean)
            ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*self.sd)+self.mean)
            out += [xnorm,ynorm]
#        print(out)
        out = out[0:n] #since sometimes it can be greater than n since we add two at a time. 
        return out
    
    def pdf(self, x):
        # HINT: to calculate the pdf, you will need math.e, math.pi, and math.sqrt
        density = ( 1/(self.sd*math.sqrt(2*math.pi) ) )*math.e**( -0.5*( (x-self.mean)/self.sd )**2 ) # here, you will plug the value X into the PDF for a normal distribution
        return density
    
    def moment(self,i,n): 
        a = self.random_list(n)
        ith_moments = [ val**i for val in a ]
        return sum(ith_moments)/n
        
if __name__ == "__main": 
    example = normal(1,2)