#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:27:31 2022

@author: puneeth
"""

import random as rnd 
import matplotlib.pyplot as plt
import math

def drange(start,end,step):
    output = [start]
    while output[-1] < end:
        output += [ round(output[-1] + step, 7) ]
    return output

def mean(data_list): 
    total = 0 
    for val in data_list: 
        total+=val
    return total/float(len(data_list))

def std(data_list): 
    total_dev = 0 
    data_mean = mean(data_list)
    for val in data_list: 
        total_dev += (val - data_mean)**2 
    var = total_dev/float(len(data_list))
    return math.sqrt(var)

def factorial(n):
    out =1 
    for i in range(n):
        out *= (i+1) 
    return out 

def choose(n,k):
    out = 1
    for i in range(k): 
        out *= (n-i)/(k-i)
    return out

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
    
class exponential :
    def __init__(self, rate = 1):
        self.rate = rate
    
    def mean(self):
        return 1/float(self.rate)
        
    def random_list(self, n = 1):
        out = [] 
        while len(out) < n: 
            x = rnd.random() 
            x_exp = -math.log(x)/float(self.rate)
            out += [x_exp]
#        print(out)
        return out
    
    def pdf(self, x):
        # HINT: to calculate the pdf, you will need math.e, math.pi, and math.sqrt
        density = self.rate*math.e**(-self.rate*x) # here, you will plug the value X into the PDF for a normal distribution
        return density
    def cdf(self, x):
        cummulative = 1 - math.e**(-self.rate*x)
        return cummulative
    
        
class binomial:
    def __init__(self, n,p): 
        self.trials = n
        self.prob = p 
    
    def random_list(self, rep=1):
        out = [] 
        for trial in range(rep):
            success = 0
            for ber in range(self.trials):
                outcome = rnd.random() 
                if outcome < self.prob:
                    success += 1 
            out += [ success ]
        return out 
    def pdf(self,k): 
        prob = choose(self.n,k)*(self.p**k)*(1-self.p)**(self.n-k)
        return prob
if __name__ == "__main__": 
    example = normal(1,2)
    
    

#Get list of bins from data. data = [ data points ], bins = number of bins we want, output = [ [cut_0,cut_1],[cut_1,cut_2],..,[cut_bins-1,cut_bins] ]
def make_cuts(data,bins): 
    biggest = max(data)
    smallest = min(data) 
    span = biggest - smallest
    size_of_one = span/bins 
    cuts = [ smallest + size_of_one*i for i in range(bins+1) ] 
    return { i:[cuts[i],cuts[i+1]] for i in range(len(cuts) - 1) }


class create_dist():
    def __init__(self,data): 
        data.sort()
        self.data = data 
        self.upper = max(data)
        self.lower = min(data)
        #Deciding how many bins we want 
        max_diff = max([data[i] - data[i-1] for i in range(1,len(data))]) #minimum difference between two consecutive values
        min_diff = min([data[i] - data[i-1] for i in range(1,len(data))]) #maximum difference between two consecutive values
        bin_size = min_diff + (max_diff - min_diff)*0.010 #size of one bin = 10% of difference range 
        bins_num = int( (self.upper - self.lower)/float(bin_size) ) #number of bins from range and bin size
        self.bins = make_cuts(self.data,bins_num) #Get the bins from the data
        self.prob = { i:0 for i in self.bins } #probability distribution 
        self.vals = { i:[] for i in self.bins } #set of values which fall in each bin 
        
        #compute the prob of data falling in each bin
        for val in self.data: 
            for key in self.bins: 
                bin_vals = self.bins[key]
                if val >= bin_vals[0] and val <= bin_vals[1]: 
                    self.prob[key] += 1 
                    self.vals[key] += [val] 
                    break        
#        print(min(self.data),max(self.data),self.bins)
#        print(len(self.data),sum(self.prob.values()))
        self.prob = {key:self.prob[key]/len(self.data) for key in self.prob } #converting frequency into probability
    
    def dist_plot(self,plot_lab,xlab,ax): 
        ax.plot([ (bin_val[0]+bin_val[1])*0.5 for bin_val in self.bins.values() ], self.prob.values(), label = plot_lab)
        if ax == plt: 
            ax.xlabel(xlab)
            ax.ylabel("Probability")
            ax.title("Probability Distribution")
        else:
            ax.set_xlabel(xlab)
            ax.set_ylabel("Probability")
            ax.set_title("Probability Distribution")
        ax.legend()        
    
    def cdf_plot(self,plot_lab,xlab,ax): 
        Cumm_prob = []
        for key in self.bins:
            Cumm_prob += [ sum([ self.prob[i] for i in range(key+1) ]) ]
#        print(Cumm_prob)
#        print(sum(self.prob.values()))
        ax.plot([ (bin_val[0]+bin_val[1])*0.5 for bin_val in self.bins.values() ], Cumm_prob, label = plot_lab, color = 'blue')
        if ax == plt: 
            ax.xlabel(xlab)
            ax.ylabel("Cummulative Probability")
            ax.title("Cummulative Distribution")
        else:
            ax.set_xlabel(xlab)
            ax.set_ylabel("Cummulative Probability")
            ax.set_title("Cummulative Distribution")
        ax.legend()
        
    def prob_x(self, value):
        prob = 0
        for key in self.bins: 
            bin_val = self.bins[key]
            if value >= bin_val[0] and value <=bin_val[1]: 
                prob = self.prob[key]
                break
        return prob
        
