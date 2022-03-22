import sys
import matplotlib.pyplot as plt
import distributions as dst 
import math

def mean(data_list): 
    total = 0 
    for val in data_list: 
        total+=val
    return total/float(len(data_list))

def std(data_list): 
    total_dev = 0 
    data_mean = mean(data_list)
    for val in data_list: 
        total_dev += (val - data_mean)**2 
    var = total_dev/float(len(data_list))
    return math.sqrt(var)

#Get list of bins from data. data = [ data points ], bins = number of bins we want, output = { 0:[cut_0,cut_1], 1:[cut_1,cut_2],..,bins:[cut_bins-1,cut_bins] }
def make_cuts(data,bins): 
    biggest = max(data)
    smallest = min(data) 
    span = biggest - smallest
    size_of_one = span/bins 
    cuts = [ round(smallest + size_of_one*i,6) for i in range(bins+1) ] 
    return { i:[cuts[i],cuts[i+1]] for i in range(len(cuts) - 1) }

def check_bin(value,bin_dict): 
#    output_exists = False
    for key in bin_dict: 
        bin_val = bin_dict[key]
        if value >= bin_val[0] and value <=bin_val[1]: 
            return key
    raise ValueError('The value ' + str(value) + ' is outside the range [' + str(bin_dict[0][0]) +', '+ str(bin_dict[list(bin_dict)[-1]][-1]) + ']' )

class create_dist():
    def __init__(self,data): 
        data.sort()
        self.data = data 
        self.upper = max(data)
        self.lower = min(data)
        #Deciding how many bins we want 
        max_diff = max([data[i] - data[i-1] for i in range(1,len(data))]) #minimum difference between two consecutive values
        min_diff = min([data[i] - data[i-1] for i in range(1,len(data))]) #maximum difference between two consecutive values
        bin_size = min_diff + (max_diff - min_diff)*0.33 #size of one bin = 33% of difference range 
        bins_num = int( (self.upper - self.lower)/float(bin_size) ) #number of bins from range and bin size
        self.bins = make_cuts(self.data,bins_num) #Get the bins from the data
        self.prob = { i:0 for i in self.bins } #probability distribution 
        self.vals = { i:[] for i in self.bins } #set of values which fall in each bin 
        
        #compute the prob of data falling in each bin
        for val in self.data: 
            for key in self.bins: 
                bin_vals = self.bins[key]
                if val >= bin_vals[0] and val <= bin_vals[1]: 
                    self.prob[key] += 1 
                    self.vals[key] += [val] 
                    break                    
        self.prob = [self.prob[key]/len(data) for key in range(len(self.prob)) ] #converting frequency into probability
    
    def dist_plot(self,plot_lab,xlab): 
        plt.plot([ (bin_val[0]+bin_val[1])*0.5 for bin_val in self.bins.values() ], self.prob, label = plot_lab)
        plt.xlabel(xlab)
        plt.ylabel("Probability")
        plt.title("Probability Distribution")
        plt.legend()
        plt.show()
        
        
    def prob_x(self, value): 
        try:
            key = check_bin(value,self.bins)
            prob = self.prob[key]
        except ValueError: 
            prob = 0 
        return prob
        

class genus:
    def __init__(self,genname):
        self.name = genname
        self.species = []
        self.data = {}
        
    def normal_dist(self,key):
        return dst.normal(mean(self.data[key]),std(self.data[key]))
        
    def emp_dist(self,key):
        return create_dist(self.data[key])
    
    


def read_spdata(fl,delim="_"):
#    print('start')
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



def main(inputs):
#    print('enter')
    file_name = inputs[1]
    value = float(inputs[2])
    genera = read_spdata(file_name)
    
#    for gen in genera: 
#        gen.dist("diameter").dist_plot(gen.name,"diameter")
#    print(len(genera))
    
    #Computed using empirical distribution
    genus_likelihoods = { gen.name:gen.emp_dist("diameter").prob_x(value) for gen in genera }
    print(genus_likelihoods)
    max_likelihood = max(genus_likelihoods.values() )
    genus_list = [] #list of genus with the maximum likelihood value
    for gen in genus_likelihoods :
        if genus_likelihoods[gen] == max_likelihood:
            genus_list += [gen]
    print(genus_list)
    
    #Computed using parametric distribution
    genus_likelihoods_para = { gen.name:gen.normal_dist("diameter").pdf(value) for gen in genera }
    print(genus_likelihoods_para)
    max_likelihood_para = max(genus_likelihoods_para.values() )
    genus_list_para = [] #list of genus with the maximum likelihood value
    for gen in genus_likelihoods_para :
        if genus_likelihoods_para[gen] == max_likelihood_para:
            genus_list_para += [gen]
    print(genus_list_para)



if __name__ == "__main__":
    main(sys.argv)
