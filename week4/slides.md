---
theme: default
footer: 'eeb1453h | week 4'
---

# week 4: parametrics, simulation, and random walks 

caroline.tomomi

---

genera empirical distributions

---

**uniform**

  - just draw a random number a bunch of times
  - usually specifies maximum and minimum bounds

---

**simulating uniform**

```
draw = random()

r = lower + (draw * (upper-lower))
``` 

---
**normal** (aka gaussian, "bell curve")

  - two parameters:
    - mean: central tendency
    - standard deviation: spread of the data
---

**simulating normal**

_transform two uniform rvs into two normal rvs_

```
draw1 = random()
draw2 = random()

# specify some parameters:
mean = 10
sd = 2

n1 = (((math.sqrt(-2 * math.log(draw1)) * math.cos(2. * math.pi * y)) * sd) + mean)
n2 = (((math.sqrt(-2 * math.log(draw1)) * math.sin(2. * math.pi * y)) * sd) + mean)
```

---

implement normal class with random draws

...go!

---

**random walk**
  - at each step, i move to the right or left with equal probability 
  - (this is a simple random walk)

![h:320](images/drunkwalk.png) 

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

**brownian motion**
  - a type of random walk defined by a normal distribution
  - parameter: _σ_, "instantaneous rate"
  - the trajectory at each step is defined by adding a normal rv with mean == 0 and std == rate of the process


![h:320](images/brownian.png) 

---

**brownian motion**
  - the variance is non-fixed-- increases infinitely with time
  - the mean of the process is the starting value

![h:320](images/brownian.png) 

---

implement brownian motion and plot

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
    - p: what is the probability of the out come occuring in each trial?

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

**homework**

can you make brownian motion behave like wright fisher? 

can you identify an pop\_size and brownian rates that yield similar behavior?


