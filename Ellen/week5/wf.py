import distributions as d
import matplotlib.pyplot as plt

class wf: ## Set up class for wright fisher, drift process = NO selection
    def __init__(self,n,freq): #two parameters are associated with writing fisher, n and frequency
        self.n = n # setting the population size
        self.freq = freq # setting the allele frequency

    def run(self,ngen=100): # function to run to simulate the wright fisher process, number of generations to run the simulation is indicated
        proc_freqs=[self.freq] #initializing proc_freq list which will contain the changing allele frequencies
        k = d.binomial(self.n, self.freq) #this is a binomial process, the number of individuals is the number of trials, and the frequency of the allele is the probability of success

        for gen in range(ngen): #Running a loop with the number of generations indicated in the run function
            freq_next = k.random_vec()[0] / self.n #frequency of next gen is a binomial number (number of times successfully drawing allele in population divided by population = frquency)
            proc_freqs.append(freq_next) #add this value to list of allele frequencies
            self.freq = freq_next #change the value of self.freq to for wf class to the new allele frequency
            k.p = self.freq #change the probability of success in binomial distribution k to new allele frequency
        return proc_freqs #return changing values of allele frequency



class wf_sel: # Set up class for wright fisher process WITH selection
    def __init__(self,n,freq,sel,her=1): #indicate parameters of class, add parameters for selection and heritability
        self.n = n #set population size
        self.freq = freq #set allele frequency
        self.sel = sel #set selection coefficient
        self.her = her # 0 = completely recessive; 1 = completely dominant; .5 = codominant, set heritability

    def exp_freq(self): #define function that will calculate the allele frequency in the next generation based on hardy-weinberg
        q = self.freq #set q as original allele frequency
        p = 1-q  # frequency of the 'other' allele
        q_next = ((q**2) * (1.0 + self.sel) + p*q*(1.0+self.her*self.sel))/(1.0+self.sel*q*((2.0*self.her*p)+q)) #Hardy weinberg frequency of q in next gen
        return q_next #return allele frequency from next generation

    def run(self,ngen=100): #define function to run the wf simulation with the number of generations being 100
        proc_freqs=[self.freq] #define a list to put allele frequencies in with self.freq (initial frequency as the first entry
        for gen in range(ngen): #start loop for how ever many generations indicated in the function
            exp_next = self.exp_freq() #get the next generation allele frequency based on selection
            k = d.binomial(self.n, exp_next) #run that allele frequency through a binomial function to account for drift
            freq_next = k.random_vec()[0] / self.n #convert resulting successes into an allele frequency
            proc_freqs.append(freq_next) #Add this allele frequency to the list you created
            self.freq = freq_next #Save new allele frequency as what goes into the loop
        return proc_freqs #return vector of allele frequencies

if __name__ == "__main__":
    n = 100 #population size
    start_p = 0.5 #starting population frequency
    sel = 0.1 #selection coefficient
    ngen = 1000 #number of generation to run simulation for
    nrep = 100 #number of simulations
    for i in range(nrep): #set up loop to run a bunch of simulations
        #sim = wf(n,start_p)
        sim = wf_sel(n,start_p,sel) #set up class of wf with selection
        walk = sim.run(ngen) #Run the simulation
        plt.plot(range(len(walk)),walk) #plot all the simulations
    plt.show() #show the plot
