import distributions
import sys
import matplotlib.pyplot as plt

#making a new class of  ornstein-uhlenbeck, and take theta * curr_pos
#discrete normal distribution change normal distribution to mean 0 and variance ttheta^2
#the time points are getting continually smaller making them "continous"
# variables I need :
# time
#theta

class o_u_p:
    def __init__(self, start, rate, theta):
        '''
        creating a new class that contains our input for mean, theta and rate
        :param start: fixed input
        :param rate: fixed input
        :param theta: fixed input
        '''
        self.start = start
        self.rate = rate
        self.theta = theta

    def run(self, ngen=100):
        '''
                the jump size will be different each time, with a constant mean, theta, and rate
                :param ngen: tell the function how many times to take steps in this case the default value is 100
                :return: the new position
                '''
        res = [self.start]  # will collect our steps but will start at the start position
        cur_pos = self.start  # the current position we start with
        k = distributions.normal(0.0, self.rate)  # how far we go
        for gen in range(ngen):
            jump = (-self.theta * cur_pos) + k.random_ls(1)[0] #new jump value with a negative theta * cur position
            cur_pos = cur_pos + jump  # taking one will give us one random normal number to see how big the jump is and pull it out of the list by indexing
            res.append(cur_pos)  # the current position now moves to the new position based on the jump
        return res
'''
bellow is the original brownian method, commenting this out
class brownian: #creating the class
   
            :param start: where the brownian motion starts
            :param rate: how fast each step is
         
    def __init__(self,start,rate):
        self.start = start # these are fixed
        self.rate = rate #fixed


    
    def run(self,ngen=100):
   
                the jump size will be different each time, with a constant mean
                :param ngen: tell the function how many times to take steps in this case the default value is 100
                :return:
            
        res = [self.start] #will collect our steps but will start at the start position
        cur_pos = self.start # the current position we start with
        k = distributions.normal(0.0,self.rate) #how far we go
        for gen in range(ngen):
            jump =k.random_ls(1)[0]
            cur_pos = cur_pos + jump #taking one will give us one random normal number to see how big the jump is and pull it out of the list by indexing
            res.append(cur_pos) # the current position now moves to the new position based on the jump
        return res
'''


for i in range(100):
    b = o_u_p(0,1.0,1.0) # mean, rate and theta inputs
    path = b.run(1000) # running the  ornstein-uhlenbeck process
    plt.plot(range(len(path)),path) #ploting our process
plt.show()

print(path)
