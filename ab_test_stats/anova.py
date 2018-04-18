
### ANOVA
# Analysis of variance
#
# Basis idea: 
# You have 3 or more groups, and want to check if they have different mean
# - Calculate variation within groups
# - Compare to variation between groups
# - (take into account degrees of freedom)
# - (number of groups-1),(total_number_of_observation-number_of_groups)
# - (Ng-1),(No-Ng)

#http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html
# https://www.youtube.com/watch?v=-yQb_ZJnFXw
# you have j groups with i obs
# (SS stands for sum of squares, ij means you treat everything as coming from same distribution)
# SSW Within group  SUM_j( SUM_i((obs_i-avg_j)**2)  
# SST total  SUM_ji((obs_ji-avg_ji)**2) (SST) 
# SSB between groups i * SUM_j(avg_ji - avg_j)**2

# B=SSB/(j-1)  # j-1 is degrees of freedom
# W=SSW/(j*i-j)  # j*i-j is degrees of freedom
# B/W with f( (j-1) , /(j*i-j) )


# see also
# http://www.randalolson.com/2012/08/06/statistical-analysis-made-easy-in-python/


import scipy
a = scipy.stats.norm.rvs(size = 20)
b =scipy.stats.norm.rvs(size = 20,loc=1)
c = scipy.stats.norm.rvs(size= 20,scale=2)

# One way anova - Null hypotheis : all dist have same mean

scipy.stats.f_oneway(a,b,c)
scipy.stats.f_oneway(a,a,a)
scipy.stats.f_oneway(a,a,c,c)

## Two way anova, calc for prop for each factor + product of factors.
# e.g. see:
# https://www.marsja.se/three-ways-to-carry-out-2-way-anova-with-python/



