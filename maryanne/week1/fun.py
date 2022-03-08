import sys

#this is for humans not computers
print("imported sys library")

class genus:
	def __int__(self, name):
		self.name = ""
		self.mass = []
		self.neomass = []
	def mean(self):
		#calculate mean for the gun
		return

def mean(mass_ls):
	total = 0.0
	count = 0 
	for mass in mass_ls:
		if mass !=None:
			total +=mass
			count+1	
	mean = None
	if count!= 0:
		mean = total/float(count)
	return mean


fl = sys.argv[1] #access list of arguments in our script
stuff = open(fl,"r")
print(stuff)

genus_dict = {}
for line in stuff:
	#print(line.strip()) #remove the white space
	spls = line.strip().split() 
	gen = spls[0]
	sp = "_".join(spls[1:-1])
	try:
		mass = float(spls[-1])
	except:
		continue
	try:
		genus_dict[gen].append(mass)
	except:
		genus_dict[gen]=[]
		genus_dict[gen].append(mass)
	for key in genus_dict:
		print(key,genus_dict[key], "\n")
test_gen = genus("test")
print(test_gen.name)


# split allows us to separate our data based on a deliminator in this case we used a space 
# we want to take the genus and then add the the value to the genus
# when we encounter a genus we want to append the dictionary by adding the values without overriding the previous 
#print(stuff.readlines()) # will allow us to read the file this is ugly tho
