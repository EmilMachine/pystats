### TEST FOR NORMALITY 

# 1. state null (H0) and alternative hypothesis (H1)
# 2. Choose level of significance (alpha)
# 3. Find critical values
# 4. Find test statistics
# 5. Draw conclusion (can you reject null hypothesis)

# 1: H0 the distribution is normal, H1 distribution is not normal.



# make sure to normalize before passing through the test.
# data
# mu = np.mean(data)
# sigma = np.std(data)
# data_norm=(data-mu)/sigma

d_uniform = scipy.stats.uniform.rvs(size = 100)
d_gauss = scipy.stats.norm.rvs(size = 100)

# In order to check for normality and equal variances, 
#  Kolmogorov Smirnov test 
## KS test:
### https://stats.stackexchange.com/questions/57885/how-to-interpret-p-value-of-kolmogorov-smirnov-test-python
### Max diff *supremum* between CDFs (cumuliative distribution function)
### of two distributions / or dist and data

### Normality test with KS, is to do median and std after distribution but SW is better
scipy.stats.kstest(d_gauss,"norm")   # p=0.37
scipy.stats.kstest(d_uniform,"norm") # p=0


# (or the Shapiro Wilk test) Better for normality test
## quantile, quantile plots slope, should be around the variance (if normal distributed)
# problem with many equal values
# hard with small n
# hard to reject small when n large
# !(too sensitive for normal test for anova / t-tests) 
# Source: https://www.youtube.com/watch?v=dRAqSsgkCUc

scipy.stats.shapiro(d_gauss)
#(0.9979180097579956, 0.24998418986797333) 
#(can not reject null hypothesis)
scipy.stats.shapiro(d_uniform)
# can reject null (ie. distribution is not normal)
# (0.944701611995697, 0.000377564632799476


### chi-squared test
# Test statistic chi-square: 
# SUM( (M-E)**2/E ) where M is measured and E is expected
# degrees of freedom is number of possible outcomes -1
# need to find test statistics depend on level of significance (alpha) and degrees of freedom 
##
# for curve fitting chi square is 
# (1/dof) * SUM(r_i/siqma_i) 
# where dof is degrees of freedom
#, r is residuals
# sigma is the std of that datapoint 



scipy.stats.normaltest(d_gauss)
# NormaltestResult(statistic=0.14418853940217, pvalue=0.93044317907638741)

scipy.stats.normaltest(d_uniform)
#NormaltestResult(statistic=40.272395038463387, pvalue=1.7987074393719047e-09)



