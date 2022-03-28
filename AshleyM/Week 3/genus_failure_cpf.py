'''
CPF: as you stated in class, you are quite close here. i would suggest going to the 'key' and fixing up your solution and getting it running accordingly. or doing so without checking the 'key', if you want to get it on your own. no need to resubmit for marks.
'''



from dataclasses import dataclass
import math
import sys

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

def make_cuts(dat,nbins=10):
    biggest = max(dat)
    smallest = min(dat)
    span = biggest - smallest
    binwidth = span/float(nbins)
    bins = {}
    binfloor = smallest
    binceiling = binwidth
    count = 0

    while True:
        if binfloor >= biggest:
            break
        
        binceiling = binfloor + binwidth
        bins[count] = []
        bins[count].append(binfloor, binceiling)
        binfloor = binceiling
        count += 1
    return bins

class emp_dist:
    def __init__(self):
        self.dat = dat
        self.bins = make_cuts(self.dat)
        self.binp = self.binfreqs()
        self.upper = 0.0
        self.lower = 0.0
        self.genera = read_spdata(self.dat)

    def binfreqs(self):
        freqs = {}
        for i in self.bins: # initialize our dictionary by setting all counts to 0
            freqs[i] = 0

        for i in self.dat:
            for j in self.bins:
                currange = self.bins[j] # (bin min, bin max)
                if i >= currange[0] and i <= currange[1]:
                    freqs[j] += 1
                    break

        tot = float(len(self.dat))
        for i in freqs:
            freqs[i] = freqs[i]/tot

        return freqs

# homework: calculate the probability of an input under the empirial distribution
# as belonging to any of our genera
    def prob_x(self,x):

        # assign x to a bin
        for i in self.bins:
            currange = self.bins[i]
            if x >= currange[0] and x <= currange[1]:
                xbin = currange
                break

        genera = self.genera
        bins = self.binfreqs()

        xfreq = bins[xbin]


        for i in genera:
            generafreq = self.binfreqs()
            xgenfreq = generafreq[xbin]
            if xgenfreq >= xfreq:
                xfreq = xgenfreq
                xgen = genera[i]

        return xgen


# yoinked
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

#self.bins = {0:(0.0,5.0), 1:(5.0,10.0)}

class genus:
    def __init__(self,genname):
        self.name = genname
        self.species = []
        self.data = {}
        self.dist = None

    def mean(self):
        tot = 0
        count = 0
        for i in self.data:
            curval = self.data[i]
            if curval != None:
                tot+=curval
        if count != 0:
            m = tot/float(count)
        else:
            m = None
        return m

    genusdist = (mean(), stdev())
    dist = pdf(genusdist)



def main(fl):
    genera = read_spdata(fl)
    #print([i.name for i in genera])
    #print([i.data for i in genera])
    for gen in genera:
        if len(gen.data["diameter"])<4:
            continue
    



if __name__ == "__main__":
    main(sys.argv[1])
