
### TESTING OF MULTIPLES HYPOTHESIS (ie. Bean vs each color bean)

# TUTORIAL
# https://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/

# pymc tutorial
# http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
import pymc
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

### simple compare A/B

# Website A had 1055 clicks and 28 sign-ups
values_A = np.hstack(([0]*(1055-28),[1]*28))
# Website B had 1057 clicks and 45 sign-ups
values_B = np.hstack(([0]*(1057-45),[1]*45))

### Bernoulli Model
# Bernoulli trial is a random experiment with only two possible outcomes.
# Binomial experiment is a sequence of Bernoulli trials performed independently.
# https://en.wikipedia.org/wiki/Bernoulli_distribution

# Create a uniform prior for the probabilities p_a and p_b
p_A = pymc.Uniform('p_A', 0, 1)
p_B = pymc.Uniform('p_B', 0, 1)

# Creates a posterior distribution of B - A
@pymc.deterministic
def delta(p_A = p_A, p_B = p_B):
    return p_B - p_A

# Create the Bernoulli variables for the observation
obs_A = pymc.Bernoulli('obs_A', p_A, value = values_A , observed = True)
obs_B = pymc.Bernoulli('obs_B', p_B, value = values_B , observed = True)

# Create the model and run the sampling
model = pymc.Model([p_A, p_B, delta, values_A, values_B])
mcmc = pymc.MCMC(model)
# Sample 1,000,000 million points and throw out the first 500,000
mcmc.sample(1000000, 500000)


## Plot dist
delta_distribution = mcmc.trace('delta')[:]

def myplot():
    sns.kdeplot(delta_distribution, shade = True)
    plt.axvline(0.00, color = 'black')

myplot()


### Prop website A, get more signups than BaseException
print "Probability that website A gets MORE sign-ups than site B: %0.3f" % (delta_distribution < 0).mean()
print "Probability that website A gets LESS sign-ups than site B: %0.3f" % (delta_distribution > 0).mean()



#### What if if you have n sites instead of 2?
# Now you have the color bean problem.
# we use .95% confidence
# at n=10 prob no false positive = (.95)^10 ~ .6 
# so we have 1-.6 = 40% prob for one or more false positives...


#### Beta delta_distribution
# - A way to generalize distribution from 0,1
# https://en.wikipedia.org/wiki/Beta_distribution
# pdf_beta(a,b) = (1/B(a,b)) * (x^(a-1) * (1-x(b-1)) 
# 1/B(a,b) is a normalize function (for sum 1)

# example of some beta functions
def my_beta(a,b,n=100):
    x = np.linspace(0,1,n)
    y = (x**(a-1))*((1-x)**(b-1))
    y = n*y/(np.sum(y))
    return (x,y)

for i in range(1,30):
    plt.plot(*my_beta(i,10,100))



### Hirachial modelling:

# Again it is a binomial model Binominal(ni,pi)
# instead of assuming each pi (conversion from a home page)
# is uniform prior, we assume the prior comes from a beta distribution. 

# which beta distribution?
# f(a,b) ~ (a+b)^(-5/2) where a,b > 0.
# logit of the mean, log(a/b), and the log of the "sample size", log(a+b),
# hmmm. Look into why?

@pymc.stochastic(dtype=np.float64)
def beta_priors(value=[1.0, 1.0]):
    a, b = value
    if a <= 0 or b <= 0:
        return -np.inf
    else:
        return np.log(np.power((a + b), -2.5))
 
a = beta_priors[0]
b = beta_priors[1]


### Do example with 5 home pages
# The hidden, true rate for each website.
true_rates = pymc.Beta('true_rates', a, b, size=5)

# The observed values
trials = np.array([1055, 1057, 1065, 1039, 1046])
successes = np.array([28, 45, 69, 58, 60])
observed_values = pymc.Binomial('observed_values', trials, true_rates, observed=True, value=successes)
model = pymc.Model([a, b, true_rates, observed_values])
mcmc = pymc.MCMC(model)
 
# Generate 1,000,000 samples, and throw out the first 500,000
mcmc.sample(1000000, 500000)



# plot posterior distributions
labels = ["a","b","c","d","e"]
for i in range(0,5):
    sns.kdeplot(mcmc.trace('true_rates')[:][:,i]
        ,label="Website " + labels[i].upper())



# Compare any posterior distributions ie. A and C
diff_CA = mcmc.trace('true_rates')[:][:,2] - mcmc.trace('true_rates')[:][:,0]
sns.kdeplot(diff_CA, shade = True, label = "Difference site C - site A")
plt.axvline(0.0, color = 'black')

print "Probability that website A gets MORE sign-ups than website C: %0.3f" % (diff_CA < 0).mean()
print "Probability that website A gets LESS sign-ups than website C: %0.3f" % (diff_CA > 0).mean()


# Compare bernouli, and other stuff
#TODO

#sns.kdeplot(siteA_distribution, shade = True, label = "Bernoulli Model")
sns.kdeplot(mcmc.trace('true_rates')[:][:,0], shade = True, label = "Hierachical Beta")
plt.axvline(0.032, color = 'black')









