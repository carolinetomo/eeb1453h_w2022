# this is a starter script you will use to add your generalization of the bday problem

from math import floor
from random import choice
import sys
import matplotlib.pyplot as plt

def pick_bday():
    n = 365
    #r = random()
    #draw = int( ( r * ( n ) ) )
    draw = choice(range(n))
    return draw

def share_bday(n):
    bdays = []

    for i in range(n):
        curbday = pick_bday()
        bdays.append(curbday)
    unique = set(bdays)
    if len(unique) < len(bdays):
        return True
    return False

def main():
    probs={}
    for i in range(100):
        if i < 2:
            continue
        reps = 1000
        pshare = 0
        for j in range(reps):
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
