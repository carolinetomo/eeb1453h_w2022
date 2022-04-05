#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:21:51 2022

@author: puneeth

Birth-Death Process
"""
import random as rnd 
import distributions as dst 
import matplotlib.pyplot as plt 

def arange(start,end,step):
    out = []
    val = start
    while val < end: 
        out += [round(val,10)]
        val += step
    return out

class birth_death():
    def __init__(self,start_size,b,d): 
        self.start = start_size
        self.b = b 
        self.d = d
    
    def path(self, time, dt=0.0001): 
        prob_b = self.b*dt
        prob_d = self.d*dt
        
        t = 0.0
        t_list = [t]
        
        pop_size = self.start
        pop_size_list = [pop_size]
        while t < time: 
            if pop_size == 0 : 
                pop_size_list += [pop_size]
                t_list[-1] = time
                break
            event = rnd.random() 
            if event < prob_b: 
                pop_size += 1 
                t_list += [t]
                pop_size_list += [pop_size]
            elif event < prob_b + prob_d: 
                pop_size -= 1
                t_list += [t]
                pop_size_list += [pop_size]
            t += dt 
        return [t_list, pop_size_list]
    
    def path_cont(self,time,dt=0.0001): 
        exp_dst = dst.exponential(self.b+self.d)
        
        t = 0.0
        t_list = [t]
        
        pop_size = self.start
        pop_size_list = [pop_size]
        while t < time: 
            t_diff = exp_dst.random_list(1)[0]
            t += t_diff
            t_list += [t] 
            event = rnd.random()
            if pop_size == 0 : 
                pop_size_list += [pop_size]
                t_list[-1] = time
                break
            if event < self.b/float(self.b + self.d) : 
                pop_size += 1
            elif pop_size != 0:
                 pop_size -= 1 
                 
            pop_size_list += [pop_size] 
            
        return [t_list, pop_size_list]
    
    def ext_prob(self, samples, threshold): 
        ext = 0 
        exp_dst = dst.exponential(self.b+self.d)
        for reps in range(samples): 
            pop_size = self.start
            while True: 
                t_diff = exp_dst.random_list(1)[0]
            
                event = rnd.random()
                if event < self.b/float(self.b + self.d): 
                    pop_size += 1
                else: 
                    pop_size -= 1 
                if pop_size == 0 : 
                    ext += 1
                    break 
                if pop_size >= threshold: 
                    break
                if pop_size < 0: 
                    print(self.b,self.d,pop_size)
                    raise ValueError('r')
#                print(self.d,pop_size)
        return ext/float(samples)
    
    
if __name__ == "__main__": 
#    b = 3
#    d = 2
#    dt = 0.0001
#    """ Discrete simulation of birth-death  """ 
#    plt.figure()
#    bd = birth_death(100,b,d) 
#    reps = 100 
#    for rep in range(reps): 
##        print(rep)
#        path = bd.path(100,dt) 
#        plt.plot(path[0], path[1])
##    plt.ylim([0,1])
#    plt.show()
#    plt.title('b = ' + str(b) + ', d = ' + str(d) + ', dt = ' + str(dt) )
#    plt.xlabel('Time')
#    plt.ylabel('Population Size')
#    
#    """ Distribution of waiting times """
#    plt.figure()
#    bd = birth_death(100,b,d) 
#    path = bd.path(1000)
#    times = path[0]
#    waiting_times = [ times[i+1] - times[i] for i in range(len(times)-1) ]
#    waiting_dst = dst.create_dist(waiting_times)
#    waiting_dst.cdf_plot('Waiting Time Cummulative Distribution', 'Waiting time',plt)
#    expected_dst = dst.exponential(b+d)
#    plt.plot(arange(0,max(waiting_times),0.001),[expected_dst.cdf(x) for x in arange(0,max(waiting_times),0.001)],label = 'Expected distribtuion', linestyle = '--', color = 'red')
#    plt.legend()
#    plt.axvline(x = dst.mean(waiting_times), color = 'blue' )
#    plt.axvline(x = 1/float(b+d), color = 'red', linestyle = '--' )
#    plt.title('Waiting Time CDF' + '\n b = ' + str(b) + ', d = ' + str(d) + ', dt = ' + str(dt) )
#    plt.show()
#    
#    
#    """ Effect of dt"""
#    dt_list = [ 0.3,0.1,0.01,0.001 ]
#    b = 1
#    d = 1
#    total_time = 1000
#    fig,ax = plt.subplots(1,len(dt_list),sharex = True)
#    bd = birth_death(100,b,d) 
#    for i in range(len(dt_list)): 
#        dt = dt_list[i]
#        path = bd.path(total_time,dt)
#        times = path[0]
#        
##        plt.subplot(1,3,i+1)
##            plt = ax[i,j]
#        waiting_times = [ times[j+1] - times[j] for j in range(len(times)-1) ]
#        waiting_dst = dst.create_dist(waiting_times)
#        waiting_dst.cdf_plot('Waiting Time Cummulative Distribution', 'Waiting time',ax[i])
#        
#        expected_dst = dst.exponential(b+d)
#        ax[i].plot(arange(0,max(waiting_times),0.001),[expected_dst.cdf(x) for x in arange(0,max(waiting_times),0.001)],label = 'Expected distribtuion', linestyle = '--', color = 'red')
#        ax[i].legend()
#        ax[i].axvline(x = dst.mean(waiting_times), color = 'blue' )
#        ax[i].axvline(x = 1/float(b+d), color = 'red', linestyle = '--' )
#        ax[i].set_title('dt = ' + str(dt))
#    fig.suptitle('Effect of dt' + '\n' + 'b = ' + str(b) + ', d = ' + str(d) + ' time =' + str(total_time))
##        ax[i].set_xlim([0,5])
#    """ Effect of b+d """
##    plt.figure()
##    dt_list = [ 0.1,0.01,0.001 ]
#    b = 0.4
#    d_list = [0.1,0.4,0.7]
#    reps = 100 
#    fig,ax = plt.subplots(2,len(d_list), sharex= 'row', sharey= 'row')
#    for i in range(len(d_list)):
#        d = d_list[i]
#        bd = birth_death(100,b,d)
#        
#        waiting_times = []
#        for rep in range(reps): 
#    #        print(rep)
#            path = bd.path(100) 
#            ax[0][i].plot(path[0], path[1])
#            times = path[0]
#            waiting_times += [ times[j+1] - times[j] for j in range(len(times)-1) ]
#        
#        waiting_dst = dst.create_dist(waiting_times)
#        waiting_dst.cdf_plot('Waiting Time Cummulative Distribution', 'Waiting time',ax[1][i])
#        ax[1][i].axvline(x = dst.mean(waiting_times), color = 'blue' )
#        ax[0][i].set_title('b = ' + str(b) + ', d =' + str(d))
#        ax[0][i].set_ylabel('Population Size')
#        ax[1][i].set_ylabel('Cummulative probability')
#        
    """ Extinction probabilities """
    b_list = [1,5]
    d_list = arange(0,6,0.1)
    fig, ax = plt.subplots(1,1)
    for b in b_list:
        ext_list = []
        for d in d_list: 
            print(d)
            bd = birth_death(1, b, d)
            ext_list += [ bd.ext_prob(10000,100) ]
        ax.plot(d_list,ext_list, label = 'b=' + str(b))
     
    
    
    
    
    
    
    
    
    
    