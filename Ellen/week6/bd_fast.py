import distributions as dist #import all the distributions we created
import matplotlib.pyplot as plt #import plotting module
from random import random #import random function (grab random number from 0 to 1)


"""
def geo_mean(ls):
    prod = ls[0]
    for i in ls[1:]:
        prod=prod*i
    gm = math.sqrt(prod)
    return gm
"""

class bd: #Create birth-death class
    def __init__(self,b,d,pop_size): #three parameters must be defined in this class, birth rate, death rate and population size
        self.b = b #birth rate
        self.d = d #death rate
        self.pop_size = pop_size #population size

    def run(self,window=100.0): #Defining a function called run requiring the parameter window which is given the default 100
        event_rate = self.b + self.d #the event rate (birth and death are both events) is the sum of the birth and death rate
        p_birth = self.b / event_rate #probability of birth is the birth rate divided by the event rate
        waits = dist.exponential(1.0 / event_rate) #Waits is an object with the class exponential with the rate equal to 1/event_rate
        t = 0.0 #Initializing time at 0
        res = {} # Initializing a dictionary res
        while True: #Creating an infinite loop
            if t >= window: #If time is greater than or equal to the window
                res[t]=self.pop_size #the value that becomes associated with t in the res dictionary is the population size 
                return res #return the dictionary

            if self.pop_size <= 0 : #If the population size drops to zero
                res[t]=0.0 #the value associated with t in the dictionary will be zero
                return res #return the dictionary

            wait = waits.random_vec()[0] #the value of wait is the first value of a random vector of values taken from the exponential distribution waits
            #print(wait)
            r = random() #r is a random number between 0 and 1
            if r < p_birth: #if r is less than the birth rate
                self.pop_size += 1 #increase the populations size by one
            else: 
                self.pop_size -= 1 #decrease the populations size by one (this doesn't seem to be the death rate as its just saying that whenever a birth does not occur, a death must occur....?)
            res[t]=self.pop_size #the values associated with t is the population size
            t+=wait #add the wait time to the time 
            #print(t)


if __name__ == "__main__":
    b = 0.09 #birth rate is 0.09
    d = 0.088 #Death rate is 0.088
    start_pop = 3 #starting population is 3
    window=100.0 #time window is 100
    nrep=1 #number of simulations to run is 100
    for i in range(nrep): #for each round of the simulation
        sim = bd(b,d,start_pop) #set sim as a class bd
        walk = sim.run(window) #get a dictionary of times associated with population sizes
        #print(walk.keys())
        plt.plot(walk.keys(),walk.values()) #plot the walk keys (which is time) against the values (population size)
    plt.show() #Show the plot
