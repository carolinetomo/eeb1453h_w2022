import sys

def make_cuts(dat,nbins=10):
    biggest = max(dat)
    smallest = min(dat)
    span = biggest - smallest
    bins = {}
    binfloor = smallest
    count = 0

    binwidth = span/float(nbins)
    while True:
        if binfloor >= biggest:
            break
        binceiling = binfloor + binwidth
        bins[count] = (binfloor,binceiling)
        binfloor = binceiling
        count+=1
    return bins

class emp_dist:
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
        return




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
