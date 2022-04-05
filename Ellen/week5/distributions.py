from random import random
import math

def mean(vals): #Mean function that inputs a list of values
    addup=0.0 #initialize total as 0.0
    for i in vals: #Looping through values in list vals
        addup += i #all each value to the total, which was initialized at 0.0
    return addup / float(len(vals)) #return mean which is calculated as the total divided by the length of the list vals which has to be set as a float number

def std(vals): #Standard deviation function that inputs list of values
    m = mean(vals) #mean of values indicated by function above
    diffsum = 0.0 #initializing standard deviation value at 0.0
    for i in vals: #looping through values in list vals
        diffsum += (i-m) ** 2.0 #calculating numerator of the standard deviation function by adding all calculations together
    s = math.sqrt( diffsum / float(len(vals)) ) #Completing the standard deviation function
    return s #return standard deviation

class uniform: ## Set the uniform distribution class, this one looks like rectangle with a low and high x threshold
    def __init__(self, lower=0.0, upper=1.0): # setting the parameters of distribution, has two, lower and higher threshold
        self.upper = upper #set upper threshold
        self.lower = lower #set lower threshold

    def random_vec(self, n=1): #defining random vector function within uniform class, number of values pulling is by default 1
        vals = [] #initializing values list
        for i in range(n): #looping through the range indicated by n
            x = random() #pull out random number between 0 and 1
            rval = lower + (x * (upper-lower)) #convert the r value to one within the lower-upper intervale
            vals.append(rval) #add value to list that we initialized
        return vals #return list of values

    def random_float(self): ##defining function that produces a random float within the interval set between lower and upper
        x = random() #pull out random number between 0 and 1 
        rval = self.lower + (x * (self.upper-self.lower)) #convert random number to one within interval
        return rval #return random number

class normal: ##defining number class distribution
    def __init__(self, mean = 0.0, sd = 1.0): ##Setting parameters of normal distribution, mean and sd, defaults are given
        self.mean = mean #set mean
        self.sd = sd #set standard deviation

    def random_vec(self, n=1, method="box_muller"): ##function to pull out vector of values from normal distribution, parameters are the number of values you wish to pull out and the method of defining the normal values
        norm=[] ## initializing the vector to put all the normal values into
        while True: # starting infinite loop
            if len(norm) == n: #If the vector length is equal to the indicated n, stop the loop
                break
            if len(norm) > n: #if the vector length is greater than the indicated n
                norm = norm[0:n] #only take the range of number indicated by n
                break

            # this is what we will use in class
            if method == "box_muller": #Here is the method used in class (called box_muller)
                x = random() #Pull out one random number between 0 and 1
                y = random() #Pull out second random number between 0 and 1
                xnorm = (((math.sqrt(-2 * math.log(x)) * math.cos(2. * math.pi * y))*self.sd)+self.mean) #Convert random number to normal number with mean and sd indicated
                ynorm = (((math.sqrt(-2 * math.log(x)) * math.sin(2. * math.pi * y))*self.sd)+self.mean) #Convert random number to normal number with mean and sd indicated

                norm.append(xnorm) #add first normal number to norm vector
                norm.append(ynorm) #add second normal number to norm vector
                #print(xnorm)
                #print(ynorm)

            # this is another approach for doing this that i am leaving because it is cool
            elif method == "polar": ##calculating normal values using the polar method which includes information from the uniform class indicated above
                unif = uniform(-1.0,1.0) # saving uniform distribution with range between -1 and 1
                while True: #creating infinite loop
                    x = unif.random_float() #grab random value from -1 to 1
                    y = unif.random_float() #grab random value from -1 to 1
                    s = (x ** 2) + (y ** 2) #s equals the sum of the squared values of these numbers
                    if s > 0 and s < 1: #if s is greater than 0 and less than 1, stop the loop
                        break 
                xnorm = (((x/math.sqrt(s))*math.sqrt(-2*math.log(s)))*self.sd)+self.mean #convert x to normal number
                ynorm = (((y/math.sqrt(s))*math.sqrt(-2*math.log(s)))*self.sd)+self.mean #convert y to normal number
                norm.append(xnorm) #add normal number to vector
                norm.append(ynorm) #add normal number to vector
        return norm #return vector of normal numbers

    def pdf(self, x): #define probability density function for normal distribution for value x
        dens = (1.0/(self.sd*math.sqrt(2*math.pi)))*(math.e ** (-.5 * (((x - self.mean)/self.sd)**2))) #math
        return dens  #return probability of x
    

    # calculates the mean and stdev from a sample
    # and reassigns the parameters of the distribution
    
    def fit_mle(self, sample):
        self.mean = mean(sample) #calculate mean and define it as self.mean which was defined in the normal class above
        self.sd = std(sample) #calculate sd and define it as self.sd which was defined in the normal class above
        return

class binomial: #Set binomial distribution class
    def __init__(self,n,p): #Set paramaters n = number of trials, p = probability of success
        self.n = n #Set number of trials
        self.p = p #set probability of success

    def random_vec(self,rep=1): #Function to extract vector of random binomial values, default length of vector is 1
        res = [] #initializing list for binomial values 
        for i in range(rep): #running loop for number of values indicated by rep, ie the number of values you want
            succ=0 #initialize value for number of successes as 0
            for j in range(self.n): #running loop for number of trials indicated in binomial class function
                r = random() #grab a random number between 0 and 1
                if r < self.p: #if the value of r is less than the probability of success, a success has occured
                    succ += 1 #add 1 to the value of succ
            res.append(succ) #add the final value of succ to the list
        return res #return vector indicating successes

class exponential: #Defining exponential distribution class
    def __init__(self,rate): #set parameters for distribution, only one which is the rate
        self.rate = rate #Set rate

    def random_vec(self, n=1): #get random vector of exponential values, default number of values is 1
        exp = [] #initialize list to put exponential values in
        for rep in range(n): #setting up loop to sample exponential values
            r = random() #draw random number between 0 and 1
            val = math.log(1-r)/(-self.rate) #convert that value to exponential value
            exp.append(val) #add value to vector
        return exp #return vector

def main(): #main function
    norm = normal(0, 10) #values for normal distribution  
    #print(norm.random_vec(1000,"box_muller"))
    exp = exponential(2) #values for exponential distribution
    print(exp.random_vec(2))

if __name__ == "__main__":
    main()
