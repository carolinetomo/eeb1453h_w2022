import distributions
import sys
import matplotlib.pyplot as plt

class brownian:
    def __init__(self,start,rate):
        self.start = start
        self.rate = rate
    
    def run(self,ngen=100):
        res = [self.start]
        cur_pos = self.start
        k = distributions.normal(0.0,self.rate)
        for gen in range(ngen):
            jump = k.random_ls(1)[0]
            cur_pos = cur_pos + jump
            res.append(cur_pos)
        return res

for i in range(100):
    b = brownian(0,1.0)
    path = b.run(1000)
    plt.plot(range(len(path)),path)
plt.show()

print(path)
