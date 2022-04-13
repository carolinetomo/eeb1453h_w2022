import distributions as d
from random import choices #probs = [0.2,0.3,0.5] events = ['thing 1', 'thing2', 'thing3'] choices(events,probs)
import math
import matplotlib.pyplot as plt

#adding unrelated deaths 

class sir:
    def __init__(self, v, g, u, d, b, s, i, r):
        '''
        :param v: rate of s-->i
        :param g: rate of --->r
        :param u: rate of i-->death
        :param d: rate of death not by virus s,i,r --> death
        :param b: rate of birth --> s
        :param s: susceptible
        :param i: infected
        :param r: recovered
        '''
        self.v = v
        self.g = g
        self.u = u
        self.b = b
        self.d = d
        self.s = s
        self.i = i
        self.r = r

    def run(self, nsteps):
        t = 0.0
        res = {"t": [t], "s": [self.s], "i": [self.i], "r": [self.r]}
        wait_times = d.exponential(1.0)
        while len(res["t"]) < nsteps:
            prob_r = self.i * self.g
            prob_i = self.b * self.s * self.i
            prob_s = self.i * self.u
            prob_death = self.i * self.u
            prob_noninfec_death = self.s * self.i * self.r * self.d
            events = {"infection": prob_i, 'recovery': prob_r, 'death': prob_death, 'birth': prob_s,
                      "noninfec_death": prob_noninfec_death}
            event_rate = sum(events.values())
            wait_times.rate = 1.0/event_rate
            t += wait_times.random_vec(1)[0]
            probs = [k/sum(events.values()) for k in events.values()]
            event = choices(population=list(events.keys()), weights=probs, k=1)[0]
            total_pop = self.s + self.i + self.r
            posibilities = ["infect", "recovery", "susceptible"]
            death_probs = [self.i / total_pop * 1.1, self.r / total_pop, self.s / total_pop]
            death_type = choices(posibilities, death_probs)
            if event == "infection":
                self.s -= 1
                self.i += 1
            elif event == "recovery":
                self.i -= 1
                self.r += 1
            elif event == 'death':
                self.i -= 1
            elif event == 'birth':
                self.s += 1
            elif event == 'noninfec_death':
                if death_type == 'infect':
                    self.i -= 1
                elif death_type == ' recovery':
                    self.r -= 1
                else:
                    self.s -= 1
            else:
                self.s += 1
            res['t'].append(t)
            res['s'].append(self.s)
            res['i'].append(self.i)
            res['r'].append(self.r)
        return res

if __name__ == "__main__":
    v = 0.1
    g = 0.1
    u = 0.1
    d = 0.1
    b = 0.1
    s = 100
    i = 10
    r = 100
    #does_it_work = sir(v, g, u, b, d, s, i, r)
    #show = does_it_work.run(20)
    #print(show)
    plt.plot(res["t"], res["s"], label="s")
    plt.plot(res["t"], res["i"], label="i")
    plt.plot(res["t"], res["r"], label="r")
    plt.legend(loc="upper left")
    plt.show()
