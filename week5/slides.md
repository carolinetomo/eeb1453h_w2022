---
theme: default
footer: 'eeb1453h | week 5'
---

# week 5: wright-fisher, birth and death 

caroline fukuchi

--- 

**markov property**

a process where a future state depends only on the present

the past thus has no bearing on our next step-- only the current state matters

---

**markov property**

this property is convenient for computing, because it lends itself well to a particular structure...


```
def things_that_happen():
  ...
  return stuff

for present in time:
  future = present + things_that_happen()
```

---

**wright-fisher process**
  - stochastic process describing allele loss and fixation
  - basic version considers only genetic drift

---


**wright-fisher process**

> A population of N genes evolves in discrete generations. Generation (k + 1) is formed from generation k by choosing N genes at random with replacement. i.e. each gene in generation (k + 1) chooses its parent at random from those present in generation k.

^ can you think of how you might implement this?

---

**binomial distribution**
  - you want to see how often one of two alternative outcomes occurs

---

**binomial distribution**
  - you want to see how often one of two alternative outcomes occurs
    - each outcome has probability _p_ and _1-p_ of happening

---

**binomial distribution**
  - you want to see how often one of two alternative outcomes occurs
  - try the thing _n_ times

---

**binomial distribution**
  - you want to see how often one of two alternative outcomes occurs
  - try the thing _n_ times
  - how many times does the outcome occur?

---

**binomial distribution**
  - params:
    - n: how many times you try the thing in total 
    - p: what is the probability of the outcome occuring in each trial?

---

implement a binomial distribution

---

**wright-fisher**

we can use the binomial distribution in each time step to determine our probability at the next step
  - _n_ = current population size
  - _p_ = the current allele frequency of allele 1 (numbered arbitrarily)

---

implement wright-fisher

---

**question:** standard wf models only drift. how might we add selection?

---

**birth and death**

  - individuals stochastically:
    - arise (birth)
    - disappear (death)


---

**birth and death**

  - population increments by integers according to params
    - birth (_b_)
    - death (_d_)

  - each birth or death is referred to as an 'event'

---

**birth and death**

we assume that:
  - this process is _markovian_
  - events occur one at a time

---

implement 'brute force' solution

---

**is there another way to do this??**

---

**poisson process**

- BD is a _poisson_ process
- events are drawn from a poisson distribution
- this offers us a key to faster algorithms

---

**poisson distribution**

- discrete probability dist
- 1 param:
  - rate -- how often do events happen?

---

**poisson distribution**

- PDs are weird and intricately linked to the markov property
  - each event is independent and not linked to other events

---

**poisson distribution**

- two fun properties:
  - PD can be derived from the binomial dist
    - divided into sub-intervals, what is the probability of 'success' (there is an event) vs not (no event) ?
    - limiting case of the binomial where the number of trials == infinity

---

**poisson distribution**

- two fun properties:
  - the waiting times between events are _exponentially distributed_

---

**exponential distribution**
  - single param
    - rate (different from the poisson rate, seen in next slide)

---

**poisson process and the exponential distribution**
  - b/c poisson is a markov process, events must be independently distributed
  - in fact, each time between an event is an _exponentially_ distributed rv

---

**poisson process and the exponential distribution**
  - lets refer to the rate for the poisson process _P_ as _λp_
  - waiting times for _P_ are drawn from an exponential dist with rate _λe_ = 1/_λp_

---

**birth-death process and poisson processes**

  - BD is a poisson process
  - in this case, _λp_ = _b_ + _d_

---

validate this relationship using our brute-force simulator

---

**how can we simulate a poisson process?**  

---

**"gillespie" or "doob-gilespie" algorithm**

- general approach is to draw waiting times from an exponential distribution
  - determine when the "next" event is

- for BD, we then need to decide what _type_ of event it is (birth or death?)
  - how might you do this?

---

**"gillespie" or "doob-gilespie" algorithm**

```
t = 0.0
max_time = 100.0
rel_birth_prob = b/(b+d)
n_ind = 10
res = []
while t < max_time:
  step = random_exponential(rate = 1/(b+d))  # how much time before an event happens? 
  t += step         			     # add our timestep to our tally of the time

  r = random()  

  if r < rel_birth_prob: # the event is a birth with probability equal to the rel prob of b vs d
    n_ind += 1
  else:                  # subtract an individual if the event is a death
    n_ind -= 1
  res.append(n_ind)
```
---


**homework**

if we don't get to it: implement a n exponential distribution class with a method to draw random samples

validate the distributional properties of our brute force bd simulator by plotting the simulated 

implement your own gillespie bd simulator
