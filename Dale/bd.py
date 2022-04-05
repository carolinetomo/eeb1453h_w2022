import distributions as d
import emp_methods as emp
import matplotlib.pyplot as plt
from random import random
from statistics import mean

class bd:
    def __init__(self,b,d,pop_size):
        self.b = b
        self.d = d
        self.pop_size = pop_size

    def run(self,window=100.0):
        dt = window / 10000.0
        prob_b = self.b * dt
        prob_d = self.d * dt
        t = 0.0
        res = []

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
            elif prob_b < r and r < (prob_b + prob_d):
                self.pop_size -= 1
            res.append(self.pop_size)
            t += dt

        return res

    def run_event_times(self,window=100.0):
        dt = window / 10000.0
        prob_b = self.b * dt
        prob_d = self.d * dt
        t = 0.0
        res = []
        event_time_list = []

        
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
                event_time_list.append(t) 
            elif prob_b < r and r < (prob_b + prob_d):
                self.pop_size -= 1
                event_time_list.append(t) 
            res.append(self.pop_size)
            t += dt
        return event_time_list


#if __name__ == "__main__":
   # b = 0.09
    #d = 0.2
    #start_pop = 10
    #window=1000.0
    #nrep=100
    #w = []
    #for i in range(nrep):
    #    sim = bd(b,d,start_pop)
    #    walk = sim.run(window)
    #    plt.plot(range(len(walk)),walk)
    #plt.show()




### HOMEWORK STUFF ###

#1 Time seperating events in our bd are indpendent and exponentially distributed. Prove it 

#I) Simulate bd model and output data w/ times and positions 

#First, instead of plotting we just want to return a list of our stuff 

#DOWN WITH THE MAIN, UP WITH THE ANARCHY CODE FORMATTING
#nrep=100
#for i in range(nrep):
sim_test = bd(0.09,0.2,100)
blah = sim_test.run_event_times(window=100) 
blah_dif = []
for i in range(len(blah)-1):
    intermediate_dif = blah[i+1]-blah[i]
    blah_dif.append(intermediate_dif)
plt.hist(blah_dif[0:26])
#blah_dif_emp_dist = emp.emp_dist(blah_dif)
#blah_dif_emp_dist.binfreqs()
#print(blah_dif_emp_dist.binfreqs())
#emp.emp_dist.binfreqs(blah_dif)
#plt.plot(range(len(blah_dif)),blah_dif)
#plt.show()
#27 is length of blah
    #    sim = bd(b,d,start_pop)
    #    walk = sim.run(window)
    #    plt.plot(range(len(walk)),walk)
    #plt.show()

#print(blah) #list of the consequential times. 

#Is this visually exponential ??? depends who you ask




#if __name__ == "__main__":
    #main()

    #b = 0.09
    #d = 0.2
    #start_pop = 1
    #0
    #window=1000.0
    #nrep=100
    #w = []
    #for i in range(nrep):
    #    sim = bd(b,d,start_pop)
    #    walk = sim.run(window)
    #    plt.plot(range(len(walk)),walk)
    #plt.show()


