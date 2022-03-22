'''
bellow is the code provided by the prof that we need to edit/add to by:
extending  the simulation in one of the directions:
1) weight the probability of drawing birthdays according to the bias in birthdays actually seen in the (a/any) population
2) accommodate the possibility of encountering twins in any group by including the frequency of twins seen in the (or any) population
3) add leap years to the simulation

NOTE: we cannot use ant packages or libraries outside of the ones she has provided for us 
'''

# this is a starter script you will use to add your generalization of the bday problem

from math import floor
from random import choice
import sys
import matplotlib.pyplot as plt


'''
the code underneath is what i added to account for leap years. this math was based off of the info from:
https://math.stackexchange.com/questions/4004667/birthday-paradox-with-leap-year#:~:text=The%20total%20probability%20of%20all,that%2C%20or%200.25%2F365.25.
and http://www.efgh.com/math/birthday.htm
if we continue with the assumption that every day is as equally likely except for feb 29 which is 1/4 as likely  which
can occur in a space of 366 possibilities the total probability is 365.25
what I'm struggling with is if im even on the right track, and how to add this information to the code above :( 
'''
def leap_year(year):
    '''
    :param int:
    :param n:
    :return:
    '''
    is_leap_year = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    if is_leap_year:
        return 366
    
    return 365



def pick_bday(year):
    '''
    generate random birthday using choice method from random
    Note: another option instead of using choice can be randint. HOWEVER this method requires two arguments:
    (start, stop+1)
    example of code using randint
    draw = random.randint(1,366)
    :return: draw (a random number)
    '''
    n = leap_year(year)
    #r = random() 
    #draw = int( ( r * ( n ) ) )
    draw = choice(range(n))
    return draw
def share_bday(n):
    '''
    generating a list of random birthdays if there are duplicates
    :return: false or true
    '''
    bdays = []
    years =  range(1920,2022)
    for i in range(n):
        curbday = pick_bday(choice(years))
        bdays.append(curbday)
    unique = set(bdays) #set function turns the list of birthdays into a set, which cannot contain duplicates
    if len(unique) < len(bdays):
        return True #returning true will only occur if the length of unique set is lest than birthday list indicating no duplicates
    return False

def main():
    '''
    calculating the probability of shared birthdays over a set number of trials (in this case 100)
    :return:
    '''
    probs={}
    for i in range(100):
        if i < 2: #if there is no duplicate continue over itteration
            continue
        reps = 1000
        pshare = 0
        for j in range(reps):
            share = share_bday(i)
            if share:
                pshare += 1 #increasing by incriments of one
        pshare = float(pshare) / float(reps)
        probs[i]=pshare

    for i in range(100000):
        years =  range(1920,2022)
        pick = pick_bday(choice(years))
        print(pick)
    plt.scatter(probs.keys(),probs.values())
    plt.axhline(y=0.5,color='red')
    plt.axhline(y=1.0,color='red')
    plt.xlabel("# of people in group")
    plt.ylabel("prob(shared bday)")
    plt.show()

if __name__ == "__main__":
    main()
