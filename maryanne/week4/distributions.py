from random import random # random() returns a random float between 0 and 1
import math
import sys

class normal:
    def __init__(self,mean,sd):
        self.mean = mean
        self.sd = sd

    def random_ls(self,n):
        norm = []

        while True:
            if len(norm) == n:
                break
            if len(norm) > n:
                norm = norm[0:n]
                break
            x = random()
            y = random()
            xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*self.sd)+self.mean)
            ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*self.sd)+self.mean)
            norm.append(xnorm)
            norm.append(ynorm)
        return norm

    def pdf(self, x):
        return 

if __name__ == "__main__":
    example = normal(0.0,2.0)
    rand = example.random_ls(20)

    print(rand)
