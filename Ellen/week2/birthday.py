# this is a starter script you will use to add your generalization of the bday problem

##What is a pandas --> open source Python packages that is widely used for data science/data anlaysis and machine learning tasks --> basically
#a library in r

# Ceil(), floor() and Round() of dataframe gets the rounded up, truncated values and rounded off value of the column
#Ceil() --> round up the column of the dataframe
#floor() --> round down or truncate the column of the dataframe
#round() --> round of the value to the specified decimal places
from math import floor

from math import ceil

#Practice from internet

print("floor(-43.13) =", floor(-43.13))
#floor(-43.13) = -44
print("ceil(-43.13) = ", ceil(-43.13))
#ceil(-43.13) =  -43
print("round(-43.13) =", round(-43.13))
#round(-43.13) = -43

print("floor(10.5) =", floor(10.5))
#floor(10.5) = 10
print("ceil(10.5) = ", ceil(10.5))
#ceil(10.5) =  11
print("round(10.5) =", round(10.5))
#round(10.5) = 10
print("round(10.6) =", round(10.6))
#round(10.6) = 11


#the choice() function returns a random element from a non-empty sequences. For example select a random password from a a list of words.
#the sequence can be a list, strong or tuple
#If you pass an empty list or sequece sto choice, it will give an error
from random import choice

from random import random

#Pratice use

pets = ["dog", "cat", "bird", "hamster", "fish", "dragon", "snake", "rat", "rabbit"]

print("My ideal pet is a", choice(pets))
#My ideal pet is a snake

#A fun little loop

for i in range(5):
    my_pet = choice(pets)
    print(my_pet)

#cat
#dog
#dog
#rabbit
#cat
#cat and dog win

import sys

#python3 -m pip install --upgrade pip
#python3 -m pip install -U pip
#python3 -m pip install -U matplotlib

import matplotlib.pyplot as plt

#remember that def marks the begining of a function
#Then you have the function name
#Then you have the brackets which may contain your arguments through which we pass values to a function
#colon marks the end of the function header

#pick_bday()

def pick_bday(): #function pick_day():
    n = 365 #define n
    #r = random() # print random number between 0-1
    #draw = int( ( r * ( n ) ) ) #multiply random generated number by n and turn into integer to get random draw
    draw = choice(range(n)) #similar to above, but slightly less clunky
    return draw

#pick_bday()
#325
#pick_bday()
#277
#February 14th is 45th day, 9X30 = 270, 9 months after 45th day is 315th day

def pick_bias_bday():
    bias_prob = choice(range(100))
    bias_range = [*range(0,315), *range(316,365)]
    #bias_range = [*range(0,90), *range(91,315), *range(316,365)]
    if bias_prob <= 5:
        draw = 315
    #elif bias_prob == i in range(6,11):
        #draw = 90
    else:
        draw = choice(bias_range)
    return draw

#x = [*range(1,4), *range(6,11)]

def pick_leap_bday(): #function pick_day():
    leap_year = choice(range(1,5))
    if leap_year == 4:
        n =366
    else:
        n=365
    #r = random() # print random number between 0-1
    #draw = int( ( r * ( n ) ) ) #multiply random generated number by n and turn into integer to get random draw
    draw = choice(range(n)) #similar to above, but slightly less clunky
    return draw


##share_bday()
def share_bday(n): #New function
    bdays = [] #create an empty string

    for i in range(n):
        curbday = pick_bday() #use previous function to pick a random day of the year
        bdays.append(curbday) #add this random choice to your empty string "bdays" --> will create a string of 365 elements
    unique = set(bdays) #turns string into set object, items in set list are in random order, so it will appear in random order **REMOVES DOUBLES**
    if len(unique) < len(bdays): #Is the length of the set less than the length of the string --> if so that means there are doubled birthdays
        return True
    return False

#test to see how set works
#x = ("apple", "orange", "strawberry", "orange", "apple")
#set(x)
#{'orange', 'strawberry', 'apple'}

