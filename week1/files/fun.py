## this is the script that we live-coded in the class on march 1. 
import sys
# ^import the sys library so that we can interact with the command line to find files to do things with


# this is for humans not computers
print("imported sys library")


# define a class to store things that we will call a genus:
class genus:
    def __init__(self, name):
        self.name = name
        self.mass = []
        self.neomass = []

    def mean(self):
        #calculate a mean for the genus
        mean = 0.0
        #self.mass
        return mean

# general function to calculate the mean from a list of (mostly) floats:
def mean(mass_ls):
    total = 0.0
    count = 0
    for mass in mass_ls:
        if mass != None:
            total += mass # means total = total + mass
            count+=1
    mean = None
    if count != 0:
        mean = total/float(count)
    return mean

# read in our file of interest and store it in memory
fl = sys.argv[1]
stuff = open(fl,"r")
#print(stuff.readline())

# separate out genera so that we can start to do things with them
genus_dict={}
for line in stuff:
    spls = line.strip().split()
    gen = spls[0]
    sp = "_".join(spls[1:-1])
    try:
        mass = float(spls[-1])
    except:
        mass = None
    try:
        genus_dict[gen].append(mass)
        print(gen)
    except:
        genus_dict[gen]=[]
        genus_dict[gen].append(mass)

for key in genus_dict:
   print(key,genus_dict[key])

test_gen = genus("Test")
print(test_gen.name)


"""
HINT: we can update the values associated with properties we have set in this new class like so:

test_masses = [10.3,11.8,9.1,13.2,7.9]
test_gen.mass = test_masses

we could also add an argument to our __init__ function so that we add this at the time of instantiation

```
class genus:
    def __init__(self,mass):
        self.name = ""
        self.neomass = []
        self.mass = mass
```

and so on. it all just depends on what you want to do.
another thing one might want to add is a record of all the associated species under the genus:

```
class genus:
    def __init__(self,mass):
        self.name = ""
        self.neomass = []
        self.mass = mass
        self.species = []
```

we can do that! we might even want to associate those species names with their associated masses. we can do that by changing the mass attribute to a dictionary instead of a list.

"""
