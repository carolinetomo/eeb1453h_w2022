import distributions as dist
import matplotlib.pyplot as plt
from random import random


"""
def geo_mean(ls):
    prod = ls[0]
    for i in ls[1:]:
        prod=prod*i
    gm = math.sqrt(prod)
    return gm
"""

class bd:
    def __init__(self,b,d,pop_size):
        self.b = b
        self.d = d
        self.pop_size = pop_size

    def run(self,window=100.0):
        event_rate = self.b + self.d
        p_birth = self.b / event_rate
        waits = dist.exponential(1.0 / event_rate)
        t = 0.0
        res = {}
        while True:
            if t >= window:
                res[t]=self.pop_size
                return res

            if self.pop_size <= 0 :
                res[t]=0.0
                return res

            wait = waits.random_vec()[0]
            r = random()
            if r < p_birth:
                self.pop_size += 1
            else:
                self.pop_size -= 1
            res[t]=self.pop_size
            t+=wait



if __name__ == "__main__":
    b = 0.09
    d = 0.088
    start_pop = 3
    window=100.0
    nrep=100
    for i in range(nrep):
        sim = bd(b,d,start_pop)
        walk = sim.run(window)
        plt.plot(walk.keys(),walk.values())
    plt.show()
