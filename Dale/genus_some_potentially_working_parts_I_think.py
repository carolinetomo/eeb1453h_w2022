import sys
import math

def make_cuts(dat,nbins=10): #Creating a function called make_cuts which takes a dataframe as an argument and makes a number of bins that we specify
    biggest = max(dat) #Defining biggest value as the maximum value in dat
    smallest = min(dat) #Defining smallest as the minimum value in dat
    span = biggest - smallest #Defining our span as the difference between the biggest and smallest value
    bins = {} #Creating an empty dictionary called bins
    binfloor = smallest #Defining the binfloor as the smallest value
    count = 0 #creating a count variable and defining it as starting at 0 (or rather defining it as 0 for now) 

    binwidth = span/float(nbins) #Defining binwidth as the span/number of bins. The total range of data/the number of boxes we want to split it into.
    while True: ## putting a while true statement so that the loop doesnt break
        if binfloor >= biggest: #Making an if-statement to say if the binfloor is equal to or greater than the biggest value, end the loop. 
            break #Break the loop if binfloor=biggest (end of data or at least that data)
        binceiling = binfloor + binwidth #Defining binceiling as binfloor + binwidth.
        bins[count] = (binfloor,binceiling) #Creating a key:value pair for our dictionary, bin. Saying when we give a count as a key, provide the associated binfloor and bincieling values
        binfloor = binceiling #Having produced our bin for a given value of count, we update our definition of binfloor to be binceiling, as the next bin's floor will be the previous bin's ceiling.
        count+=1 #Next we increase our count by 1 and re-start the loop, ending when we run out of bins (binfloor >= biggest)
    return bins #This statement returns a dictionary, bins, with keys as integers and tuples as values (binfloor,bincieling)


# Creating a function to check through bins for the x value: 
def bin_checker(x_value, dict_of_bins):
    for bin_key in dict_of_bins:
        bin_val = dict_of_bins[key]
        if value >= bin_val[0] and value <=bin_val[1] #this is the same structure as what we did in class to make freqs{}
            return key







class emp_dist: #Creating a new class of object called emp_dist 
    def __init__(self,dat): #Initializing the class and it has the property of dat, data
        self.dat = dat
        self.bins = make_cuts(self.dat) #Property of emp_dist is bins, which we create using our make_cuts function
        #This will create the bins using the code we see between lines 11-19. The number of bins should be specified in the make_cuts fuction itself
        self.upper = 0.0 #Defining upper and lower bounds as empty things for now. 
        self.lower = 0.0
        self.binp = self.binfreqs() #Defining binp (bin probability) as a property. We will get this property of any given emp_dist using the binfreqs() method. 

    def binfreqs(self): #Defining binfreqs() method
        freqs = {} #Creating an empty dictionary called freqs

        for i in self.bins: # initialize our dictionary
            freqs[i] = 0 #
