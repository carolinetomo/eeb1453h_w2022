import distributions
import sys
import matplotlib.pyplot as plt
import math 

class brownian:
    def __init__(self,start,rate):
        self.start = start
        self.rate = rate #rate is the standard deviation of the jump. Each jump is normally distributed with some sd rate. 
    
    def run(self,ngen=100):
        res = [self.start] #res is our list of locations 
        cur_pos = self.start
        k = distributions.normal(0.0,self.rate)
        for gen in range(ngen):
            jump = k.random_ls(1)[0]
            cur_pos = cur_pos + jump
            res.append(cur_pos)
        return res
#To make this model into continuous time, or approximate continuous time, we essentially just need to take progressively smaller time increments, s.t. dt~=0
    def run_continuous(self, ngen=100):
        res = [self.start] #res is our list of locations. We initialize it with a starting position of self.start
        cur_pos = self.start #our current position also begins at self.start
        t = 0 #Initializing a time parameter t
        dt = 0.001 #initializing a time-jump parameter dt as the time difference between getting values. In discrete time, this was implicilty 1 
        k = distributions.normal(0.0,self.rate*math.sqrt(dt)) #Using property of Brownian motion that each jump is normally dist with mean =0 and var = theta^2, here theta = dt. So sd = sqrt dt
        t_list = [t] #initializing a list of time values t_list beginning with t=0
        while t<= ngen: #while time is within ngen 
            jump = k.random_ls(1)[0] #same as before, draw a random jump with mean 0, sd=1
            cur_pos = cur_pos + jump #as before
            res.append(cur_pos) #As before
            t=t+dt #While t is less than ngen itll keep running and each unit of time = 0.001 (or whatever I sepecified as my t value). Increasing time by dt each time we go through the loop
            t_list.append(t) #adding this new time to our list of times
        return [res,t_list] #returning both our list of locations and our list of times
    

for i in range(100): #Running regular brownian motion
    b = brownian(0,1.0)
    path = b.run(10)
    plt.plot(range(len(path)),path)
plt.show()

for i in range(100): #running continuous brownian motion
    b = brownian(0,1.0)
    path = b.run_continuous(10) #using b.run_continous method instead
    plt.plot(path[1],path[0]) #indexing our list we returned from this metho to plot our times on the x and our values on the y
plt.show()
#print(path)

#ornstein uhlenbach distribtution.

#This is like an exercise band or anxious-avoidant trap. The further you pull away the stronger it pull you back in. This is because the pull is scaled by the distance jumped 
#In this case, we've added some term theta which pulls a path back towards the center, 0, after each jump.
class orn_uhl: #initialized a new class of distribution which is the same as our class Brownian, except it has an additional theta parameter
    def __init__(self,start,rate,theta):
        self.start= start
        self.rate = rate 
        self.theta = theta

    def run(self,ngen=100):
        res = [self.start]
        cur_pos = self.start
        k = distributions.normal(0.0,self.rate)
        for gen in range(ngen):
            jump = (-self.theta * cur_pos)+ k.random_ls(1)[0] #updated to make jump depend on current position and parameter theta. 
            cur_pos = cur_pos +jump 
            res.append(cur_pos)
        return res

for i in range(100):
    ou = orn_uhl(0,2.0,1.0)
    path = ou.run(1000)
    plt.plot(range(len(path)),path)
plt.show()



#Every time we move (jump) the jump value originates from a normal distribution with mean= 0 and sd=rate. S.t. our expected jump is 0. 

#Every time we run a brownian motion we are getting one path. 


#Producing a continunous time normal distribtution for Brownian motion. 
#To do  this we will initialize a normal distribution with mean = 0 and stdev = self.rate*math.sqrt(t)

