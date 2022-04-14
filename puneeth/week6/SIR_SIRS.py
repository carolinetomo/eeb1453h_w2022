#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:15:40 2022

@author: puneeth

SIR and SIRS Models
"""

import distributions as dst 
import matplotlib.pyplot as plt
import random as rnd



class SIR: 
    def __init__(self,b,v,u,g,S,I,R):
        self.b = b #birth rate S += 1 
        self.v = v #infection rate S -> I
        self.u = u #death rate due to infection I -= 1 
        self.g = g #recovery rate I -> R
        
        self.S_start = S #number of susceptible 
        self.I_start = I #number of infected
        self.R_start = R #number of recoverd
    
    def path(self, time=30):
        t = 0
        S = self.S_start 
        I = self.I_start 
        R = self.R_start
        D = 0 #number of deceased
        
        pop_size = {'t':[t], 's':[S], 'i':[I], 'r':[R], 'd':[D]}
        
        
        while t < time:           
            #Computing the rates of different events. See below for what each event refers to
            event_rates = [self.b*S,self.v*S*I,self.u*I,self.g*I]
            event_rate = float(sum(event_rates))
            
            #stop if no events are to happen or if S crosses a threshols (which means the infection has been avoided altogether)
            if event_rate == 0 or S > 3*self.S_start: 
                pop_size['t'] += [time]
                pop_size['s'] += [ S ]
                pop_size['i'] += [ I ]
                pop_size['r'] += [ R ]
                pop_size['d'] += [ D ]
                break 
                
            #Compute the time for next event 
            exp_dst = dst.exponential(sum(event_rates))
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            pop_size['t'] += [t]
            
            #Decide which event occurs.
            event = rnd.choices([0,1,2,3],[self.b*S,self.v*S*I,self.u*I,self.g*I])[0] 
            #0-birth, 1-infection, 2-death due to infection, 3-recovery 
            
            if event == 0 : 
                S += 1 
            elif event == 1: 
                S -= 1 
                I += 1 
            elif event == 2: 
                I -= 1
                D += 1 
            elif event == 3: 
                I -= 1 
                R += 1 
                
            pop_size['s'] += [ S ]
            pop_size['i'] += [ I ]
            pop_size['r'] += [ R ]
            pop_size['d'] += [ D ]
            
        return pop_size 
    
    # Compute the mean population size at the end of the run 
    def mean_pop(self , sample=100, time=30): 
        P_list = [] 
        D_list = []
        for sam in range(sample): 
            pop_sam = self.path(time)
            tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
            P_list += [tot_size]
            D_list += [ pop_sam['d'][-1] ]
        mean_size = dst.mean(P_list)
        mean_deaths = dst.mean(D_list)
        return [mean_size, mean_deaths]
    
class SIRS: 
    def __init__(self,b,v,u,g,w,S,I,R):
        self.b = b
        self.v = v
        self.u = u
        self.g = g
        self.w = w 
        
        self.S_start = S #number of susceptible 
        self.I_start = I #number of infected
        self.R_start = R #number of recoverd
    
    def path(self, time=30):
        t = 0
        S = self.S_start 
        I = self.I_start 
        R = self.R_start
        D = 0 #number of deceased
        
        pop_size = {'t':[t], 's':[S], 'i':[I], 'r':[R], 'd':[D]}
        
        exp_dst = dst.exponential(1.0) #Create an exponential distribution. The rate will updated at each round.
        while t < time:           
            event_rates = [self.b*S,self.v*S*I,self.u*I,self.g*I,self.w*R]
            event_rate = float(sum(event_rates))
            
            #stop if no events are to happen or if S crosses a threshols (which means the infection has been avoided altogether)
            if event_rate == 0 or S > 3*self.S_start: 
                pop_size['t'] += [time]
                pop_size['s'] += [ S ]
                pop_size['i'] += [ I ]
                pop_size['r'] += [ R ]
                pop_size['d'] += [ D ]
                break 
                
            #Compute the time for the next event 
            exp_dst = dst.exponential(sum(event_rates))
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            pop_size['t'] += [t]
            
            #Decide which event occurs
            event = rnd.choices([0,1,2,3,4],event_rates)[0] 
            #0-birth, 1-infection, 2-death due to infection, 3-recovery, 4-recovered loses immunity 
            if event == 0 : 
                S += 1 
            elif event == 1: 
                S -= 1 
                I += 1 
            elif event == 2: 
                I -= 1
                D += 1 
            elif event == 3: 
                I -= 1 
                R += 1 
            elif event == 4: 
                R -= 1
                S += 1
                
            pop_size['s'] += [ S ]
            pop_size['i'] += [ I ]
            pop_size['r'] += [ R ]
            pop_size['d'] += [ D ]
            
        return pop_size 
    
    def mean_pop(self , sample=100, time=30): 
        P_list = [] 
        D_list = []
        for sam in range(sample): 
            pop_sam = self.path(time)
            tot_size = pop_sam['s'][-1] + pop_sam['i'][-1] + pop_sam['r'][-1]
            P_list += [tot_size]
            D_list += [ pop_sam['d'][-1] ]
        mean_size = dst.mean(P_list)
        mean_deaths = dst.mean(D_list)
        return [mean_size, mean_deaths]
    
if __name__ == "__main__": 
    b = 1
    v = 2
    u = 0
    g = 1
    S = 100
    I = 1
    R = 0
    
    """ One instance """
    sir = SIR(b,v,u,g,S,I,R)
    path_sample = sir.path(100)
    t_list = path_sample['t']
    S_list = path_sample['s']
    I_list = path_sample['i']
    R_list = path_sample['r']
    
    plt.plot(t_list,S_list,label = 'S')
    plt.plot(t_list,I_list,label = 'I')
    plt.plot(t_list,R_list,label = 'R')
    plt.legend()
    plt.title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
    
    """ Effect of increasing u """
    b = 0.1
    v = 0.02
    u_list = [0,0.05,0.1,0.15,0.2]
    g = 0.1
    S = 100
    I = 1
    R = 0
    fig, ax = plt.subplots(2,len(u_list)+1, sharey = True)
    MP_list = []
    MD_list = []
    
    for i in range(len(u_list)):
        u = u_list[i]
        print(u)
        sir = SIR(b,v,u,g,S,I,R)
        path_sample = sir.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[0][i].plot(t_list,S_list,label = 'S')
        ax[0][i].plot(t_list,I_list,label = 'I')
        ax[0][i].plot(t_list,R_list,label = 'R')
        ax[0][i].plot(t_list,D_list,label = 'D')
        
        ax[0][i].legend()
        ax[0][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sir.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[0][-1].plot(u_list,MP_list, label='Mean Pop Size')
    ax[0][-1].plot(u_list,MD_list, label='Mean Deaths')
    ax[0][-1].set_xlabel('death rate u')
    ax[0][-1].set_title('Mean Size')
    ax[0][-1].legend()
    
    
    MP_list = []
    MD_list = []
    
    w = 0.2
    for i in range(len(u_list)):
        u = u_list[i]
        print(u)
        sirs = SIRS(b,v,u,g,w,S,I,R)
        path_sample = sirs.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[1][i].plot(t_list,S_list,label = 'S')
        ax[1][i].plot(t_list,I_list,label = 'I')
        ax[1][i].plot(t_list,R_list,label = 'R')
        ax[1][i].plot(t_list,D_list,label = 'D')
        
        ax[1][i].legend()
        ax[1][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sirs.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[1][-1].plot(u_list,MP_list, label='Mean Pop Size')
    ax[1][-1].plot(u_list,MD_list, label='Mean Deaths')
    ax[1][-1].set_xlabel('death rate u')
    ax[1][-1].set_title('Mean Size')
    ax[1][-1].legend()
    
    fig.suptitle('SIR Model (Row 1) and SIRS Model (Row 2, w = ' +str(w)+ ')' )
    fig.supxlabel('Time')
    fig.supylabel('Size')
    
    
    """ Effect of increasing b """
    
    b_list = [0,0.05,0.1,0.15,0.2]
    v = 0.02
    u = 0.1
    g = 0.1
    S = 100
    I = 1
    R = 0
    fig, ax = plt.subplots(2,len(b_list)+1, sharey = True)
    MP_list = []
    MD_list = []
    
    for i in range(len(b_list)):
        b = b_list[i]
        print(b)
        sir = SIR(b,v,u,g,S,I,R)
        path_sample = sir.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[0][i].plot(t_list,S_list,label = 'S')
        ax[0][i].plot(t_list,I_list,label = 'I')
        ax[0][i].plot(t_list,R_list,label = 'R')
        ax[0][i].plot(t_list,D_list,label = 'D')
        
        ax[0][i].legend()
        ax[0][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sir.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[0][-1].plot(b_list,MP_list, label='Mean Pop Size')
    ax[0][-1].plot(b_list,MD_list, label='Mean Deaths')
    ax[0][-1].set_xlabel('birth rate b')
    ax[0][-1].set_title('Mean Size')
    ax[0][-1].legend()
    
    
    MP_list = []
    MD_list = []
    
    w = 0.2
    for i in range(len(b_list)):
        b = b_list[i]
        print(b)
        sirs = SIRS(b,v,u,g,w,S,I,R)
        path_sample = sirs.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[1][i].plot(t_list,S_list,label = 'S')
        ax[1][i].plot(t_list,I_list,label = 'I')
        ax[1][i].plot(t_list,R_list,label = 'R')
        ax[1][i].plot(t_list,D_list,label = 'D')
        
        ax[1][i].legend()
        ax[1][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sirs.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[1][-1].plot(b_list,MP_list, label='Mean Pop Size')
    ax[1][-1].plot(b_list,MD_list, label='Mean Deaths')
    ax[1][-1].set_xlabel('birth rate b')
    ax[1][-1].set_title('Mean Size')
    ax[1][-1].legend()
    
    fig.suptitle('SIR Model (Row 1) and SIRS Model (Row 2, w = ' +str(w)+ ')' )
    fig.supxlabel('Time')
    fig.supylabel('Size')
    
    """ Effect of increasing v """
    b = 0.1
    v_list = [0.01,0.015,0.02,0.025,0.03]
    u = 0.1
    g = 0.1
    S = 100
    I = 1
    R = 0
    fig, ax = plt.subplots(2,len(v_list)+1, sharey = True)
    MP_list = []
    MD_list = []
    
    for i in range(len(v_list)):
        v = v_list[i]
        print(v)
        sir = SIR(b,v,u,g,S,I,R)
        path_sample = sir.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[0][i].plot(t_list,S_list,label = 'S')
        ax[0][i].plot(t_list,I_list,label = 'I')
        ax[0][i].plot(t_list,R_list,label = 'R')
        ax[0][i].plot(t_list,D_list,label = 'D')
        
        ax[0][i].legend()
        ax[0][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sir.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[0][-1].plot(v_list,MP_list, label='Mean Pop Size')
    ax[0][-1].plot(v_list,MD_list, label='Mean Deaths')
    ax[0][-1].set_xlabel('infection rate v')
    ax[0][-1].set_title('Mean Size')
    ax[0][-1].legend()
    
    
    MP_list = []
    MD_list = []
    
    w = 0.2
    for i in range(len(v_list)):
        v = v_list[i]
        print(v)
        sirs = SIRS(b,v,u,g,w,S,I,R)
        path_sample = sirs.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[1][i].plot(t_list,S_list,label = 'S')
        ax[1][i].plot(t_list,I_list,label = 'I')
        ax[1][i].plot(t_list,R_list,label = 'R')
        ax[1][i].plot(t_list,D_list,label = 'D')
        
        ax[1][i].legend()
        ax[1][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sirs.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[1][-1].plot(v_list,MP_list, label='Mean Pop Size')
    ax[1][-1].plot(v_list,MD_list, label='Mean Deaths')
    ax[1][-1].set_xlabel('infection rate v')
    ax[1][-1].set_title('Mean Size')
    ax[1][-1].legend()
    
    fig.suptitle('SIR Model (Row 1) and SIRS Model (Row 2, w = ' +str(w)+ ')' )
    fig.supxlabel('Time')
    fig.supylabel('Size')
    
    """ Effect of increasing g """
    b = 0.1
    v = 0.02
    u = 0.1
    g_list = [0.02,0.06,0.1,0.14,0.18]
    S = 100
    I = 1
    R = 0
    fig, ax = plt.subplots(2,len(g_list)+1, sharey = True)
    MP_list = []
    MD_list = []
    
    for i in range(len(g_list)):
        g = g_list[i]
        print(g)
        sir = SIR(b,v,u,g,S,I,R)
        path_sample = sir.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[0][i].plot(t_list,S_list,label = 'S')
        ax[0][i].plot(t_list,I_list,label = 'I')
        ax[0][i].plot(t_list,R_list,label = 'R')
        ax[0][i].plot(t_list,D_list,label = 'D')
        
        ax[0][i].legend()
        ax[0][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sir.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[0][-1].plot(g_list,MP_list, label='Mean Pop Size')
    ax[0][-1].plot(g_list,MD_list, label='Mean Deaths')
    ax[0][-1].set_xlabel('recovery rate g')
    ax[0][-1].set_title('Mean Size')
    ax[0][-1].legend()
    
    
    MP_list = []
    MD_list = []
    
    w = 0.2
    for i in range(len(g_list)):
        g = g_list[i]
        print(g)
        sirs = SIRS(b,v,u,g,w,S,I,R)
        path_sample = sirs.path(30)
        t_list = path_sample['t']
        S_list = path_sample['s']
        I_list = path_sample['i']
        R_list = path_sample['r']
        D_list = path_sample['d']
        
        ax[1][i].plot(t_list,S_list,label = 'S')
        ax[1][i].plot(t_list,I_list,label = 'I')
        ax[1][i].plot(t_list,R_list,label = 'R')
        ax[1][i].plot(t_list,D_list,label = 'D')
        
        ax[1][i].legend()
        ax[1][i].set_title('b = ' + str(b) + ',v = ' + str(v) + ',u = ' + str(u) + ',g = ' + str(g))
        
        MP,MD = sirs.mean_pop(1000,30)
        
        MP_list += [MP]
        MD_list += [MD]
    ax[1][-1].plot(g_list,MP_list, label='Mean Pop Size')
    ax[1][-1].plot(g_list,MD_list, label='Mean Deaths')
    ax[1][-1].set_xlabel('recovery rate g')
    ax[1][-1].set_title('Mean Size')
    ax[1][-1].legend()
    
    fig.suptitle('SIR Model (Row 1) and SIRS Model (Row 2, w = ' +str(w)+ ')' )
    fig.supxlabel('Time')
    fig.supylabel('Size')
    
