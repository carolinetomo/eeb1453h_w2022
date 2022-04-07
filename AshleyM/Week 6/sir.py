import distributions as d
from random import choices
import sys

'''
how to use choices function

probs = [0.2,0.3,0.5]
event = ["thing1", "thing2", "thing3"]
choices(event, probs)

'''

class sir:
    def __init__(self, v, g, u, b, uu, s, i, r):
        self.v = v # rate infection
        self.g = g # rate recovery
        self.u = u # rate death
        self.b = b # rate birth
        self.uu = uu # rate non infection-related death
        self.s = s # susceptible count
        self.i = i # infected count
        self.r = r # recovered count

    def run(self, nstep, s, i, r):
        t = 0.0
        #res = {"t":[t], "s":[self.s], "i":[self.i], "r":[self.r]}
        #wait_times = d.exponential (1/(self.v+self.g+self.u+self.b))
        #probs = [self.v, self.g, self.u, self.b]
        #event = ["infection", "recovery", "death", "birth"]

        wait_times = d.exponential (1/(self.v+self.g+self.u+self.uu+self.b))

        while t < float(nstep):

            # rate of reinfection after recovery = 0.1
            # add in a rate of non infection-related deaths
            events = {"infect" : (s * r * 0.1 * self.v), "recovery" : (i * self.g), "death" : (i * self.u), "birth" : self.u, "unrdeath" : self.uu * s * i * r}
            event_rate = sum(events.values())
            wait_times.rate = 1.0/event_rate
            probs = [k / sum(events.values()) for k in events.values()]
            event = choices(population = list(events.keys()), weights = probs, k=1)[0]
            
            # need to decide that if there is an unrelated death, which group were they from?
            # implemented a 10% greater chance of someone infected dying of other unrelated calculations
            # which are not typically counted in infection deaths
            totalpop = s + i + r
            eligible = ["infect", "recovery", "susceptible"]
            deathprobs = [i/totalpop*1.1, r/totalpop, s/totalpop]
            whichdeath = choices (eligible,deathprobs)

            #print(event)
            #sys.exit()

            jumps = wait_times.random_vec(1)
            t += jumps[0]

            if event == 'infect':
                s -= 1
                i += 1
            elif event == 'recovery':
                s += 1
                i -= 1
                r += 1
            elif event == 'death':
                s -= 1
                i -= 1
            elif event == 'unrdeath':
                if whichdeath == 'infect':
                    i -= 1
                elif whichdeath == 'recovery':
                    r -= 1
                else:
                    s -= 1
            else:
                s += 1


        return [s, i, r]

if __name__ == "__main__":
    v = 0.1
    g = 0.9
    u = 0.05
    b = 0.1
    uu = 0.01
    s = 100
    i = 1
    r = 100
    nstep = float(1000)

    test = sir(v, g, u, b, uu, s, i, r)
    show = test.run(nstep, s, i, r)
    print(show)
            