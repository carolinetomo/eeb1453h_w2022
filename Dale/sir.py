import distributions as d
from random import choices
import matplotlib.pyplot as plt
import sys

class sir:
    def __init__(self,s,i,r,m,b,g,w,u,x,y,z):
        self.s = s  # susceptible pop
        self.i = i  # infected pop
        self.r = r  # recovered pop
        self.m = m  # host death rate from infections
        self.b = b  # infection rate
        self.g = g  # recovery rate
        #Adding a new parameter here, w, which will be the rate of return of individuals from the recovered to susceptible class. FOR PART I
        self.w = w # rate of waning immunity-- transition rate from R -> S
        #Adding a new paramater here, u, which will be the birth rate of indviduals. This is for PART II where Births and Deaths are no longer equivalent, allowing for pop growth. 
        self.u = u
        #FURTHER PART II ADDITIONS
        self.x = x #Non-viral death rate of Susceptible individuals
        self.y = y #Non-viral death rate of Infected individuals
        self.z = z #Non-viral death rate of Recovered indivduals
    def run(self,nstep=100):
        n = self.s + self.i + self.r
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]}
        wait_times = d.exponential(1.0)
        while len(res["t"]) < nstep:
            #events = {"birth" : self.m * n, "infect" : ( self.b * (self.s + self.i ) ) / n, "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #events = {"birth" : self.m * n, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            events = {"birth" : self.m * self.i, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i}

            event_rate = sum(events.values())
            if event_rate == 0 or self.i == 0 and self.s == 0:
                print("time to extinction: ", t)
                break
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = choices(population = list(events.keys()), weights = probs, k = 1)[0]
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

            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)

        return res
    def run_waning_immunity(self,nstep=100): #Making a method to run the SIR simulation with wanining immunity. Recovery term w was added to class SIR. 
        n = self.s + self.i + self.r
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]}
        wait_times = d.exponential(1.0)
        while len(res["t"]) < nstep:
            #events = {"birth" : self.m * n, "infect" : ( self.b * (self.s + self.i ) ) / n, "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #events = {"birth" : self.m * n, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #Added a new event here, immun_loss, where immunty wanes. This only happens to indv in class R and it occurs at rate w.
            events = {"birth" : self.m * self.i, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i, "immun_loss" : self.r*self.w}
 
            event_rate = sum(events.values())
            if event_rate == 0 or self.i == 0 and self.s == 0:
                print("time to extinction: ", t)
                break
            wait_times.rate = 1.0 / event_rate

            probs = [i / sum(events.values()) for i in events.values()]
            event = choices(population = list(events.keys()), weights = probs, k = 1)[0]
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
            elif event == "immun_loss": #Added what happens when immunity wanes-- an indv moves from R to S, so S+1, R-1. 
                self.r -=1
                self.s +=1

            wait = wait_times.random_vec(1)[0]
            t += wait

            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)

        return res
#Making a new method for part 2 which will allow us to have seperate birth and death rates, allowing for population growth.
#I suppose that this model still has the implicit assuption that individuals cannot be born with immunity, but this could be added, but there would be sooo much to keep track of. 
    def run_bd_separ(self,nstep=100):
            n = self.s + self.i + self.r
            t = 0.0
            res= {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]}
            wait_times = d.exponential(1.0)
