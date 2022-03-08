## file: primass.tab

import sys

# creating a method and functions for genus to associate specific parts of data
# with a specific genus
# data type that we are creating ourselves
class genus:
    #self: declass itself
    def __init__(self, name):
        self.name = name
        self.mass = []
        self.neomass = []

    def mean(self):
        #calculate and return value for mean of genus
        return


def mean(mass_ls): 
    total = 0.0
    count = 0
    for mass in mass_ls:
        # adds mass to total if a mass exists
        if mass != None:
            total += mass # total = total + mass
            count += 1

    mean = None
    
    if count != 0:
        mean = total/float(count)
        print (mean)
    return mean

# defines fl as 2nd value in our file list
fl = sys.argv[1]

# opens fl in read mode
stuff = open (fl, "r")

# create empty dictionary for genus
genus_dict={}

# populate genus_dict
for line in stuff:
    # splits into different 
    spls = line.strip().split()

    # defines each split
    gen = spls[0]
    sp = "_".join(spls[1:-1])

    # defines mass depending whether a value exists or N/A
    # can use except: continue if we do not want to define a datatype as "None"
    try:
        mass = float(spls[-1])
    except: 
        mass = None

    # populates genus dictionary with mass 
    # if the genus key exists in the dictionary, mass value is added to list
    try:
        genus_dict[gen].append(mass)
    # if the genus key does not exist in the dictionary, list is created and mass value is added
    except:
        genus_dict[gen] = []
        genus_dict[gen].append(mass)


# for each genus key created, print mass values in list
for key in genus_dict:
    print (key, genus_dict[key], "\n")

mean(genus_dict[1])



##test_gen = genus("Test")
##print (test_gen)
