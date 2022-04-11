import distributions as dist
import random
import matplotlib.pyplot as plt

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
        wait_times = dist.exponential(1.0) #waiting time between the events (ie between the rates of change is an exponential distribution with the rate 1. The probability of an event happening is 100% so 1/prob_event = 1
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

    def run_pop(self,nstep=100):
        n = self.s + self.i + self.r
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r], "n": [n]}
        wait_times = dist.exponential(1.0)
        while len(res["t"]) < nstep:

            events = {"birth" : self.m * self.i, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i}
            event_rate = sum(events.values())
            
            if event_rate == 0 or self.i == 0 and self.s == 0:
                print("time to virus extinction: ", t)
                break
            if n == 0:
                print("Apocalypse! Everybody dies!", t)
                break
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = random.choices(population = list(events.keys()), weights = probs, k = 1)[0]
            if event == "birth":
                self.s += 1
            elif event == "infect":
                self.s -= 1
                self.i += 1
            elif event == "recov":
                self.i -= 1
                self.r += 1
            #elif event == "sdeath":
            #    self.s -= 1
            elif event == "ideath":
                self.i -= 1
            #elif event == "rdeath":
            #    self.r -= 1

            wait = wait_times.random_vec(1)[0]
            t += wait
            n = self.s + self.i + self.r

            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)
            res["n"].append(n)

        return res
    
#Adding in separate birth rate, individual natural death for each of s,i,r groups, infection death for infected group
class sir_expand: #create a class for the SIR process (susceptability, infection, recovery)
    def __init__(self,s,i,r,b,v,u,g,d): # lots of parameters to input into this function
        self.s = s  # susceptible pop (how many people are susceptible in the population)
        self.i = i  # infected pop (how many people are infected in the population)
        self.r = r  # recovered pop (how many people are recovered in the population)
        self.b = b  # birth rate (how many individuals are added to the susceptible population
        self.v = v  # infection rate (how many individuals are transitioning from susceptible to infected
        self.u = u  # death via infection (how many infected people are dying because of the disease
        self.g = g  # recovery rate (how many people are recovering from the disease, transition from infected to recovered)
        self.d = d  # standard death rate (how many people are dying just because

#Events to model:
        #Birth: Any individual can give birth, and the baby will not be infected --> total population size X probability of birth
        #Death by natural causes: Any individual can die of natural causes --> total population size X probaility of natural death, but needs to be broken down into groups to acount for changes in different types of populations
        #Death by infection: the number of infected people who die
        #Infection: an encounter of susceptible individual with infected individual with the rate of infection
        #Recovery: the number of infected individuals with the rate of recovery
        
    def run_expand(self,nstep=100):
        n = self.s + self.i + self.r
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r], "n": [n], "event": []}
        wait_times = dist.exponential(1.0)
        while len(res["t"]) < nstep:

            events = {"birth" : n * self.b,
                      "infect" : ( self.v * self.s * self.i ) ,
                      "recov" : self.i * self.g,
                      "infect_death" : self.u * self.i,
                      "s_nat_death": self.s * self.d,
                      "i_nat_death": self.i * self.d,
                      "r_nat_death": self.r * self.d}
            event_rate = sum(events.values())
            
            if n > 0 and self.i == 0:
                print("Virus Extinction! Humans win!: ", t)
                break
            elif n == 0:
                print("Apocalypse! Everybody dies!:", t)
                break
            
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = random.choices(population = list(events.keys()), weights = probs, k = 1)[0]
            #print(event)
            if event == "birth":
                self.s += 1
            elif event == "infect":
                self.s -= 1
                self.i += 1
            elif event == "recov":
                self.i -= 1
                self.r += 1
            elif event == "infect_death":
                self.i -= 1
            elif event == "s_nat_death":
                self.s -= 1
            elif event == "i_nat_death":
                self.i -= 1
            elif event == "r_nat_death":
                self.r -= 1

            wait = wait_times.random_vec(1)[0]
            t += wait
            n = self.s + self.i + self.r
            #print(n)
            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)
            res["n"].append(n)
            res["event"].append(event)

        return res

#Adding in transition from recovered to susceptible (loss of immunity)
class sir_expand_w: #create a class for the SIR process (susceptability, infection, recovery)
    def __init__(self,s,i,r,b,v,u,g,d,w): # lots of parameters to input into this function
        self.s = s  # susceptible pop (how many people are susceptible in the population)
        self.i = i  # infected pop (how many people are infected in the population)
        self.r = r  # recovered pop (how many people are recovered in the population)
        self.b = b  # birth rate (how many individuals are added to the susceptible population
        self.v = v  # infection rate (how many individuals are transitioning from susceptible to infected
        self.u = u  # death via infection (how many infected people are dying because of the disease
        self.g = g  # recovery rate (how many people are recovering from the disease, transition from infected to recovered)
        self.d = d  # standard death rate (how many people are dying just because
        self.w = w  #rate at which recovered individuals are converted back into suceptible individuals = loss of immunity

