import sys
import distributions as d

def make_cuts(dat,nbins=10):
    '''

    :param dat: import the values this will allow us to set the sizes of our bins
    :param nbins: set the number of bins we want in our distribution
    :return:
    '''
    biggest = max(dat) #finding the largest value
    smallest = min(dat) #finding the smallest vale
    span = biggest - smallest #getting the range between the smallest and largest
    bins = {} #creating an empty dictionary to store our bins
    binfloor = smallest #creating a minimum number to start our bins based on the smallest value
    count = 0 #start count at 0

    binwidth = span/float(nbins) #creat the size of bins based on the range divided by the number of bins
    while True:
        if binfloor >= biggest: #if the binfloor is greater or equal to the largest number then stop
            break
        binceiling = binfloor + binwidth #create a bincieling to create the max size of the bin
        bins[count] = (binfloor,binceiling) #count the values in each bin
        binfloor = binceiling #the new bin floor will be the bincieling of the previous bin
        count+=1 #add 1 to the count
    return bins

class emp_dist: #creating a class for our empirical distribution
    def __init__(self,dat):
        self.dat = dat
        self.bins = make_cuts(self.dat)
        self.upper = 0.0
        self.lower = 0.0
        self.binp = self.binfreqs()

    def binfreqs(self):
        freqs = {}

        for i in self.bins: # initialize our dictionary
            freqs[i] = 0

        for i in self.dat:
            for j in self.bins:
                currange = self.bins[j] # (bin min, bin_max)
                if i >= currange[0] and i <= currange[1]:
                    freqs[j] += 1
                    break
        tot = float(len(self.dat))
        for i in freqs:
            freqs[i] = freqs[i]/tot
        return freqs

    # calculate the probability of an input under the empirical dist
    def prob_x(self,x):
        '''
        an empirical distribution  is one for which each possible event is assigned a probability derived from experimental
        observation. It is assumed that the events are independent and the sum of the probabilities is 1.

        the way the function is calculated is so that by ordering all of the unique observations in the data sample and
         calculating the cumulative probability for each as the number of observations less than or equal to a given
          observation divided by the total number of observations.
          such that:
          EDF(x) = number of observations <= x / n

          the
        :param x:
        :return:
        '''
        prob = 0
        for i in self.bins:
            bound = self.bins[i] 
            if not bound[0] <= x <= bound[1]:
                return 0
            else:
                prob = self.binp[i]
                break
        return prob



class genus:
    def __init__(self,genname):
        self.name = genname
        self.species = []
        self.data = {}
        self.dist = None

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
        genera.append(newgen)
    return genera


def main(fl):
    genera = read_spdata(fl)
    print([i for i in genera])

    """for gen in genera:
        if len(gen.data["diameter"])<4:
            continue"""


if __name__ == "__main__":
    # will need to adjust args to input an X. the goal is to find the most likely genus to which an unknown sample belongs
    main(sys.argv[1])
