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

class ornstein_uhlbeck():
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

""" Brownian Motion """

sample_size = 1000
rate = 2 #standard deviate
total_time = 10
bm = brownian_motion(0,rate)


#Plotting multiple brownian paths
fig, ax = plt.subplots(1,2)
fig.suptitle('Random paths')
path_list = [] 

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
m = 4
fig_m,ax_m = plt.subplots(1,m)
for i in range(1,m+1):
    moment_list = [ moment(i,val_list) for val_list in positions_tim ]
    exp_moment_list = [ moment(i,val_list) for val_list in expected_dist ]
    ax_m[i-1].scatter(time,exp_moment_list,label = str(i)+' normal moment',marker = '*', s = 1, color = 'blue' )
    ax_m[i-1].plot(time,moment_list,label = str(i)+' moment',color = 'red' )
    ax_m[i-1].set_xlabel('Time')
    ax_m[i-1].set_ylabel('E[x**' + str(int(i)) + ']' )
    ax_m[i-1].legend(loc = 'upper left')
fig_m.suptitle('Moment of Brownian motion') 

#Changing step size 
m = 3
dt_list = [ 10**(-i) for i in range(m) ] # dt_list = [ 1,-0.1,-0.01.-0.001 ]
fig_dt, ax_dt = plt.subplots(1,m)
path_list = [] 
for ind in range(m):
    dt = dt_list[ind]
    print(dt)
    for i in range(sample_size):
        time, path = bm.path(total_time,dt)
        ax_dt[ind].plot(time,path)
    ax_dt[ind].set_title('dt = ' + str(dt))
    ax_dt[ind].set_xlabel('Time')
    ax_dt[ind].set_ylabel('Position')
fig_dt.suptitle('Changing size of time step - Brownian Motion')

""" Ornstein-Uhlenbeck Motion """

#Plotting multiple ornstein-uhlenbeck paths
rate_ou = 2
pull_ou = 1
ou = ornstein_uhlbeck(0,rate_ou,pull_ou)
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
m = 4
fig_m2,ax_m2 = plt.subplots(1,m)
for i in range(1,m+1):
    moment_list = [ moment(i,val_list) for val_list in positions_tim ]
    exp_moment_list = [ moment(i,val_list) for val_list in expected_dist ]
    ax_m2[i-1].scatter(time,exp_moment_list,label = str(i)+' normal moment',marker = '*', s = 1, color = 'blue' )
    ax_m2[i-1].plot(time,moment_list,label = str(i)+' moment',color = 'red' )
    ax_m2[i-1].set_xlabel('Time')
    ax_m2[i-1].set_ylabel('E[x**' + str(int(i)) + ']' )
    ax_m2[i-1].legend(loc = 'lower right')
fig_m2.suptitle('Moment of Ornstein-Uhlenbeck motion') 

#Changing step size 
m = 3
dt_list = [ 10**(-i) for i in range(m) ] # dt_list = [ 1,-0.1,-0.01.-0.001 ]
fig_dt2, ax_dt2 = plt.subplots(1,m)
path_list = [] 
for ind in range(m):
    dt = dt_list[ind]
    print(dt)
    for i in range(sample_size):
        time, path = ou.path(total_time,dt)
        ax_dt2[ind].plot(time,path)
    ax_dt2[ind].set_title('dt = ' + str(dt))
    ax_dt2[ind].set_xlabel('Time')
    ax_dt2[ind].set_ylabel('Position')
fig_dt2.suptitle('Changing size of time step - Ornstein Uhlenbeck')