#Events to model:
        #Birth: Any individual can give birth, and the baby will not be infected --> total population size X probability of birth
        #Death by natural causes: Any individual can die of natural causes --> total population size X probaility of natural death, but needs to be broken down into groups to acount for changes in different types of populations
        #Death by infection: the number of infected people who die
        #Infection: an encounter of susceptible individual with infected individual with the rate of infection
        #Recovery: the number of infected individuals with the rate of recovery
        #Loss of immunity: number of recovered individuals times the rate of immunity loss 
        
    def run_expand_w(self,nstep=100):
        n = self.s + self.i + self.r
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r], "n": [n], "event": []}
        wait_times = dist.exponential(1.0)
        while len(res["t"]) < nstep:

            events = {"birth" : n * self.b,
                      "infect" : ( self.v * self.s * self.i ) ,
                      "recov" : self.i * self.g,
                      "infect_death" : self.u * self.i,
                      "s_nat_death": self.s * self.d,
                      "i_nat_death": self.i * self.d,
                      "r_nat_death": self.r * self.d,
                      "immunity_loss": self.r * self.w}
            event_rate = sum(events.values())
            
            if n > 0 and self.i == 0:
                print("Virus Extinction! Humans win!: ", t)
                break
            elif n == 0:
                print("Apocalypse! Everybody dies!:", t)
                break
            
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = random.choices(population = list(events.keys()), weights = probs, k = 1)[0]
            #print(event)
            if event == "birth":
                self.s += 1
            elif event == "infect":
                self.s -= 1
                self.i += 1
            elif event == "recov":
                self.i -= 1
                self.r += 1
            elif event == "infect_death":
                self.i -= 1
            elif event == "s_nat_death":
                self.s -= 1
            elif event == "i_nat_death":
                self.i -= 1
            elif event == "r_nat_death":
                self.r -= 1
            elif event == "immunity_loss":
                self.r -= 1
                self.s += 1

            wait = wait_times.random_vec(1)[0]
            t += wait
            n = self.s + self.i + self.r
            #print(n)
            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)
            res["n"].append(n)
            res["event"].append(event)

        return res

#Adding in evolution of hertiable super immunity where you and your children cannot get the disease
class sir_expand_w_super: #create a class for the SIR process (susceptability, infection, recovery)
    def __init__(self,s,i,r,b,v,u,g,d,w,sup,sup_b,g_sup): # lots of parameters to input into this function
        self.s = s  # susceptible pop (how many people are susceptible in the population)
        self.i = i  # infected pop (how many people are infected in the population)
        self.r = r  # recovered pop (how many people are recovered in the population)
        self.b = b  # birth rate (how many individuals are added to the susceptible population
        self.v = v  # infection rate (how many individuals are transitioning from susceptible to infected
        self.u = u  # death via infection (how many infected people are dying because of the disease
        self.g = g  # recovery rate (how many people are recovering from the disease, transition from infected to recovered)
        self.d = d  # standard death rate (how many people are dying just because
        self.w = w  #rate at which recovered individuals are converted back into suceptible individuals = loss of immunity
        self.sup = sup #population that has permanent immunity that is heritable
        self.sup_b = sup_b #birth rate of super immunity individuals to make immune children
        self.g_sup = g_sup # recovery rate that produces permanently immune people

