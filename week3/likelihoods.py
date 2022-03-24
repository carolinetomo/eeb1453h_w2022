import sys,math
from genus import *
import matplotlib.pyplot as plt


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
        newgen.data["diameter"] = [math.log(i) for i in genvals[gen] if i > 0.0]
        genera.append(newgen)
    return genera


def main(fl,test_meas):
    test_meas = math.log(test_meas)
    genera = read_spdata(fl)
    for gen in genera:
        if len(gen.data["diameter"])<4:
            continue
        gen.init_emp_dist("diameter")
        gen.init_norm_dist("diameter")
        """
        plt.hist(gen.data['diameter'])
        plt.suptitle("emp")
        plt.show()
        plt.hist(gen.dist['norm'].random_vec(200,"polar"))
        plt.suptitle("norm")
        plt.show()
        """
        print(gen.name,"emp_p:",gen.dist['emp'].prob_x(test_meas),"norm_p:",gen.dist['norm'].pdf(test_meas))
        #print(gen.dist['emp'].p)


if __name__ == "__main__":
    main(sys.argv[1],float(sys.argv[2]))