#Follow down with bias function
def share_bias_bday(n): #New function
    bdays = [] #create an empty string

    for i in range(n):
        curbday = pick_bias_bday() #use previous function to pick a random day of the year
        bdays.append(curbday) #add this random choice to your empty string "bdays" --> will create a string of 365 elements
    unique = set(bdays) #turns string into set object, items in set list are in random order, so it will appear in random order **REMOVES DOUBLES**
    if len(unique) < len(bdays): #Is the length of the set less than the length of the string --> if so that means there are doubled birthdays
        return True
    return False

#Follow down with leap function
def share_leap_bday(n): #New function
    bdays = [] #create an empty string

    for i in range(n):
        curbday = pick_leap_bday() #use previous function to pick a random day of the year
        bdays.append(curbday) #add this random choice to your empty string "bdays" --> will create a string of 365 elements
    unique = set(bdays) #turns string into set object, items in set list are in random order, so it will appear in random order **REMOVES DOUBLES**
    if len(unique) < len(bdays): #Is the length of the set less than the length of the string --> if so that means there are doubled birthdays
        return True
    return False

##Main function
def main(): #New function
    probs={} #empty dictionary
    for i in range(100): #starting a for loop for 100 trials
        if i < 2: #If value is less than 2 do nothing
            continue
        reps = 1000 #defining reps as 1000
        pshare = 0 #probability of sharing is 0
        for j in range(reps): #new for loop, for 1000 trials
            share = share_bday(i) #true or false, they share a birthday
            if share: #this is equivalent to sharing if share is true
                pshare += 1 #then probabilty is 100% or 1
        pshare = float(pshare) / float(reps) #change pshare into decimal, devide it by decimal of range
        probs[i]=pshare # probability of that number of people sharing a birthday is recorded in probs dictionary 
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()

"""for i in range(100000):
    pick = pick_bday()
    print(pick)"""

#follow down with bias function
def main_bias(): #New function
    probs={} #empty dictionary
    for i in range(100): #starting a for loop for 100 trials
        if i < 2: #If value is less than 2 do nothing
            continue
        reps = 1000 #defining reps as 1000
        pshare = 0 #probability of sharing is 0
        for j in range(reps): #new for loop, for 1000 trials
            share = share_bias_bday(i) #true or false, they share a birthday
            if share: #this is equivalent to sharing if share is true
                pshare += 1 #then probabilty is 100% or 1
        pshare = float(pshare) / float(reps) #change pshare into decimal, devide it by decimal of range
        probs[i]=pshare # probability of that number of people sharing a birthday is recorded in probs dictionary 
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()

##follow down with leap function
def main_leap(): #New function
    probs={} #empty dictionary
    for i in range(100): #starting a for loop for 100 trials
        if i < 2: #If value is less than 2 do nothing
            continue
        reps = 1000 #defining reps as 1000
        pshare = 0 #probability of sharing is 0
        for j in range(reps): #new for loop, for 1000 trials
            share = share_leap_bday(i) #true or false, they share a birthday
            if share: #this is equivalent to sharing if share is true
                pshare += 1 #then probabilty is 100% or 1
        pshare = float(pshare) / float(reps) #change pshare into decimal, devide it by decimal of range
        probs[i]=pshare # probability of that number of people sharing a birthday is recorded in probs dictionary 
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()



#When the interpreter runs a .py file, the __name__ variable will be set as __main__ if the file that is being run is the main program
#I think this means that it will read everything, but only run that main function that you defined --> makes sense considering all the other functions are feeding into that main one
#if the variable name is set to main then run main, it will only not be main if you set to not be that
#I think this means that if on the line "python code_to_run", you have birthday.py as the "code_to_run", it will run the main function
#if you import from birthdy.py, it will not run the main fucntion.

if __name__ == "__main__": ##Will return the main function all run
    main()


##Code tests
#share = share_bday(2)
#share
#False


#share = share_bday(10)
#share
#False

#share=share_bday(25)
#share
#True