#Events to model:
        #Birth: Any individual can give birth, and the baby will not be infected --> total population size X probability of birth
        #Death by natural causes: Any individual can die of natural causes --> total population size X probaility of natural death, but needs to be broken down into groups to acount for changes in different types of populations
        #Death by infection: the number of infected people who die
        #Infection: an encounter of susceptible individual with infected individual with the rate of infection
        #Recovery: the number of infected individuals with the rate of recovery
        #Loss of immunity: number of recovered individuals times the rate of immunity loss
        #Super recovery: the number of infected people times the rate of super recovery for permanent immunity
        #Super_birth: the birth of immune children from permanently immune parent
        
    def run_expand_w_super(self,nstep=100):
        n = self.s + self.i + self.r + self.sup
        t = 0.0
        res = {"t":[t], "s":[self.s], "i":[self.i], "r":[self.r], "super":[self.sup], "n":[n], "event":[]}
        wait_times = dist.exponential(1.0)
        while len(res["t"]) < nstep:

            events = {"birth" : n * self.b,
                      "infect" : (self.v * self.s * self.i),
                      "recov" : self.i * self.g,
                      "infect_death" : self.u * self.i,
                      "s_nat_death": self.s * self.d,
                      "i_nat_death": self.i * self.d,
                      "r_nat_death": self.r * self.d,
                      "super_nat_death": self.sup * self.d,
                      "immunity_loss": self.r * self.w,
                      "super_recov": self.i * self.g_sup,
                      "super_birth": self.sup * self.sup_b}
            event_rate = sum(events.values())
            
            if n > 0 and self.i == 0 and (self.sup/n) < 0.9:
                print("Virus Extinction! Humans win!: ", t)
                break
            elif n == 0:
                print("Apocalypse! Everybody dies!:", t)
                break
            elif n > 0 and self.i == 0 and (self.sup/n) > 0.9:
                print("Superhumans take over! All hail evolution!:", t)
                break
            
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = random.choices(population = list(events.keys()), weights = probs, k = 1)[0]
            #print(event)
            if event == "birth":
                self.s += 1
            elif event == "infect":
                self.s -= 1
                self.i += 1
            elif event == "recov":
                self.i -= 1
                self.r += 1
            elif event == "infect_death":
                self.i -= 1
            elif event == "s_nat_death":
                self.s -= 1
            elif event == "i_nat_death":
                self.i -= 1
            elif event == "r_nat_death":
                self.r -= 1
            elif event == "super_nat_death":
                self.sup -= 1
            elif event == "immunity_loss":
                self.r -= 1
                self.s += 1
            elif event == "super_recov":
                self.i -= 1
                self.sup += 1
            elif event == "super_birth":
                self.sup += 1

            wait = wait_times.random_vec(1)[0]
            t += wait
            n = self.s + self.i + self.r + self.sup
            #print(n)
            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)
            res["n"].append(n)
            res["super"].append(self.sup)
            res["event"].append(event)

        return res



