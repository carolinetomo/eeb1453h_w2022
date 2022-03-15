# this is a starter script you will use to add your generalization of the bday problem

from math import floor
from random import choice
import sys
import matplotlib.pyplot as plt

def pick_bday(): #This just picks a day of the year for the birthday randomly
    n = 365
    #r = random()
    #draw = int( ( r * ( n ) ) )
    draw = choice(range(n))
    return draw

def share_bday(n): #defining a function, share_bdat which takes n as an argument (# of things we are picking)
    bdays = [] #Generates an empty bdays list of length n 

    for i in range(n): 
        curbday = pick_bday()  #Grabbing 1 random birthday
        bdays.append(curbday)  #Adding that birthday to the list after we've selected it
    unique = set(bdays)        #Getting the number of unique birthdays from the list
    if len(unique) < len(bdays): #If the length of unique birthdays is less than the number of birthdays, there must be a shared one
        return True              #If there is a shared birthday, return True
    return False                 #If there is not a shared birthday, return False

def main():  #Creating a main function
    probs={}  
    for i in range(100): 
        if i < 2:
            continue
        reps = 1000 #Doing a 1000 iterations of the loop
        pshare = 0
        for j in range(reps): #another for loop specifying that if there are shared birthdays, give us the #of shared/total number of bdays picked to get a probabiltiy
            share = share_bday(i)
            if share:
                pshare += 1
        pshare = float(pshare) / float(reps)
        probs[i]=pshare
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()

"""for i in range(100000):
    pick = pick_bday()
    print(pick)"""

if __name__ == "__main__":
    main()

# Let's try and extend this birthday problem to account for the chance of twins. 
# Actually figuring out the chance that 2 randomly selected people are twins is very difficult
#Without knowing how people will be selected or from where. 
#WIth this in mind, I will try to use information about the prevalence of twins in the population
#To account for this prior expectation. 


#Trying to work through the logic and figure out what needs to change. 

#Picking birthdays will still need to happen, so the pick_bday() function can remain the same
def pick_bday(): 
    n = 365
    #r = random()
    #draw = int( ( r * ( n ) ) )
    draw = choice(range(n))
    return draw

#We will still need to know if indv share a birthday, so we can also keep the share_bday() func.
def share_bday(n): #defining a function, share_bday which takes n as an argument (# of things we are picking)
    bdays = [] #Generates an empty bdays list of length n 

    for i in range(n): 
        curbday = pick_bday()  #Grabbing 1 random birthday
        bdays.append(curbday)  #Adding that birthday to the list after we've selected it
    unique = set(bdays)        #Getting the number of unique birthdays from the list
    if len(unique) < len(bdays): #If the length of unique birthdays is less than the number of birthdays, there must be a shared one
        return True              #If there is a shared birthday, return True
    return False               


#Now we'll need info about twins 

#Twins account for 1/42 people in the general population. 
#So considering random sampling, each indv selected has a 1/42 chance of being a twin. 

#Let's mirror the structure above to try and make a function which will tell us if an individual is a twin 
#To accomplish this, I'll first make a function which picks a number between 1-42, since twins are 1/42 people in the pop and call it pick_twinning

def pick_twinning():
    n = 42
    draw = choice(range(n))
    return(draw)

#Again mirroring the above structure, I'll make a a function which will tell us if there is a twin in the midst of a list
#I'll call this function real_twin()

def real_twin(n):
    twins = []

    for i in range(n):
        twinosity = pick_twinning()
        twins.append(twinosity)
    unique_twin = set(twins)
    if len(unique_twin) < len(twins):
        return True
    return False 


#Now we have functions to tell us if an indvidual shares a birthday and to tell us if an individual is a twin. 
#I'd like to try and combine these to know, what is the probability that 2 individuals share a birthday and are both twins (not necessarily with eachother)

#To do this, I will attempt to edit the main function to incorporate our new information and new functions 

def main():  #Creating a main function
    probs={}  
    for i in range(100): 
        if i < 2:
            continue
        reps = 1000 #Doing a 1000 iterations of the loop
        pshare = 0
        for j in range(reps): #another for loop specifying that if there are shared birthdays, give us the #of shared/total number of bdays picked to get a probabiltiy
            share = share_bday(i)
            if share:
                pshare += 1
        pshare = float(pshare) / float(reps)
        probs[i]=pshare
        ptwin = 0
        for k in range(reps): #Trying to use the same format as before to add another for loop which tells us if we have twins or not. 
            twin = real_twin(i) 
            if twin:
                ptwin += 1
        ptwin = float(ptwin) / float (reps)
        probs[i]=ptwin #Plotting stuff isn't working so I Can't quite see if this has affected our outcome
        
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()


#Birthday problem extension: Doing it for a range of possible values of group sizes

#Defining a min and max number of people
MIN_NUM_PEOP = 2
MAX_NUM_PEOP = 50

#Now making a range of n values and storing them in an object called ns 
ns = range(MIN_NUM_PEOP, MAX_NUM_PEOP+1)

#Making an empty list which will hold the probabilities for each n value
n_probs = []

# Using a for loop to iterate over our range of values

for n in ns:
    prob_together = share_bday(n)
    n_probs.append(prob_together)


# Putting the code altogether

def estimate_p_for_range_o_vals(ns):
    n_probs = []

    for n in ns:
        prob_together = share_bday(n)
        n_probs.append(prob_together)
    return n_probs



### Thoughts on using this format for a weighted distribution of births

#Thought maybe could give each day more than 1 number representing it if it had more bdays than normal, and do across range of people sizes using this format?

#e.g 10000 units which are split among 365 days depending on prior knowledge of the prob of being born on that day



















