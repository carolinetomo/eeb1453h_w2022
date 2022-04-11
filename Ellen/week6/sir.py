import distributions as d #import distributions module we created
#from random import choices #import function choices from random --> this function will randomly selected an entry from a provided list of potential entries weighted by provided probabilities
import random as random
import matplotlib.pyplot as plt #import module for plotting
import sys #import sys

class sir: #create a class for the SIR process (susceptability, infection, recovery)
    def __init__(self,s,i,r,m,b,g): # lots of parameters to input into this function
        self.s = s  # susceptible pop (how many people are susceptible in the population)
        self.i = i  # infected pop (how many people are infected in the population)
        self.r = r  # recovered pop (how many people are recovered in the population)
        self.m = m  # host death rate (rate of people going from infected to death = mortality or just your regular old death rate?) #this also seems to be going into the model as the birth rate
        self.b = b  # infection rate (rate of people going from susceptible to infected)
        #self.v = v  # death rate from infections
        self.g = g  # recovery rate (rate of people going from inflected to recovered)


    def run(self,nstep=100): # define a function to run, one parameter = number of steps, default is 100
        n = self.s + self.i + self.r #population size is number of susceptible people, infected people and recovered people
        t = 0.0 #Initialize time at zero
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]} #set up res dictionary, associated parameters with a string of numbers (ie tracking variable through time--> doing so for time, susceptible population, infected population and recovered population
        wait_times = d.exponential(1.0) #waiting time between the events (ie between the rates of change is an exponential distribution with the rate 1. The probability of an event happening is 100% so 1/prob_event = 1
        while len(res["t"]) < nstep: #setting up infinite loop, will run while the length of the string t is the dictionary res is less than the number of time steps indicated as a parameter in the run function

            #events = {"birth" : self.m * n, "infect" : ( self.b * (self.s + self.i ) ) / n, "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            # birth: probability of death/birth times number of people (shouldn't it be an addition as each person has a change to give birth, we don't the probability of everyone giving birth? Also take into account females?
            #infect: the probability of infection times the probability of being susceptible or infected (shouldn't it be recovered) divided by the population size (not sure why divided here)
            #recov: the probability of infection multiplied by probabilty of recovery
            #probability of susceptible death is susceptible population times probability of death
            #probability of infected death
            #probability of recovered death
            #events = {"birth" : self.m * n, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}

            events = {"birth" : self.m * self.i, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i}
            #events is a dictionary containing the probabilities of each event happening, four events
            #birth is the host birth rate multipled by the infected population (why infected population)
            #infection is the probability of infection multiplied by the the number of susceptible people multiplied by the number of infected people, not sure why infected people added, maybe to model susceptible encounter with infected
            #recovery is th number of infected people multipled by the recovery rate
            #death of infected people is the death rate multiplied by the number of infected people

            
            event_rate = sum(events.values()) #rate of event is the sum of all the event probabilities
            if event_rate == 0 or self.i == 0 and self.s == 0: #if event rate is zero (event does not occur) or the number of infected people is zero and the number of susceptible people is zero
                print("time to extinction: ", t) #print time to extinction and time (extinction of virus)
                break #stop loop
            wait_times.rate = 1.0 / event_rate #the rate of the wait.times exponential distribution is 1/ the event rate/probability indicated above

            probs = [i / sum(events.values()) for i in events.values()] #list of probabilities of each event = event value of one event over the total event value 
            event = random.choices(population = list(events.keys()), weights = probs, k = 1)[0] # choose one of the events from the events dictionary keys with probabilties indicated by probs string, choose only one and return that value 
            if event == "birth": #if it is a birth
                self.s += 1 #add person to susceptible population
            elif event == "infect": #if it is an infection
                self.s -= 1 #take away person from suscetible population
                self.i += 1 #add a person to infected population
            elif event == "recov": #if it is a recovery
                self.i -= 1 #take away a person from the infected population
                self.r += 1 #add a person to the recovery population
            #elif event == "sdeath":
            #    self.s -= 1
            elif event == "ideath": #if it is an infected death
                self.i -= 1 #take away a person from the infected population
            #elif event == "rdeath":
            #    self.r -= 1

            wait = wait_times.random_vec(1)[0] #pick a random wait time between an event
            t += wait #add the wait time to the time

            res["t"].append(t) #add this value of time to the res dictionary
            res["s"].append(self.s) #add this value of susceptibile population to the res dictionary
            res["i"].append(self.i) #add this value of infected population to the res dictionary
            res["r"].append(self.r) #add this value of recovered population to the res dictionary

        return res #return the res dictionary



if __name__ == "__main__":
    s =10000
    i = 1
    r = 0
    m = 0.02
    b = 0.5
    g = 0.2
    nstep = 10000
    print(nstep)
    sim = sir(s,i,r,m,b,g)
    res = sim.run(nstep

    
    #plt.plot(res["t"],res["s"],label="s") #plot susceptible population over time 
    #plt.plot(res["t"],res["i"],label="i") #plot infected population over time
    #plt.plot(res["t"],res["r"],label="r") #plot recovered population over time
    #plt.legent(loc="upper left") #put legend in the top left
    #plt.show() #show everything
