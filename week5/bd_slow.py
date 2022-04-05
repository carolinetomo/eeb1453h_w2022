import distributions as d
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
        waiting_times = []
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
                waiting_times.append(sincelast)
                sincelast = 0.0
            elif prob_b < r and r < (prob_b + prob_d):
                self.pop_size -= 1
                waiting_times.append(sincelast)
                sincelast = 0.0
            else:
                sincelast += dt
            res.append(self.pop_size)
            t += dt

        return res,waiting_times

if __name__ == "__main__":
    b = 0.09
    d = 0.2
    start_pop = 10
    window=1000.0
    nrep=100
    w = []
    for i in range(nrep):
        sim = bd(b,d,start_pop)
        walk,wait_times = sim.run(window)
        w += wait_times
        plt.plot(range(len(walk)),walk)
    plt.show()

    gm = 1/mean(w)

    event_rate = b+d
    print(gm,event_rate)
    plt.hist(w)
    plt.axvline(x=gm,color="red")
    plt.show()
