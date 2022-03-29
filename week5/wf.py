import distributions as d
import matplotlib.pyplot as plt

class wf:
    def __init__(self,n,freq):
        self.n = n
        self.freq = freq

    def run(self,ngen=100):
        proc_freqs=[]
        k = d.binomial(self.n, self.freq)

        for gen in range(ngen):
            freq_next = k.random_vec()[0] / self.n
            proc_freqs.append(freq_next)
            self.freq = freq_next
            k.p = self.freq
        return proc_freqs



class wf_sel:
    def __init__(self,n,freq,sel,her=1):
        self.n = n
        self.freq = freq
        self.sel = sel
        self.her = her # 0 = completely recessive; 1 = completely dominant; .5 = codominant

    def exp_freq(self):
        q = self.freq
        p = 1-q  # frequency of the 'other' allele
        q_next = ((q**2) * (1.0 + self.sel) + p*q*(1.0+self.her*self.sel))/(1.0+self.sel*q*((2.0*self.her*p)+q))
        return q_next

    def run(self,ngen=100):
        proc_freqs=[self.freq]
        for gen in range(ngen):
            exp_next = self.exp_freq()
            k = d.binomial(self.n, exp_next)
            freq_next = k.random_vec()[0] / self.n
            proc_freqs.append(freq_next)
            self.freq = freq_next
        return proc_freqs

if __name__ == "__main__":
    n = 100
    start_p = 0.5
    sel = 0.1
    ngen = 1000
    nrep = 100
    for i in range(nrep):
        #sim = wf(n,start_p)
        sim = wf_sel(n,start_p,sel)
        walk = sim.run(ngen)
        plt.plot(range(len(walk)),walk)
    plt.show()