#I believe this code here is saying to iterate through the keys of our dictionary, bins, then to enter values into a new dictionary, freqs,
#such that i is the key from bins AND we use the same key for freqs. Eventually, freqs and bins will have the same keys but store different values.
#The goal is for freqs to store a probability density and for bins to store binfloor and binceiling
        for i in self.dat: #Iterating through the data 1 value at a time
            for j in self.bins: #iterate through bins based on their key number
                currange = self.bins[j] # Define our current range (bin_min, bin_max). We access this tuple by giving the key, j, to the dictionary self.bins
                if i >= currange[0] and i <= currange[1]: #For each data point, we will check and see if the value falls within the bin range
                    #if it is within the value of the bin range then...
                    freqs[j] += 1 #we add 1 to the value corresponding to that bin's key in the freqs dictionary
                    break #Break the loop after we've added that value to freqs, so that we can examine the next datapoint
        tot = float(len(self.dat)) #calculate our total numbrt of data points as the length of dat
        for i in freqs: #Iterating through our dictionary freqs
            freqs[i] = freqs[i]/tot #updating our dictionary to give us values/total (i.e. turning counts into frequencies)
        return freqs
        #Return our freqs dictionary from this

 #calculate the probability of an input under the empirical dist

 #Conceptualizing the problem: 

 #What we want: A bunch of objects of the class ~genus~ each with their own properties, of which an empirical distribution will be one (emp_dist). Probs wants these genera in a list
 # What we want to do: For each unknown value, x, we want to [go through our list of genera], checking the [emp_dist] of each genus to [see if ~x~ is within the distribtuion].
 # If x is within the distribution, we want to [go through the bins in the distribution 1 at a time] and when we find the bin in which the x value is found, we want the [probability density]
 #of that bin (i.e. the value of that bin from the freq dictionary). We would also like the output from iterating through all of the genuses to be a list of probability densities 
 # or if we are feeling super ambitious, it could be nice to have the output be a dictionary with keys as genera and values as likelihoods
 # 

 

 #  Making the prob x method

 #Not completely sure if working, since some difficulty adding to the main function. 
    def prob_x(self,x):
        probability = 0 #creating empty probability value
        for i in self.bins: #iterating through the keys of the bins dictionary
            up_low_bounds = self.bins[i] #Bin boundaries given by tuple of values in bins
            if not up_low_bounds[0]<=x<=up_low_bounds[1]:
                return 0
            else:
                probability = self.binp[i] #this is the value from the binfreqs dictionary as defined in our emp_dist class
                break
        return probability 


   
         #the idea is to have a functional script that takes two inputs-- a data file and an unknown sample -- 
  #  return          #and identifies the most likely genus to which the unknown sample belongs. you will be taking the 
                        #unknown measurement and checking its probability given the empirical distributions that we have calculated for each genus.


##Parametric Dist Stuff

#making a class called normal which will be a normal distribution
class normal:
    def __init__(self,mean=0,stdev=1):
        self.mean = mean
        self.stdev = stdev 
    #making a method ~pdf~ which will calculate the probability density function 
    def pdf(self,x): #Takes vlalue x and calculates the area under the curve (?)
        prob_density = 0 #making an empty probability density value first
        prob_density = (1/(self.sd*math.sqrt(2*math.pi)))*math.e**((-1/2)*(((x-self.mean)/self.sd)**2))
        return prob_density #entering in the equation to calculate probability density





class genus: #intializing our class, genus
    def __init__(self,genname):
        self.name = genname #Giving property genname,--- genus name
        self.species = [] #Making an empty list to hold species names within the genus
        self.data = {} #Making an empty dictionary to hold information about indv in the genus
        self.dist = None #making an empty distribution for the genus 

    def mean(self, attr):
        return

def read_spdata(fl,delim="_"):
    opfl = open(fl,"r")
    genvals = {}
    genera = []
    for line in opfl:
        spls=line.strip().split()
        gen = spls[0]
        val = spls[-1]
        try:
            val = float(val)
        except:
            continue
        try:
            genvals[gen].append(val)
        except:
            genvals[gen]=[]
            genvals[gen].append(val)

    for gen in genvals:
        newgen = genus(gen)
        #newgen.species = genvals[gen].keys()
        newgen.data["diameter"] = genvals[gen]
        newgen.dist = emp_dist(newgen.data['diameter']) #making a new distribution for each genus 
        genera.append(newgen)
    return genera  

#####MAIN FUNCTION WHERE THINGS HAPPEN

#Definitley confused about how to meld together all of the parts and put them in the main function

def main(fl, x):
    genera = read_spdata(fl) #retrieving our list of genera and data using the read_spdata function
    for gen in genera: #
        gen.dist = emp_dist(gen.data["diameter"])
        break

        






#def main(fl):
    #genvals = read_spdata(fl)#Defining genvals as a dictionary of of our genera and measurements from the plant_genera.tab file #Defining the function prob_x which takes a dataframe and a value as its arguments 

        #STUFF THAT GOES IN PROB X 
    #for key in genvals: #printing a list of the genera 
     #   print(key)
    
#If I want to see something from an output I have to put some code which will generate that output into the main function. 
    """for gen in genera:
        if len(gen.data["diameter"])<4:
            continue"""


if __name__ == "__main__":
    # Updated to also take X as an argument
    main(sys.argv[1]) 











    