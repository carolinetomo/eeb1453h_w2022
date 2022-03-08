## python fun.py primass.tab


##import library
import sys


##Print message
#print ("imported sys library")

#create special data object in python for genus as an example --> have properties and functionalities associated with them
#Tell python we want a class and the name of the class
#creating a template for a genus and telling python what it is --> creating an instance of that class
class genus:
        def __init__(self, name, mass): #self refers to the class itself as an agrument
                self.name = name
                self.mass = mass
                self.neomass = []
                self.species = []

        def mean(self):
            #calculate a mean for the genus
                mean= 0.0
            #self.mass
                return

##Playing with classes

#test_gen = genus("Test")
#print(test_gen.name)

#human = genus("homo", [10.3,11.8,9.1,13.2,7.9])

#print("Humans are part of the genus", human.name)
#print("Weight values in the genus homo are", human.mass)

#Examples I found online

#class Dog:
    
#def __init__(self, dogBreed, dogEyeColor):
    #self.breed = dogBreed
    #self.eyeColor = dogEyeColor
        
#tomita = Dog("Fox Terrier", "brown")

#print("This dog is a", tomita.breed, "and its eyes are", tomita.eyeColor)

#class Dog:                
 
    #def __init__(self, dogBreed="German Shepherd",dogEyeColor="Brown"): 
  
        #self.breed = dogBreed   
        #self.eyeColor = dogEyeColor

#charlie = Dog()

#print("Charlie is a", charlie.breed, "and he has", charlie.eyeColor, "eyes")

#toby = Dog("Poodle")

#print("Toby is a", toby.breed, "and he has", toby.eyeColor, "eyes")

##write own function --> want to calculate means for each of your lists --> take input and return output

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


##testing out the new mean function

#x = [1,2,3]
#y = mean(x)
#print("The mean of x is", y)


##read in one of week 1 files
##we have variables and can save things to them
##period allows us to assess all functions --> take things form command line and see what importaed
##print to write it to command line
## takes everything after python and says it is in a list, you could add agruments

## python fun.py gibberish stuff --> put gibberish and stuff in a list
##use this to tell python what file to read
## python fun.py primass.tab
## just read primass.tab

fl = sys.argv[1]

#print(fl)

##open the file you wish to open --> argument 1 is the path, second argrument two is tell python that you are reading this file

stuff = open(fl, "r")
stuff2 = open(fl, "r") #need a separate object to make the second dictionary run

#print(stuff)

## OUTPUT: <open file 'primass.tab', mode 'r' at 0x108a2e660>
##makes an object --> a data type that stores information --> file has been read by python and is being stored by python in library nestled within python
##can do stuff like readlines --> stuff.readlines() --> tells it to do the function readlines --> periods main that you are accessing things associated with that object
## this is why R is switching towards _

##Loop

genus_dict = {}
for line in stuff:
    #print(line) #method is a function that comes after a period, print all lines in file
    #print(type(line)) ## Tell you what each line is --> ie that it is a str
    #print(line.strip()) ## --> no white space
    #print(line.strip().split("\t")) ##makes any space a new element in line, if split has no argument it will split on any white space
    spls = line.strip().split()
    gen = spls[0]
    #sp = spls[1]
    #sp = spls[1:-1] ##take everything before the stop but not taking the stop won't work
    sp = "_".join(spls[1:-1])
    try:
        mass = float(spls[-1]) ##convert to float number, but will not read NA, also taking from the end
    except:
        mass = None ##don't do anything for NA
        continue ## not add them
    try:
        genus_dict[gen].append(mass)
        #print(gen)
    except:
        genus_dict[gen]=[]
        genus_dict[gen].append(mass)
        
for key in genus_dict:
        #print(key,genus_dict[key])
        #print(key) #prints only the genera
        #print(genus_dict[key]) #prints only the masses
        #print(mean(genus_dict[key])) ##Gives me the mean
        #print(key, genus_dict[key], mean(genus_dict[key])) #everything
        #check = key, genus_dict[key], mean(genus_dict[key]) ## saves as an object but only last genus because it isn't looping through

#print(check) ##prints the object
#genus_check = check[0]
#mass_check = check[1]
#mean_check = check[2]

#print(genus_check)
#print(mass_check)
#print(mean_check)

#print(genus_dict.keys())

##OUTPUT:
#['Trachypithecus', 'Pithecia', 'Nasalis', 'Cacajao', 'Microcebus', 'Papio',
 #'Pseudopotto', 'Chlorocebus', 'Oreonax', 'Pongo', 'Allocebus', 'Ateles', 'Allenopithecus',
 #'Aotus', 'Presbytis', 'Lophocebus', 'Cheirogaleus', 'Perodicticus', 'Pygathrix', 'Cebus',
 #'Cercopithecus', 'Semnopithecus', 'Brachyteles', 'Piliocolobus', 'Tarsius', 'Hylobates',
 #'Callimico', 'Mandrillus', 'Colobus', 'Galago', 'Lepilemur', 'Miopithecus', 'Arctocebus',
 #'Loris', 'Callicebus', 'Nycticebus', 'Lemur', 'Symphalangus', 'Lagothrix', 'Otolemur',
 #'Chiropotes', 'Callithrix', 'Procolobus', 'Avahi', 'Euoticus', 'Phaner', 'Eulemur',
 #'Saimiri', 'Rhinopithecus', 'Bunopithecus', 'Simias', 'Indri', 'Pan', 'Gorilla',
 #'Nomascus', 'Propithecus', 'Theropithecus', 'Saguinus', 'Cercocebus', 'Mirza',
 #'Homo', 'Varecia', 'Daubentonia', 'Hapalemur', 'Alouatta', 'Macaca', 'Prolemur', 'Leontopithecus', 'Erythrocebus']


##Trying to add species into dictionary

#Loop

genus_species_dict = {}
for line in stuff2:
        #print(line)
        spls_2 = line.strip().split()
        #print(spls_2)
        gen_2 = spls_2[0]
        #print(gen_2)
        sp_2 = spls_2[1]
        #print(sp_2)
        try:
                genus_species_dict[gen_2].append(sp_2)
                #print(gen_2)
        except:
                genus_species_dict[gen_2]=[]
                genus_species_dict[gen_2].append(sp_2)

#for key in genus_species_dict:
        #print(key,genus_species_dict[key])



