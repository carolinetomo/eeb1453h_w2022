import distributions as d
from random import choices

"""
probs = [0.2,0.3,0.5]
event = ["thing1","thing2","thing3"]
choices(event,probs)
"""


class sir:
    def __init__(self,v,g,u,b,s,i,r):
        self.s = s  # susceptible pop
        self.i = i  # infected pop
        self.r = r  # recovered pop

        self.m = m  # host death rate
        self.b = b  # infection rate
        self.g = g  # recovery rate

    def run(self,nstep):
        t = 0.0
        res = {"t":[t],"s":[self.s],"i":[self.i],"r":[self.r]}
        wait_times = d.exponential(1.0)
        while len(res["t"]) < nstep:
            events = {"birth" : self.m * self.i, "infect" : ( self.b * self.s * self.i ) , "recov" : self.i * self.g, "ideath" : self.m * self.i}
            event_rate = sum(events.values())
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
            elif event == "ideath":
                self.i -= 1
            
            wait_times.rate = 1.0 / event_rate
            wait = wait_times.random_vec(1)[0]
            t += wait

            res["t"].append(t)
            res["s"].append(self.s)
            res["i"].append(self.i)
            res["r"].append(self.r)
        return res

if __name__ == "__main__":
    sim = sir(093929320)
