import distributions as d


class wf:
    def __init__(self,n,freq):
        self.n = n
        self.freq = freq

    def run(self,ngen):
        proc_freqs=[self.freq]
        k = d.binomial(self.n,self.freq)
        for gen in range(ngen):
            freq_next = k.random_vec(1)[0] / self.n
            proc_freqs.append(freq_next)
            self.freq = freq_next
            k.p = self.freq
        return proc_freqs



