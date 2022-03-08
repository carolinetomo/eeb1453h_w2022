#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar1  10:16:41 2020

@author: puneeth
"""

import sys 

##----Defining a function to compute mean of a list with float and non-float values----##
def mean(a): 
    s = 0 
    n = 0
    for i in a:
        try: 
            s += i 
            n += 1
        except: 
            s += 0 
    if n != 0 : 
        return round(s/float(n),5)
        ##----Rounding because stupid python has unneccesary trailing term. Eg. 9.0 is displayed as 9.0000000001----##
    else: 
        return None
    

class genus: 
    def __init__(self, name, species_mass = {}): 
        self.name = name 
        self.species_mass = species_mass
        ##----The init runs only at initialization. Therefore if you update species_mass the following two commented attribute don't change ----##
#        self.species = self.species_mass.keys()
#        self.masses = self.species_mass.values()
        
    ##----For the above mentioned reason we need to define species and masses as methods rather than attributes----##
    def species(self):
        return self.species_mass.keys()
    def masses(self):
        return self.species_mass.values()
    def mean(self):
        return mean(self.masses())
        

print("imported sys library")


fl = sys.argv[1] ##----Read the index 1 input----##
fl_open = open(fl,"r") ##----Opening the mentioned filel----##


##----Lesson learnt: Once a file is read it becomes empty so you need to open it again ----##
#print(fl_open.readlines())
#fl_open.close()
#fl_open = open(fl,"r")

""" Method 1 """
genus_dict = {} 

for line in fl_open.readlines(): 
    line_spl = line.strip().split() ##----Split the sentence at whitespaces ----##
    genus_str = line_spl[0]
    sp = "_".join(line_spl[1:-1])
    try: 
        mass = float(line_spl[-1])
    except: 
        mass = None 
    try:
        genus_dict[genus_str] += [mass]
    except: 
        genus_dict[genus_str] = [mass]

genus_mean1 = {} 

for key in genus_dict:
    genus_mean1[key] = mean(genus_dict[key])
     
#print(genus_mean1)


""" Method 2 """
genus_dict = {} 
fl_open = open(fl,"r")  ##----Need to open the file again. Also see line 52----##
#print(fl_open.readlines())

for line in fl_open.readlines(): 
#    print('Entered')
    line_spl = line.strip().split()
    genus_str = line_spl[0]
    sp = "_".join(line_spl[1:-1])
    try: 
        mass = float(line_spl[-1])
    except: 
        mass = None 
    try:
        genus_dict[genus_str].species_mass[sp] = mass 
#        print('Entered try')
    except: 
        genus_dict[genus_str] = genus(genus_str,{sp:mass})
#        print('Entered try')

genus_mean2 = {} 

for key in genus_dict:
    genus_mean2[key] = genus_dict[key].mean()

#print(genus_mean2)
print(genus_mean1 == genus_mean2)
#
#for key in genus_dict:
#    print(genus_dict[key].species_mass)
#    print(genus_dict[key].masses)
#    print(genus_dict[key].species_mass.values())

#print(len(genus_mean1) == len(genus_mean2))

