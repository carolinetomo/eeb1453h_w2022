import sys

import math

def make_cuts(dat,nbins=10):
    biggest = max(dat)
    smallest = min(dat)
    span = biggest - smallest
    bins = {}
    binfloor = smallest
    count = 0

    binwidth = span/float(nbins) #Remember that flaot converts integer (12) to a floating-point number (12.0)
    while True:
        if binfloor >= biggest:
            break
        binceiling = binfloor + binwidth
        bins[count] = (binfloor,binceiling)
        binfloor = binceiling
        count+=1
    return bins

def mean(dat):
    total = 0.0
    count = 0
    for mass in dat:
        if mass != None:
            total += mass # means total = total + mass
            count+=1
    mean = None
    if count != 0:
        mean = total/float(count)
    return mean

def sd(dat, mean):
    total = 0.0
    count = 0
    for mass in dat:
        if mass != None:
            count +=1
            total += (mass-mean)**2
    sd = None
    if count != 0:
        sd = math.sqrt(total/count)
    return sd

class emp_dist:
    def __init__(self,dat):
        self.dat = dat
        self.bins = make_cuts(self.dat)
        self.upper = 0.0
        self.lower = 0.0
        self.binp = self.binfreqs()

    def binfreqs(self):
        freqs = {} #Make freqs into a dictioary, 0:[a,b], 1:[c,d]

        for i in self.bins: # initialize our dictionary, for looping values in self.bins --> remember 0:[1,2], 1:[2,3], 2:[3,4]
            freqs[i] = 0 #A freqs entries start at zero

        for i in self.dat: #looping through all the values of in the dataset
            for j in self.bins: #loop through the values in self.bins dictionary
                currange = self.bins[j] # (bin min, bin_max)
                if i >= currange[0] and i <= currange[1]: #if the value in self.data is within the range specified by self.bins....
                    freqs[j] += 1 #increase the frequency value for that bin by 1
                    break #stop once you find what bin the data value is in
        tot = float(len(self.dat)) #get the float value of the size of the data set
        for i in freqs:
            freqs[i] = freqs[i]/tot #convert each frequency value for the bin into a proportion that could be graphed in a histogram
        return freqs

     #calculate the probability of an input under the empirical dist
    def prob_x(self,x):
        prob = 0
        for i in self.bins:
            boundaries = self.bins[i]
            #print(x, boundaries, self.binp[i])
            if x >= boundaries[0] and x <= boundaries[1]:
                prob = self.binp[i]
                #print("enter")
                break
        return prob

class normal:
    def __init__(self, mean = 0.0, sd = 1.0):
        self.mean = mean
        self.sd = sd

    def pdf(self, x):
        # HINT: to calculate the pdf, you will need math.e, math.pi, and math.sqrt
        density = 0 # here, you will plug the value X into the PDF for a normal distribution
        density = (1/(self.sd*math.sqrt(2*math.pi)))*math.e**((-1/2)*(((x-self.mean)/self.sd)**2))
        return density


#y = [1, 2, 2, 2, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9, 10]
#yy = emp_dist(y)
#yy.dat
#[1, 2, 2, 2, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9, 10]
#yy.bins
#{0: (1, 1.9), 1: (1.9, 2.8), 2: (2.8, 3.6999999999999997), 3: (3.6999999999999997, 4.6), 4: (4.6, 5.5), 5: (5.5, 6.4), 6: (6.4, 7.300000000000001), 7: (7.300000000000001, 8.200000000000001), 8: (8.200000000000001, 9.100000000000001), 9: (9.100000000000001, 10.000000000000002)}
#yy.binp
#{0: 0.05555555555555555, 1: 0.16666666666666666, 2: 0.0, 3: 0.05555555555555555, 4: 0.05555555555555555, 5: 0.2222222222222222, 6: 0.05555555555555555, 7: 0.1111111111111111, 8: 0.2222222222222222, 9: 0.05555555555555555}
#yy.prob_x(2)
#0.16666666666666666

class genus: #defining new class genus
    def __init__(self,genname): #things defined in this class
        self.name = genname #name of genus
        self.species = [] #species in genus
        self.data = {} #data on genus dictionary
        self.dist = None #distribution?
        self.paranorm = None

    
def read_spdata(fl,delim="_"): #function for reading species data
    opfl = open(fl,"r") #open the file and specific to read it, saved as opfl
    genvals = {} #initializing a dictionary
    genera = [] #initializing a list
    for line in opfl: #Loop through lines in dataset
        spls=line.strip().split() #spliting up data in each line into columns
        gen = spls[0] #specify genus
        val = spls[-1] #specify values
        try:
            val = float(val) #turn values into floats
        except:
            continue #ignore NA
        try:
            genvals[gen].append(val) #create dictionary with gen as key and values as input
        except:
            genvals[gen]=[]
            genvals[gen].append(val)

    for gen in genvals:
        newgen = genus(gen) #classify each key in dictionary as genus under new gen
        #newgen.species = genvals[gen].keys()
        newgen.data["diameter"] = genvals[gen] #Add values to specified class
        mean_calc = mean(genvals[gen])
        #print(mean_calc)
        sd_calc = sd(genvals[gen], mean_calc)
        #print(sd_calc)
        newgen.dist = emp_dist(genvals[gen])
        newgen.paranorm = normal(mean_calc, sd_calc)
        genera.append(newgen) #make new thing genera
    return genera #return genera

#Next step would be to define each genus as a emp_distribution class --> ie get each genus as a distribution
#Get a list of probabilities for x from each distribution
#Figure out where prob is highest and print the genus that this is


def main(fl, x): #Data going into function main
    genera = read_spdata(fl) #get genera data using newly created function
    #print([i for i in genera]) #Print all things in genera?
    #print genera
    """for gen in genera:
        if len(gen.data["diameter"])<4:
            continue"""
    #print(genera[0].name)
    #genera[0].dist = empirical distribution of type class
    #genera[0].dist.prob_x(x) --> input value --> only get one  --> need to get all --> {genus1: prob1, genus2: prob 2, etc}
    genus_like = {}
    pr_max = 0
    pr_max2 = 0
    name = ""
    name2 = ""
    for gen in genera:
        key = gen.name
        pr = gen.dist.prob_x(float(x))
        #print(pr)
        #print(gen.dist.binp)
        #print(gen.dist.bins)
        genus_like[key] = pr
        if pr > pr_max:
            pr_max = pr
            name = key
    print("Emperical Distribution:", name, pr_max)
    for gen in genera:
        key2 = gen.name
        pr2 = gen.paranorm.pdf(float(x))
        #print(pr2)
        genus_like[key2] = pr2
        if pr2 > pr_max2:
            pr_max2 = pr2
            name2 = key2
    print("Normal Distribution:", name2, pr_max2)
    
    


if __name__ == "__main__":
    # will need to adjust args to input an X. the goal is to find the most likely genus to which an unknown sample belongs
    main(sys.argv[1], sys.argv[2])


#for line in genera:
        #distribution = emp_dist(genera[1])
    #newgen.distribution = emp_dist(genvals[gen]) ##creating distribution for each genera? based on values in dictionary?


# ** is square, ** is to the power
