import distributions as d
from random import random
import matplotlib.pyplot as plt
import sys
import numpy as np

class bd:
    def __init__ (self, b, d, pop_size):
        self.b = b
        self.d = d
        self.pop_size = pop_size

    def run(self, n, window = 100.0):
        dt = window / 1000.0 # change in time
        prob_b = self.b * dt
        prob_d = self.d * dt
        self.n = n

        popsize = n

        t = 0.0
        res = []

        # time between successes
        sincelast = 0.0

        # loop: did something happen (birth or death?)? was it a birth or was it a death? create new pop size accordingly

        while True:
            if t >= window:
                break

            r = random()

            if r <= prob_b:
                popsize += 1
                sincelast = 0.0
            elif r <= (prob_d+prob_b) and r >= prob_b:
                popsize -= 1   
                sincelast = 0.0
            else:
                sincelast += dt                 

            '''
            if popsize <= 0:
                res.append(0)
                break
            '''

            res.append(sincelast)

            t += dt
                    
        return res


if __name__ == "__main__":
    '''
    example = bd(0.1, 0.05, 10)
    show = example.run(1000)
    print(show)
    '''

    b = 0.1
    d = 0.1
    start_pop = 10000
    window=1000.0
    nrep=1
    w = []

    sim = bd(b,d,start_pop)
    walk = sim.run(window)

    sum = 0.0
    for i in range(len(walk)):
        sum += walk[i]

    # rate = average span of time between successes (lambda)
    # if we run this several times, we see that lambda ~= 1/(b+d)
    rate = sum / len(walk)

    '''
    x=np.array([1,2,3,4,5])
    y=np.exp(x)
    plt.plot(x,y)
    plt.show()
    sys.exit()
    '''

    plt.hist(walk)
    plt.show()
    sys.exit()


    for i in range(nrep):

        plt.plot(range(len(walk)),walk)

    plt.show()

# homework: validate exponential waiting times for b-d process using graphs