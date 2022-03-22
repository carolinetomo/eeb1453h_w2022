#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 01:07:27 2022

@author: puneeth
"""


import math

class normal:
    def __init__(self, mean = 0.0, sd = 1.0):
        self.mean = mean
        self.sd = sd

    def pdf(self, x):
        # HINT: to calculate the pdf, you will need math.e, math.pi, and math.sqrt
        density = ( 1/(self.sd*math.sqrt(2*math.pi) ) )*math.e**( -0.5*( (x-self.mean)/self.sd )**2 ) # here, you will plug the value X into the PDF for a normal distribution
        return density