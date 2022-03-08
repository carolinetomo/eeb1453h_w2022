---
theme: default
footer: 'eeb1453h | week 2'
---

# week 2: simulation, frequencies, probabilities 

caroline.tomomi

---

> he felt the bubble lift him, felt it break and the dust whirlpool engulf him, dragging him down into cool darkness. for a moment, the sensation of coolness and the moisture were blessed relief. then, as his planet killed him, **it occurred to kynes that his father and all the other scientists were wrong: _the most persistent principles of the universe were accident and error._**

_dune_, frank herbert (1965)

---

what is stochasticity?

---

what is stochasticity?
  
  - behavior described by an underlying probability distribution

---

what is stochasticity?
  
  - behavior described by an underlying probability distribution
  - characterized by random 'noise'

---

what is stochasticity?
  
  - behavior described by an underlying probability distribution
  - characterized by random 'noise'
  - need to think a bit about **probabilities**

---

probability
  
  - number between zero and one
  - an event with probability 0 is impossible
  - an event with probability 1 is certain

---

there are debates about what probabilities actually are
  
  - one view: "probabilities are relative frequency of an outcome in repeated trials"
  - another: "probabilities reflect degree of belief"
  - in general, we'll just think of them as **reflecting uncertainty in a 'thing'**

---

random probability distributions

  - describe the probabilities of different "things"  
  - 'parametric' and 'nonparametric'

---

**'parametric' distributions**

  - e.g., normal, bernoulli, exponential 
  - mathematical function that reflects probabilities of 'things' given some parameters

---

**'nonparametric' (empirical) distributions**

  - estimated from some data
  - the probability of 'things' that result from some repeated trials

---

**simulation!**
  - we can simulate probabilities and probability distributions

---

**how do we generate randomness?**
  - generally use pseudo-randomness  

---

**computation of stochasticity**

---

**computation of stochasticity**

  - general approach is to draw lots of little probabilities over and over

---

**computation of stochasticity**

  - general approach is to draw lots of little probabilities over and over
  - these little probabilities sum to an instance of a distribution or stochastic process


---

**statistical uncertanity**
  - we can use also simulation to estimate our degree of certainty in a statistical estimate

---

**the bootstrap**
  - shuffle data a bunch of times and see how a number varies

---

_how might we use this to gauge certainty in an estimate?_

---

histograms are other examples of empirical probability distributions

---

**simulating _parametric_ distributions**

  - can also simulate parametric distributions using one of several approaches

---

**generating stochasticity**

  - we will use and abuse random.random()
    - returns a (pseudo)random number between 0 and 1

---

**the birthday problem**

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

**exponential**

  - lopsided distribution
  - single parameter: "rate" (aka "lambda")

---

**simulating exponential**

need to be a bit more clever

```
draw = random()
rate = 1        #can be any val >1

r = math.log(1-draw) / (-rate)
```

---

**normal**

  - "bell curve"
  - two parameters:
    - mean: central tendency
    - standard deviation: spread of the data


---

**simulating normal**

```
#need to draw 2 random values for this:
draw1 = random()
draw2 = random()

# specify some parameters:
mean = 10
sd = 2

n1 = (((math.sqrt(-2 * math.log(draw1)) * math.cos(2. * math.pi * y)) * sd) + mean)
n1 = (((math.sqrt(-2 * math.log(draw1)) * math.sin(2. * math.pi * y)) * sd) + mean)

# input: 2 uniform rv between 0 and 1, mean, standard deviation
# output: 2 normal rv 

```
---

**distributions have a couple of properties we will use a lot**

---

**cumulative density function (cdf)**
  - what is the probability of a random variable being equal to or smaller than?
  - generally looks a lot like the birthday problem solution

---

**probability density/mass function (pdf or pmf)**
  - what is the probability of a distribution generating a particular value?

