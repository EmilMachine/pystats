# https://www.quora.com/How-can-I-do-an-A-B-test-in-Python

import scipy
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


# Independent T-test 
# - test the means between 2 means (normal distribution)
# - can only be applied to interval/ratio§
# - assumes equal variation (unless using Welsh t-test)
# 
# §: (http://www.mymarketresearchmethods.com/types-of-data-nominal-ordinal-interval-ratio/)
# - norminal (categorical unordered), 
# - ordinal (categorical ordered)
# - interval (numeric, but no abs zero (ratios do not make sense))
# - ratio (numeric, with abs zero)


## Needs to test for normality, see test_for_normality.py

### distributions
np.random.seed(1)
n = 1000
a = np.random.normal(5,1,n)
a2 = np.random.normal(5,2,n)
a3 = np.random.normal(5,5,n)

b = np.random.normal(5,1,n)
b2 = np.random.normal(4.5,1,n)
b3 = np.random.normal(4.4,1,n)
c = np.random.lognormal(1.6,0.2,n)
d = np.random.lognormal(1.6,0.3,n)
e = np.random.exponential(1,n)

plt.figure(0)
sns.kdeplot(a,shade=True)
sns.kdeplot(a2,shade=True)
sns.kdeplot(a3,shade=True)



plt.figure(1)
sns.kdeplot(a,shade=True)
sns.kdeplot(b,shade=True)
sns.kdeplot(b2,shade=True)
sns.kdeplot(b3,shade=True)

plt.figure(2)
sns.kdeplot(a,shade=True)
sns.kdeplot(b,shade=True)
sns.kdeplot(c,shade=True)
sns.kdeplot(d,shade=True)
sns.kdeplot(e,shade=True)



### TESTS
# t test
# f test
# z test?


scipy.stats.ttest_1samp(a,5) 


#  Bartlett test 
# (or Levene test) 




# let us try with the usual p = 0.05

### test for a given mean
scipy.stats.ttest_1samp(a,5) # p = .21  not sig
scipy.stats.ttest_1samp(a,4.7) # p = 2.7E-36  sig

### Test vs different polulation
scipy.stats.ttest_ind(a,b) #  p=0.98, not significatnt
scipy.stats.ttest_ind(a,b2) # p=1.4, not significant

# Welsh students t-test
# in practice little difference (?)
scipy.stats.ttest_ind(a,a2)                 # p = 0.82636
scipy.stats.ttest_ind(a,a2,equal_var=False) # p = 0.82637

### interpretate results
# p-result significance for null hypothesis
# e.g. if p<0.05 discard null (identical mean) with 1/20 security
# 

# Margin of error (confidence interval...)






