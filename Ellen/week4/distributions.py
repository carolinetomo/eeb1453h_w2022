from random import random #random() returns a random float between 0 and 1, pulling only random function from random module

import math #import math, to access functions make sure to write math. 

import sys # import sys

#implementing our own module of distributions

#Python does not have statistical info within it, you have to import it or create it
#We are going to create statistical objects for each distribution that do what we want

class normal:  #Creating a class for a normal distribution that you can specify something as
    def __init__(self, mean, sd): #you have given the class the arguments of "mean" and "sd", provide a mean and sd this values when specifying a class. You have not provided a default. Alternatively, you could write (self) and specify mean below, would not need to specify when making the object
        self.mean = mean #Tells what mean is
        self.sd = sd #Tells what sd is

    def random_ls(self, n): #create method what will take normal distribution given values and will make a list of indepedent normal values, n = number of values to generate
        norm = [] # creating the list to put the normal values in

        while True: #Start of true statement
            if len(norm) == n: #if the length of the list of normal values is equal to the n specified, stop looping through method
                break #stop
            if len(norm) > n: #If the length of the list of normal values is greater than n (because each round produces 2 values), only take the range of norm that is equal to the n value that you want
                norm = norm[0:n] #range of norm that has the number of values you wish
                break #stop
            x = random() #random numbers between 0 and 1 for x
            y = random() #random numbers between 0 and 1 for y
            xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*self.sd)+self.mean) #Take random numbers and transform into normal
            ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*self.sd)+self.mean) #Need both random numbers to get one the curve from which we get the transforme numbers
            #print(x, y, xnorm, ynorm) #Check if values match expectations
            #sys.exit() # exit program, break after one thing
            norm.append(xnorm) #add xnorm value to norm list
            norm.append(ynorm) #add ynorm value to the norm list
        #print(norm, len(norm))
        #sys.exit()
        return norm #return the norm list

    def pdf(self, x): #define the pdf function, probability of value in normal distribution
        density = 0 # here, you will plug the value X into the PDF for a normal distribution
        density = (1/(self.sd*math.sqrt(2*math.pi)))*math.e**((-1/2)*(((x-self.mean)/self.sd)**2))
        return density

if __name__ == "__main__":
    example = normal(0.0, 2.0)
    rand = example.random_ls(20)
   
    print(rand)

 #xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*1)+0)
 #ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*1)+0)
