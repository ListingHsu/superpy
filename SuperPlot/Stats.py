#########################################################################
#                                                                       #
#    S t a t s                                                          #
#                                                                       #
#########################################################################

import numpy as NP

# Useful statistical functions.

def PosteriorMean(posterior, param):
    """ Calculate the posterior mean.
    posterior -- Data column of posterior weight.
    param -- Data column of parameter.
    """        
    # Calculate posterior mean - dot product weights with parameter 
    # values and normalize.
    postmean = NP.dot(posterior, param) / \
    sum(posterior)
    return postmean

def BestFit(chisq, param):
    """ Calculate the best-fit. 
    chisq -- Data column of chi-squared.
    param -- Data column of parameter.
    """
    # Calculate the best-fit - find the point that corresponds 
    # to the smallest chi2.
    bestfit = param[chisq.argmin()]
    return bestfit 

def PValue(chisq, dof):
    """ Calculate the pvalue. 
    chisq -- Data column of chi-squared.
    dof -- Number of degrees of freedom.
    """
    from scipy import stats
    # Find the associated p-value. The survival function, sf,
    # is 1 - the CDF.
    pvalue = stats.chi2.sf(chisq.min(), dof)
    return pvalue

