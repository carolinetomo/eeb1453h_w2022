#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:47:36 2022

@author: puneeth

Wright-Fisher Haploid Model
"""
import random as rnd 
import distributions as dst 
import matplotlib.pyplot as plt 

class wright_fisher:
    def __init__(self, pop_size, p_start, mu=0, nu=0, s=0): 
        self.start = float(p_start)
        self.N = pop_size
        self.mu = float(mu)
        self.nu = float(nu)
        self.s = float(s)
    def path(self, time = 100): 
        p0 = self.start
        p_list = [p0]
        
        for gen in range(time): 
            p_current = p_list[-1]
            
            sel_change = self.s*p_current*(1-p_current)/(1+self.s*p_current)
            p_current += sel_change #selection
            
            mut_change = -self.mu*p_current + self.nu*(1-p_current)
            p_current += mut_change #mutation
            
            bin_dist = dst.binomial(self.N,p_current)
            new_size = bin_dist.random_list(1)[0] #drift 
            
            p_new = new_size/float(self.N)
            p_list += [p_new]
            
        return p_list

if __name__ == "__main__": 
    wf = wright_fisher(1000,0.5) 
    reps = 100 
    for rep in range(reps): 
        print(rep)
        path = wf.path() 
        plt.plot(range(len(path)), path)
    plt.ylim([0,1])
    plt.show()