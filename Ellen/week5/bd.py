import distributions as dist
import matplotlib.pyplot as plt
from random import random


class bd: ## create a class birth-death
    def __init__(self,b,d,pop_size): #three parameters to indicate the birth-death distribution
        self.b = b #birth rate
        self.d = d #death rate
        self.pop_size = pop_size #populations size 

    def run(self,window=100.0): #defining the function to run in this class, default window size is 100
        dt = window / 10000.0 #the change in time is the window size divided by 10000 --> ie a very small number getting towards the instantaneous birth rate?
        prob_b = self.b * dt #coverting birth rate to a probability: birth rate = birth/time, by multiplying by time, time cancels out and we get get probability
        prob_d = self.d * dt #coverting death rate to a probability: death rate = death/time, by multiplying by time, time cancels out and we get get probability
        t = 0.0 #Initialize time, it starts at 0.0 seconds
        res = [] #initialize res list, currently nothing in this, but we will add to it, keeping track of population size

        sincelast = 0.0 #initialize "sincelast" variable, starts at 0.0
        while True: #starting infinite loop
            if t >= window: #if time reaches the indicated window value, ie the time interval, stop the loop
                break #stop the loop

            if self.pop_size == 0: # if the populations size drops to zero, (ie pop_size = zero)
                res.append(0) #add zero to the list res (population size) 
                t+=dt #add the change in time to the variable time, change the value of time to the next interval
                continue # Continue in the loop

            r = random() #Draw a randome number between zero and 1
            if r < prob_b: #if the value of r is less than the value of birth probability, a birth event will occur
                self.pop_size += 1 #add one to the population size
            elif prob_b < r and r < (prob_b + prob_d): #If the value of r is less than the sum of the probability of birth and death, but greater than the probability of birth, a death event occurs
                self.pop_size -= 1 # take one away from the population size
            res.append(self.pop_size) #add new population size value to the list res
            t += dt #add change in time to the variable

        return res #this function should return the list res which is the changing values of the population size
    
    ##Idea create a function that pulls out the length of time where population does not change as a vector, plot to see if exponential shape

    def run_t(self,window=100.0): 
        dt = window / 10000.0 
        prob_b = self.b * dt 
        prob_d = self.d * dt 
        t = 0.0 
        res = [] 
        inter = []
        interval = 0.0
        sincelast = 0.0 
        while True: 
            if t >= window: 
                break 

            if self.pop_size == 0: 
                res.append(0)  
                t+=dt 
                continue 

            r = random() 
            if r < prob_b: 
                self.pop_size += 1
                #print(interval)
                if interval != 0:
                    inter.append(float(interval))
                interval = 0.0
            if prob_b < r and r < (prob_b + prob_d): 
                self.pop_size -= 1
                #print(interval)
                if interval != 0:
                    inter.append(float(interval))
                interval = 0.0
            elif r > (prob_b + prob_d):
                self.pop_size += 0
                interval += dt
                
            res.append(self.pop_size) 
            t += dt
            
            
        return res, inter #this function should return the list res which is the changing values of the population size
    
    


if __name__ == "__main__": ##main function to run 
    b = 0.09 #birth rate is 0.09 per time interval
    d = 0.1 # death rate is 0.2 per time interval
    start_pop = 1000 #starting population is 10 individuals
    window=1000.0 #window of time to measure/ max time
    nrep=100 #number of repitions to run the simulation
    w = [] #Initializing a list w, not sure where this is coming in?
    rate = (1/(b+d))
    x = dist.exponential((1/(b+d)))
    for i in range(nrep): #running loop to simulate birth-death 100 times
        sim = bd(b,d,start_pop) #indicate what the birth death class that we are looking at contains
        walk, intervals = sim.run_t(window) # run the birth-death simulation to create a list of of population sizes over time interval
        #print(walk)
        s_intervals = sorted(intervals)
        length = range(len(s_intervals))
        #print(s_intervals)
        #x_vec = x.random_vec(len(s_intervals))
        x_vec = x.random_vec(100)
        s_x_vec = sorted(x_vec)
        #plt.plot(range(len(walk)),walk) #plot the vaues of the populations size list against the length of the vector (ie over time)
        plt.plot(length, s_intervals)
        #plt.plot(length, s_x_vec)
        #plt.plot(range(100), s_x_vec)
    plt.show() #show the plot of all the birth-death simulations





    #rate = (1/(b+d))
    #print(rate)
    #x = dist.exponential((1/((b*dt)+(d*dt))))
    #x = dist.exponential((1/(b+d)))
    #print(x)
    #x_vec = x.random_vec(len(s_intervals))
    #x_vec = x.random_vec(100)
    #s_x_vec = sorted(x_vec)
    #print(walk)
    #print(x_vec)
    #print(s_intervals)
    #plt.plot(length, s_intervals, label = "time_intervals")
    #plt.legend()
    #plt.show()
    #plt.plot(length, s_x_vec, label = "exponential")
    #plt.plot(range(100), s_x_vec, label = "exponential")
    #plt.legend()
    #plt.show()





    #print(intervals)
    #print(walk)
    #s_intervals = sorted(intervals)
    #print(s_intervals)
    #length = range(len(s_intervals))
    #print(length)
    #plt.plot(length, s_intervals)
    #plt.show()
    #plt.plot(length, intervals)
    #plt.show()
    
