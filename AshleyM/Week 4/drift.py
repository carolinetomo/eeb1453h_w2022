import distributions
import sys
import matplotlib.pyplot as plt

class brownian:
    def __init__(self,start,rate):
        self.start = start
        self.rate = rate

# how many times do we want to sample from the Brownian motion? (number of generations)
    def run(self, ngen = 100):
        res = [self.start]
        cur_pos = self.start

        # how far do we go at each step?
        k = distributions.normal(0, self.rate)

        for gen in range(ngen):
            # we want 1 random normal number that will tell us how big the jump will be
            # will return a list, so we want to take the first thing from the list

            # we take out the 0 index because we want to save jump as a float
            jump = k.random_ls(1)[0]
            jump = jump * self.rate
            cur_pos = cur_pos + jump
            if cur_pos >= 1:
                cur_pos == 1
                res.append(cur_pos)
                break
            if cur_pos <= 0:
                cur_pos == 0
                res.append(cur_pos)
                break
            res.append(cur_pos)
        return res

# mutation rate per gene per generation: ~ 10e-4 to 10e-6
popsize = 100000
mutation = 0.000001 * popsize 

# trajectories are normally distributed due to CLT
for i in range (100):
    b = brownian (0.3, mutation)

    plt.suptitle('Drift by Initial Allele Frequency') 

    path = b.run(100)

    # format is (x, y)
    plt.plot(range(len(path)), path)
    plt.ylim([0,1])
    plt.xlim([0,100])
plt.show()