#With this new model, the probabiities for birth and death will have to change
#Birth rate is somewhat tricky to change, as birthrate should logically depend on the total population size (S+I+R) however indv can only be born into S 
            while len(res["t"]) < nstep:
            #events = {"birth" : self.m * n, "infect" : ( self.b * (self.s + self.i ) ) / n, "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #events = {"birth" : self.m * n, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #Added a new event here, immun_loss, where immunty wanes. This only happens to indv in class R and it occurs at rate w.
                events = {"birth" : self.u*(self.s+self.i+self.r), "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i}
 
                event_rate = sum(events.values())
                if event_rate == 0 or self.i == 0 and self.s == 0:
                    print("time to extinction: ", t)
                    break
                wait_times.rate = 1.0 / event_rate

                probs = [i / sum(events.values()) for i in events.values()]
                event = choices(population = list(events.keys()), weights = probs, k = 1)[0]
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
            #elif event == "immun_loss": #Added what happens when immunity wanes-- an indv moves from R to S, so S+1, R-1. 
             #   self.r -=1
              #  self.s +=1

                wait = wait_times.random_vec(1)[0]
                t += wait

                res["t"].append(t)
                res["s"].append(self.s)
                res["i"].append(self.i)
                res["r"].append(self.r)

            return res


####### PART II -- NON-VIRULENCE DEATH RATE ###########
#First: our previous deathrate, m, can be repurposed as our virus death parameter. 
#Second: We must have a new event in our dictionary, events, to differentiate virally-perpetrated deaths from deaths attributable to other causes. 
#The first 2 parts seem straight-forward to implement. 
#It seems that using the approach of adding a single non-viral death parameter the difficulty lies in figuring out which stage, S I or R, actually has the indv dying.
#I'm sure this is doable, but it seems quite difficult. 
#Instead we can make a model where there are non-viral death rates for each class. This also necessitates new events in our events dictionary to indicate which class has this death occurring
#This type of model formulation should offer some utility, whereby we can account for being in one of these classes altering your probability of non-viral death-- comorbidity 

#In sum: 
#       Class SIR will recieve 3 alterations, adding 3 new parameters for non-viral death rates in each class. m will continue to only represent virally-induced death
#       events will be updated to differentiate deaths from eachother and identify their location: S_death, I_death, R_death, and now viral_death (can only occur in stage I)
#       When S_death occurs s-=1, when I_death occurs i -=1, when R_death occurs r-=1
    def run_death_all_around_us(self,nstep=100):
                n = self.s + self.i + self.r
                t = 0.0
                res= {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]}
                wait_times = d.exponential(1.0) 
                while len(res["t"]) < nstep:
            #events = {"birth" : self.m * n, "infect" : ( self.b * (self.s + self.i ) ) / n, "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #events = {"birth" : self.m * n, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "sdeath" : self.m * self.s, "ideath" : self.m * self.i, "rdeath" : self.m * self.r}
            #Added a 3 new events as described above.
                    events = {"birth" : self.u*(self.s+self.i+self.r), "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i, "sdeath" :self.s*self.x ,"ideath_nonviral":self.i*self.y  , "rdeath":self.r*self.z}
 
                    event_rate = sum(events.values())
                    if event_rate == 0 or self.i == 0 and self.s == 0:
                        print("time to extinction: ", t)
                        break
                    wait_times.rate = 1.0 / event_rate

                    probs = [i / sum(events.values()) for i in events.values()]
                    event = choices(population = list(events.keys()), weights = probs, k = 1)[0]
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
                    elif event == "sdeath":
                        self.s -= 1
                    elif event == "ideath_nonviral":
                        self.i -= 1
                    elif event == "rdeath":
                        self.r -= 1
            #elif event == "rdeath":
            #    self.r -= 1
            #elif event == "immun_loss": #Added what happens when immunity wanes-- an indv moves from R to S, so S+1, R-1. 
             #   self.r -=1
              #  self.s +=1

                    wait = wait_times.random_vec(1)[0]
                    t += wait

                    res["t"].append(t)
                    res["s"].append(self.s)
                    res["i"].append(self.i)
                    res["r"].append(self.r)

                return res





if len(sys.argv) != 2:
   print("usage: "+sys.argv[0]+" <r0>")
   sys.exit()

r0 = float(sys.argv[1])

m = 0.02 #death rate
#b =  # infection rate 
g = 0.2 #recovery rate

s = 10000
i = 1
r = 0

b = (r0-g-m)/(s+i+r) # virulence
w=0.001
u=0.01
x=0.01
y=0.05
z=0.01

#r0 = (v * (s+i+r)) + m + g
print("r0:",r0)

sim = sir(s,i,r,m,b,g,w,u,x,y,z)
res = sim.run_death_all_around_us(50000)


#print(res["t"])
plt.plot(res["t"],res["s"],label="s")
plt.plot(res["t"],res["i"],label="i")
plt.plot(res["t"],res["r"],label="r")
plt.legend(loc="upper left")
plt.show()
