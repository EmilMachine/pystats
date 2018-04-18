
### sources
#http://www.raosoft.com/samplesize.html
#https://www.isixsigma.com/tools-templates/sampling-data/how-determine-sample-size-determining-sample-size/

# https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
###
# E = z_(a/2) * sigma / (sqrt(n)

# n = [z_(a/2) sigma / E ]**2


from statsmodels.stats.proportion import proportion_confint
# http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportion_confint.html

# confidence interval for binomial proportions
count = 10 # successs
nobs = 1000 # trials
alpha = 0.05 # significance
method = 'normal' # type of approx
proportion_confint(count, nobs, alpha=alpha, method=method)

### Alternatives written here:
# https://stackoverflow.com/questions/13059011/is-there-any-python-function-library-for-calculate-binomial-confidence-intervals


### Complete A/B test for binominal data. 

#test data, n_a,success_a,n_b,success_b
n_a,s_a,n_b,s_b = [1000,400,1000,450]

## calculate margin of error 
# decide 
alpha = 0.05
method = 'normal'

conf_a = proportion_confint(s_a, n_a, alpha=alpha, method=method)
conf_b = proportion_confint(s_b, n_b, alpha=alpha, method=method)

# Calculate p value that conf_a and conf_b is diffferent
import scipy.stats as sts
import numpy as np
data_a = (np.random.rand(n_a)>(float(s_a)/n_a)).astype(int)
data_b = (np.random.rand(n_b)>(float(s_b)/n_b)).astype(int)

# (t-test does not assume known variance)

# two sample t_tests
t_stats = sts.ttest_ind(data_a,data_b,equal_var=True, nan_policy='propagate')


### z-tests (assume known variance)

# see also https://stats.stackexchange.com/questions/124096/two-samples-z-test-in-python
#http://www.statsmodels.org/dev/generated/statsmodels.stats.proportion.proportions_ztest.html
from statsmodels.stats.proportion import proportions_ztest


counts = np.array([s_a, s_b])
nobs = np.array([n_a, n_b])
# z_tests
z_stats_two = proportions_ztest(counts, nobs,alternative="two-sided")
z_stats_two


# Directional
# smaller: h_0 = prop > value. e.g a>b, alternative is a<b
z_stats_small = proportions_ztest(counts, nobs,alternative="smaller")
z_stats_small


# Note this is a two sided t_test, e.g. only check means are different
### to get direction (one tailed t_tests), divide p with 2, (and look sign of statistics)





# https://docs.scipy.org/doc/scipy/reference/stats.html
## TOOD reverse  calculate sample size
