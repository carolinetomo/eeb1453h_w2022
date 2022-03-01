import sys

class genus:
    def __init__(self, name):
        self.name = name
        self.mass = []
        self.neomass = []

    def mean(self):
        #calculate a mean for the genus
        #self.mass
        return

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

# this is for humans not computers
print("imported sys library")
fl = sys.argv[1]
stuff = open(fl,"r")
#print(stuff.readline())

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
   print(key,genus_dict[key],"\n")    

test_gen = genus("Test")
print(test_gen.name)