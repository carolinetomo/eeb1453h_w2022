from random import random
import math
#from tkinter import N

class normal:
    def __init__(self, mean, sd):
        self.mean = mean
        self.sd = sd

# transform random numbers (between 0 and 1) into normal distribution according to mean and sd
    def random_ls(self, n):
        norm = []

        while True:
            if len(norm) == n:
                break
            if len(norm) > n:
                norm = norm[0:n]
                break

            x = random()
            y = random()

            xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*self.sd) + self.mean)
            ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*self.sd) + self.mean)

            norm.append(xnorm)
            norm.append(ynorm)

        return norm

class binomial:
    def __init__(self,n,p):
        self.n = n
        self.p = p

    def random_vec(self,rep=1):
        res = []
        for i in range (rep):
            success = 0
            for j in range (self.n):
                if random() <= self.p:
                    success += 1
            res.append(success)
        
        return res  

        



if __name__ == "__main__":
    example = binomial(100,0.5)
    rand = example.random_vec(10)
    print (rand)