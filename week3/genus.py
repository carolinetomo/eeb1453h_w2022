import sys
import distributions as d

class genus:
    def __init__(self,genname):
        self.name = genname
        self.species = []
        self.data = {}
        self.dist = {}

    def mean(self, attr):
        tot = 0
        count = 0
        for i in self.data["attr"]:
            curval = self.data["attr"][i]
            if curval != None:
                tot+=curval
        if count != 0:
            m = tot/float(count)
        else:
            m = None
        return m

    def init_emp_dist(self,attr):
        dist = d.emp_dist(self.data[attr])
        self.dist['emp'] = dist

    def init_norm_dist(self,attr):
        dist = d.normal()
        dist.fit_mle(self.data[attr])
        self.dist['norm'] = dist

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


def main(fl,test_meas):
    genera = read_spdata(fl)
    for gen in genera:
        if len(gen.data["diameter"])<4:
            continue
        gen.init_emp_dist("diameter")
        print(gen.name,gen.dist['emp'].prob_x(test_meas))
        #print(gen.dist['emp'].p)


if __name__ == "__main__":
    # first arg should be data file, second arg should be value you want to evaluate across genera
    main(sys.argv[1],float(sys.argv[2]))
