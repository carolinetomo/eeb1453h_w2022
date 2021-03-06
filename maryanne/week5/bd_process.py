import distributions_1 as d
import matplotlib.pyplot as plt
from random import random
from statistics import mean
from random import random

class bd:
    def __init__(self, b, d, pop_size):
        self.b = b #birth rate
        self.d = d #death rate
        self.pop_size = pop_size #population size

    def run(self,window=100.0):
        dt = window / 10000.0 #change in time
        prob_b = self.b * dt #birth probability
        prob_d = self.d * dt #death probability
        t = 0.0
        res = []
        sincelast = 0.0
        times = []
        while True:
            if t >= window:
                break

            if self.pop_size == 0:
                res.append(0)
                t += dt
                continue

            r = random()
            if r < prob_b: #if there is a birth
                self.pop_size += 1
                times.append(sincelast)
                sincelast = 0.0
            elif prob_b < r and r < (prob_b + prob_d): #if there is a death
                self.pop_size -= 1
                times.append(sincelast)
                sincelast = 0.0
            else: #when changes stops
                sincelast += dt
            res.append(self.pop_size) #change the population size
            t += dt

        return res, times
if __name__ == "__main__":
    b = 0.2
    d = 0.2
    start_pop = 100
    window=1000.0
    nrep=10
    w = []
    for i in range(nrep):
        sim = bd(b,d,start_pop)
        walk,times = sim.run(window)
        w += times
        plt.plot(range(len(walk)),walk)
    plt.show()

    gm = 1/mean(w)

    event_rate = b+d
    print(gm,event_rate)
    plt.hist(w)
    plt.axvline(x=gm,color="red")
    plt.show()