if __name__ == "__main__":
    #s = 1000
    #i = 1
    #r = 0
    #m = 0.02
    #b = 0.5
    #g = 0.2
    #nstep = 10000



    #s = 1000 #susceptible pop
    #i = 1 #infect pop
    #r = 0 # recovered pop
    #b = 0 # birth rate
    #v = 0.1 #infection rate
    #u = 0.5 # virus death rate
    #g = 0.9 # recovery rate
    #d = 0.02 #natural death rate
    #nstep = 10000

    #s = 1000 #susceptible pop
    #i = 1 #infect pop
    #r = 0 # recovered pop
    #b = 0.1 # birth rate
    #v = 0.05 #infection rate
    #u = 0.1 # virus death rate
    #g = 0.9 # recovery rate
    #d = 0.09 #natural death rate
    #w = 0.99 #Immunity loss rate
    #nstep = 100000

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.04 # birth rate
    v = 0.9 #infection rate
    u = 0.8 # virus death rate
    g = 0.15 # recovery rate
    d = 0.05 #natural death rate
    w = 0.3 #Immunity loss rate
    sup = 0 #superhuman pop
    sup_b = 0.04 #superhuman birth rate
    g_sup = 0.05 #super recovery
    nstep = 100000
    
    sim = sir_expand_w_super(s,i,r,b,v,u,g,d,w,sup,sup_b,g_sup)
    res = sim.run_expand_w_super(nstep)
    #print(res["t"])
    #print(res["n"])
    #print(res["i"])
    #print(res["event"])
    #print(res["s"])

    plt.plot(res["t"],res["s"],label="s") #plot susceptible population over time 
    plt.plot(res["t"],res["i"],label="i") #plot infected population over time
    plt.plot(res["t"],res["r"],label="r") #plot recovered population over time
    plt.plot(res["t"],res["n"],label="n") #plot total population size over time
    plt.plot(res["t"],res["super"],label="super")
    plt.legend(loc="upper left") #put legend in the top left
    plt.show() #show everything


    """
Figure one: run function
    s = 1000
    i = 1
    r = 0
    m = 0.02
    b = 0.5
    g = 0.2
    nstep = 10000

Figure two: run function
    s = 1000
    i = 1
    r = 0
    m = 0.02
    b = 0.1
    g = 0.2
    nstep = 10000

Figure three: run function
    s = 1000
    i = 1
    r = 0
    m = 0.02
    b = 0.1
    g = 0.5
    nstep = 10000

Figure four: run function
    s = 1000
    i = 1
    r = 0
    m = 0.02
    b = 0.1
    g = 0.9
    nstep = 10000

Figure five: run_pop function
    s = 1000
    i = 1
    r = 0
    m = 0.02
    b = 0.5
    g = 0.2
    nstep = 10000

Figure six: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.5 #infection rate
    u = 0.1 # virus death rate
    g = 0.5 # recovery rate
    d = 0.02 #natural death rate
    nstep = 10000

Figure seven: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.5 #infection rate
    u = 0.1 # virus death rate
    g = 0.5 # recovery rate
    d = 0.02 #natural death rate
    nstep = 1000000
    Vircus Extinction! Humans win!:  84869250.91761881

Figure eight: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.1 # birth rate
    v = 0.5 #infection rate
    u = 0.7 # virus death rate
    g = 0.1 # recovery rate
    d = 0.02 #natural death rate
    nstep = 10000

Figure nine: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.2 # birth rate
    v = 0.99 #infection rate
    u = 0.99 # virus death rate
    g = 0.0001 # recovery rate
    d = 0.02 #natural death rate
    nstep = 10000

Figure ten: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0 # birth rate
    v = 0.1 #infection rate
    u = 0.99 # virus death rate
    g = 0.01 # recovery rate
    d = 0.5 #natural death rate
    nstep = 10000

Figure eleven: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0 # birth rate
    v = 0.1 #infection rate
    u = 0.5 # virus death rate
    g = 0.9 # recovery rate
    d = 0.5 #natural death rate
    nstep = 10000

Figure 12: sir_expand, run_expand function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0 # birth rate
    v = 0.1 #infection rate
    u = 0.5 # virus death rate
    g = 0.9 # recovery rate
    d = 0.02 #natural death rate
    nstep = 10000    

Figure 13: sir_expand_w, run_expand_w function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.1 #infection rate
    u = 0.1 # virus death rate
    g = 0.9 # recovery rate
    d = 0.02 #natural death rate
    w = 0.7 #Immunity loss rate
    nstep = 100000

Figure 14: sir_expand_w, run_expand_w function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.05 #infection rate
    u = 0.1 # virus death rate
    g = 0.9 # recovery rate
    d = 0.02 #natural death rate
    w = 0.7 #Immunity loss rate
    nstep = 100000

Figure 15: sir_expand_w, run_expand_w function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.1 # birth rate
    v = 0.05 #infection rate
    u = 0.1 # virus death rate
    g = 0.9 # recovery rate
    d = 0.02 #natural death rate
    w = 0.7 #Immunity loss rate
    nstep = 100000

Figure 16: sir_expand_w, run_expand_w function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.1 # birth rate
    v = 0.05 #infection rate
    u = 0.1 # virus death rate
    g = 0.9 # recovery rate
    d = 0.09 #natural death rate
    w = 0.99 #Immunity loss rate
    nstep = 100000

Figure 17: sir_expand_w_super, run_expand_w_super function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.2 #infection rate
    u = 0.1 # virus death rate
    g = 0.89 # recovery rate
    d = 0.02 #natural death rate
    w = 0.99 #Immunity loss rate
    sup = 0
    sup_b = 0.2
    g_sup = 0.01
    nstep = 100000

Figure 18: sir_expand_w_super, run_expand_w_super function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.02 # birth rate
    v = 0.2 #infection rate
    u = 0.1 # virus death rate
    g = 0.80 # recovery rate
    d = 0.02 #natural death rate
    w = 0.99 #Immunity loss rate
    sup = 0
    sup_b = 0.04
    g_sup = 0.1
    nstep = 100000

Figure 19: sir_expand_w_super, run_expand_w_super function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.04 # birth rate
    v = 0.25 #infection rate
    u = 0.5 # virus death rate
    g = 0.4 # recovery rate
    d = 0.04 #natural death rate
    w = 0.2 #Immunity loss rate
    sup = 0 #superhuman pop
    sup_b = 0.04 #superhuman birth rate
    g_sup = 0.1 #super recovery
    nstep = 100000

Figure 20: sir_expand_w_super, run_expand_w_super function

    s = 1000 #susceptible pop
    i = 1 #infect pop
    r = 0 # recovered pop
    b = 0.04 # birth rate
    v = 0.9 #infection rate
    u = 0.9 # virus death rate
    g = 0.095 # recovery rate
    d = 0.04 #natural death rate
    w = 0.5 #Immunity loss rate
    sup = 0 #superhuman pop
    sup_b = 0.005 #superhuman birth rate
    g_sup = 0.1 #super recovery
    nstep = 100000

    """
    
