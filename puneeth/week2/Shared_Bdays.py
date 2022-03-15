#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 02:16:32 2022

@author: puneeth
"""
import random as rnd
import matplotlib.pyplot as plt

#def sum_bool(a): 
#    total = 0
#    if type(a) != type([]):
#        raise TypeError("The argument should be " + str(type([])) + ", got " + str(type(a)) )
#    for ind in range(len(a)): 
#        if type(a[ind]) != type(True):
#            raise TypeError("The " + str(ind) + " entry of the list should be "  + str(type(True)) + " but is " + str(type(a[ind])) )
#        if a[ind]: 
#            total += 1 
#    return total


def sum_list(a): 
    total = 0 
    if type(a) != type([]) and type(a) != type(range(2)):
        raise TypeError("The argument should be " + str(type([])) + ", got " + str(type(a)) )
    for val in a: 
        total += val 
    return total

def weighted_choice(val_list, weights): 
    cummulative_weights = [0] + [ sum_list(weights[:n])/sum_list(weights) for n in range(1,len(val_list)+1) ]
#    print(cummulative_weights)
    rnd_val = rnd.random()
#    print(rnd_val)
    ind = 0
    while rnd_val > cummulative_weights[ind]:
        ind += 1 
    return val_list[ind-1]

def pick_bday(leap_year,monthly_dist):
    if leap_year and rnd.random() < 0.25: 
        len_months = [31,29,31,30,31,30,31,31,30,31,30,31]
        weight_months = [ len_months[mnth]*monthly_dist[mnth] for mnth in range(12) ] 
        month = weighted_choice(range(12),weight_months)
        bday = sum_list( [0] + len_months[:month] ) + rnd.choice(range(len_months[month]) ) +1
#        bday = rnd.choice(range(366))
    else:
        len_months = [31,28,31,30,31,30,31,31,30,31,30,31]
        weight_months = [ len_months[mnth]*monthly_dist[mnth] for mnth in range(12) ] 
        month = weighted_choice(range(12),weight_months)
        bday = sum_list( [0] + len_months[:month] ) + rnd.choice(range(len_months[month])) +1
#        bday = rnd.choice(range(365))
    return bday

def share_bday(n,leap_year,twins_prob,monthly_dist): 
    shared_bday = False
    bdays = [pick_bday(leap_year,monthly_dist) for ind in range(n)]
    for ind1_index in range(n-1):
        for ind2_index in range(ind1_index+1,n):            
            if rnd.random() < twins_prob: 
                shared_bday = True
                break
            else: 
                if bdays[ind1_index] == bdays[ind2_index]: 
                    shared_bday = True
                    break
        if shared_bday:
            break
    return shared_bday 

def prob_shared_bday(n,N,leap_year=False,twins_prob=0,monthly_dist = [1 for mnth in range(12)]):
    print(n)
    reps = [1 if share_bday(n,leap_year,twins_prob,monthly_dist) else 0 for rep in range(N)]
    return sum_list(reps)/float(N)

def find_n(val, prob): 
    for ind in range(len(val)):
        if val[ind] >= prob: 
            return ind
    else: 
        return 'The value is never reached'
    
    
N = 5000
x_val = range(2,25)
y_val = [ prob_shared_bday(n,N) for n in x_val ]
plt.scatter(x_val,y_val,label = 'No leaps, No twins, Uniform Dist', color = 'red')
plt.axvline(x=x_val[find_n(y_val,0.5)], linestyle='--', color = 'red')

y_val = [ prob_shared_bday(n,N,leap_year=True) for n in x_val ]
plt.scatter(x_val,y_val,label = 'Only leaps', color = 'blue')
plt.axvline(x=x_val[find_n(y_val,0.5)], linestyle='--', color = 'blue')

y_val = [ prob_shared_bday(n,N,twins_prob=0.01) for n in x_val ]
plt.scatter(x_val,y_val,label = 'Only 1% twins', color = 'green')
plt.axvline(x=x_val[find_n(y_val,0.5)], linestyle='--', color = 'green')

y_val = [ prob_shared_bday(n,N,monthly_dist = [1,1,1,1,1,1,1,1,1,1,3,1]) for n in x_val ]
plt.scatter(x_val,y_val,label = 'Only skewed distribution - Nov 3 times', color = 'black')
plt.axvline(x=x_val[find_n(y_val,0.5)], linestyle='--', color = 'black')

plt.xlabel('Sample size')
plt.ylabel('Prob of shared bday')
plt.title('Minimum sample size to have a 20% prob of having shared bday pair')
plt.legend()



