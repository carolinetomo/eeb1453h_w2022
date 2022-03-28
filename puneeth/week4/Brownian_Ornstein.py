#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:16:42 2022

@author: puneeth
"""
import math
import random as rnd 
import distributions as dst 
import matplotlib.pyplot as plt 

def moment(i,val_list): 
    ith_moments = [ val**i for val in val_list ]
    return sum(ith_moments)/float(len(val_list))

class brownian_motion(): 
    def __init__(self,start,rate):
        self.start = start 
        self.rate = rate
    
    def path(self,final_time,dt=0.01): 
        
        t = 0
        time = [t]
        
        cur_pos = self.start
        positions = [cur_pos]
        
        jump_dist = dst.normal(0, dt)
        
        while t < final_time: 
            jump = self.rate*jump_dist.random_list()[0]
            
            cur_pos = cur_pos + jump
            positions = positions + [ cur_pos ]
            
            t = t + dt
            time = time + [ t ]
            
        return [time,positions]

class ornstein_uhlenback():
    def __init__(self,start,rate,pull):
        self.start = start 
        self.rate = rate
        self.pull = pull
    
    def path(self,final_time,dt=0.01): 
        
        t = 0
        time = [t]
        
        cur_pos = self.start
        positions = [cur_pos]
        
        jump_dist = dst.normal(0, dt)
        
        while t < final_time: 
            jump = -self.pull*cur_pos*dt + self.rate*jump_dist.random_list()[0]
            
            cur_pos = cur_pos + jump 
            positions = positions + [ cur_pos ]
            
            t = t + dt
            time = time + [ t ]
            
        return [time,positions]
    
fig, ax = plt.subplots(1,2)
fig.suptitle('Random paths')
sample_size = 1000
rate = 2 #standard deviate
total_time = 10

bm = brownian_motion(0,rate)
path_list = [] 

#Plotting multiple brownian paths
for i in range(sample_size):
    print(i)
    time, path = bm.path(total_time)
    path_list += [path]
    ax[0].plot(time,path)

ax[0].set_xlabel('Time')
ax[0].set_ylabel('Position')
ax[0].set_title('Brownian')
#Restructuring the data to get all the positions at a time together (as opposed to all time points for same path)
positions_tim = [ [] for ind in range(len(time))]
expected_dist = [ [] for ind in range(len(time))]
for ind in range(len(time)): 
    positions_tim[ind] = [ path[ind] for path in path_list ]
    #Creating a same size sample from normal distribution with mean 0 and var t 
    expected_dist[ind] = dst.normal(0,rate**2*time[ind]).random_list(sample_size)

#Plotting moments of the paths at each time point
m = 3 
fig_2, ax_2 = plt.subplots(1,m)
for i in range(1,m+1): 
    moments = [ moment(i, positions_tim[ind]) for ind in range(len(time))]
    normal_moments = [ moment(i, expected_dist[ind]) for ind in range(len(time))]
    ax_2[i].plot( range(len(time)), moments )
    ax_2[i].scatter( range(len(time)), normal_moments )
    
#Plotting multiple brownian paths
rate_ou = 2
pull_ou = 1
ou = ornstein_uhlenback(0,rate_ou,pull_ou)
path_list = []

for i in range(sample_size):
    print(i)
    time, path = ou.path(total_time)
    path_list += [path]
    ax[1].plot(time,path)
    
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Position')
ax[1].set_title('Ornstein-Uhlenbeck')

#Restructuring the data to get all the positions at a time together (as opposed to all time points for same path)
positions_tim = [ [] for ind in range(len(time))]
expected_dist = [ [] for ind in range(len(time))]
for ind in range(len(time)): 
    positions_tim[ind] = [ path[ind] for path in path_list ]
    #Creating a same size sample from normal distribution with mean 0 and var t 
    expected_dist[ind] = dst.normal(0,rate_ou**2*(1-math.e**(-2*pull_ou*time[ind]))/float(2*pull_ou)).random_list(sample_size)
    
#Plotting moments of the paths at each time point

