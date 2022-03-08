import sys
from random import choice
import matplotlib.pyplot as plt

def data_as_list(flnm):
    fl=open(flnm,"r")
    vals=[]
    for line in fl:
        spls=line.strip().split()
        try:
            val=float(spls[-1])/1000 # divide to convert from g to kg
            vals.append(val)
        except:
            continue
    return vals

def calc_mean(values):
    tot=0.0
    count=0
    for i in values:
        tot+=i
        count+=1
    mean = tot/float(count)
    return mean

# take as input our data vector, and resample to simulate a new dataset
def subsample_ls(values):
    sim_vals=[]
    for i in range(len(values)):
        #resample stuff
        sim_vals.append(choice(values))
    #print(len(values),len(sim_vals))
    return sim_vals

def bootstrap_mean(values,reps=1000):
    emp_mean = calc_mean(values)
    sim_means = []
    for rep in range(reps):
        simdat = subsample_ls(values)
        sim_mean = calc_mean(simdat)    
        sim_means.append(sim_mean)
    print(min(sim_means),max(sim_means),emp_mean)

    plt.hist(sim_means, bins = 20,density=True)
    plt.axvline(x=emp_mean,color='red')
    plt.xlabel("estmate of mean body mass")
    plt.ylabel("probability")
    plt.show()
    return


def main(args):
    vals = data_as_list(args[1])
    bootstrap_mean(vals)
    return

if __name__ == "__main__":
    main(sys.argv)
