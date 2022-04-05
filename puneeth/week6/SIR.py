#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:15:40 2022

@author: puneeth

SIR Models
"""

import distributions as dst 
import matplotlib.pyplot as plt
import random as rnd



class SIR: 
    def __init__(self,b,v,u,g,S,I,R):
        self.b = b
        self.v = v
        self.u = u
        self.g = g 
        self.S_start = S 
        self.I_start = I 
        self.R_start = R
    
    def path(self, time):
        t = 0
        S = self.S_start 
        I = self.I_start 
        R = self.R_start
        
        pop_size = {'t':[t], 's':[S], 'i':[I], 'r':[R]}
        
        
        while t < time:           
            if S+I == 0 : 
                pop_size['t'] += [time]
                pop_size['s'] += [ S ]
                pop_size['i'] += [ I ]
                pop_size['r'] += [ R ]
                break 
            event_rates = [self.b*S,self.v*S*I,self.u*I,self.g*I]
            exp_dst = dst.exponential(sum(event_rates))
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            pop_size['t'] += [t]
            event = rnd.choices([0,1,2,3],[self.b*S,self.v*S*I,self.u*I,self.g*I])[0]
#            print(S,I,R,event)
            if event == 0 : 
                S += 1 
            elif event == 1: 
                S -= 1 
                I += 1 
            elif event == 2: 
                I -= 1
            elif event == 3: 
                I -= 1 
                R += 1 
                
            pop_size['s'] += [ S ]
            pop_size['i'] += [ I ]
            pop_size['r'] += [ R ]
        return pop_size 
    
if __name__ == "__main__": 
#    b = 1
#    v = 2
#    u = 0
#    g = 1
#    S = 100
#    I = 1
#    R = 0
#    
#    sir = SIR(b,v,u,g,S,I,R)
#    path_sample = sir.path(100)
#    t_list = path_sample['t']
#    S_list = path_sample['s']
#    I_list = path_sample['i']
#    R_list = path_sample['r']
#    
#    plt.plot(t_list,S_list,label = 'S')
#    plt.plot(t_list,I_list,label = 'I')
#    plt.plot(t_list,R_list,label = 'R')
#    plt.legend()
#    plt.title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
    
    """ Effect of increasing u """
    
#    b = 0.1
#    v = 0.02
#    u_list = [0,0.05,0.1,0.15,0.2]
#    g = 0.1
#    S = 100
#    I = 1
#    R = 0
#    fig, ax = plt.subplots(1,len(u_list), sharey = True)
#    for i in range(len(u_list)):
#        u = u_list[i]
#        sir = SIR(b,v,u,g,S,I,R)
#        path_sample = sir.path(50)
#        t_list = path_sample['t']
#        S_list = path_sample['s']
#        I_list = path_sample['i']
#        R_list = path_sample['r']
#        
#        ax[i].plot(t_list,S_list,label = 'S')
#        ax[i].plot(t_list,I_list,label = 'I')
#        ax[i].plot(t_list,R_list,label = 'R')
#        ax[i].legend()
#        ax[i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
    
    """ Effect of increasing b """
    
#    b_list = [0,0.05,0.1,0.15,0.2]
#    v = 0.02
#    u = 0.1
#    g = 0.1
#    S = 100
#    I = 1
#    R = 0
#    fig, ax = plt.subplots(1,len(b_list), sharey = True)
#    for i in range(len(b_list)):
#        b = b_list[i]
#        sir = SIR(b,v,u,g,S,I,R)
#        path_sample = sir.path(30)
#        t_list = path_sample['t']
#        S_list = path_sample['s']
#        I_list = path_sample['i']
#        R_list = path_sample['r']
#        
#        ax[i].plot(t_list,S_list,label = 'S')
#        ax[i].plot(t_list,I_list,label = 'I')
#        ax[i].plot(t_list,R_list,label = 'R')
#        ax[i].legend()
#        ax[i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
#    
    """ Effect of increasing v """
    
#    b = 0.1
#    v_list = [0.01,0.015,0.02,0.025,0.03]
#    u = 0.1
#    g = 0.1
#    S = 100
#    I = 1
#    R = 0
#    fig, ax = plt.subplots(1,len(v_list), sharey = True)
#    for i in range(len(v_list)):
#        v = v_list[i]
#        sir = SIR(b,v,u,g,S,I,R)
#        path_sample = sir.path(30)
#        t_list = path_sample['t']
#        S_list = path_sample['s']
#        I_list = path_sample['i']
#        R_list = path_sample['r']
#        
#        ax[i].plot(t_list,S_list,label = 'S')
#        ax[i].plot(t_list,I_list,label = 'I')
#        ax[i].plot(t_list,R_list,label = 'R')
#        ax[i].legend()
#        ax[i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
    
    """ Effect of increasing g """
    
    b = 0.1
    v = 0.02
    u = 0.1
    g_list = [0.02,0.06,0.1,0.14,0.18]
    S = 100
    I = 1
    R = 0
    fig, ax = plt.subplots(1,len(g_list), sharey = True)
    for i in range(len(g_list)):
        g = g_list[i]
        sir = SIR(b,v,u,g,S,I,R)
        path_sample = sir.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        
        ax[i].plot(t_list,S_list,label = 'S')
        ax[i].plot(t_list,I_list,label = 'I')
        ax[i].plot(t_list,R_list,label = 'R')
        ax[i].legend()
        ax[i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))