import distributions as d
from random import choices
import matplotlib.pyplot as plt
import sys

class sir:
    def __init__(self,s,i,r,m,b,g):
        self.s = s  # susceptible pop
        self.i = i  # infected pop
        self.r = r  # recovered pop
        self.m = m  # host death rate
        self.b = b  # infection rate
        #self.v = v  # death rate from infections
        self.g = g  # recovery rate


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


if len(sys.argv) != 2:
    print("usage: "+sys.argv[0]+" <r0>")
    sys.exit()

r0 = float(sys.argv[1])

m = 0.02 #death rate
#v = 0.0007 # virulence 
g = 0.2 #recovery rate

s = 10000
i = 1
r = 0

v = (r0-g-m)/(s+i+r) # virulence

#r0 = (v * (s+i+r)) + m + g
print("r0:",r0)

sim = sir(s,i,r,m,v,g)
res = sim.run(50000)


#print(res["t"])
plt.plot(res["t"],res["s"],label="s")
plt.plot(res["t"],res["i"],label="i")
plt.plot(res["t"],res["r"],label="r")
plt.legend(loc="upper left")
plt.show()
