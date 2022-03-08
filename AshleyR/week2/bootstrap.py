import sys
from random import choice

def data_as_list(flnm):
	fl=open(flnm, "r")
	vals=[]
	for line in fl:
		spls=line.strip().split()
		try:
			val=float(spls[-1])/1000 #converts from g to kg
			vals.append(val)
		except:
			continue
	return vals

def calc_mean(values):
	tot=0.0
	count=0
	for i in values:
		tot+=i
		count+=1
	mean = tot/float(count)
	return mean

# take as input our data vector, and resample to simulate a new dataset
def subsample_ls(values):
	sim_vals=[]
	for i in range(len(values)):
		sim_vals.append(choice(values)) #appends a choice from values to our simulated dataset
	# NOTE: python uses whitespace instead of curly braces, so above loop ends now because we are no longer tabbing
	# print(len(values), len(sim_vals)) # for testing, this would print the length of values and sim_vals --> these should be the same length or something funky is happening
	# sys.exit() # for testing, this would exit after printing above line
	sim_mean = calc_mean(sim_vals) #calculates mean for sim_vals
	return sim_mean

def bootstrap_mean(values, reps=1000) #reps = # of times we're going to subsample
	emp_mean = calc_mean(values)

	for rep in range(reps):
		simdat = subsample_ls(values) #simulated dataset
	return

def main(args):
	vals = data_as_list(args[1])
	mean = calc_mean(vals)
	print(mean)
	return