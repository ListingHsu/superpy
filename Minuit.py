#########################################################################
#                                                                       #
# M i n u i t                      
#                                                                       #
#########################################################################

# Minimise the likelihood with minuit.

# Internal packages.
import Debug as DB # Debug options.
import Likelihood # Constraints and likelihood functions.

# External packages.
from iminuit import Minuit # Easy to install via sudo pip install iminuit

# Wrapper for our likelihood function so that arguments are individual parameters, rather than a list.
def chisquared(a0, alphas, invalpha, m0, m12, mb, mt, signmu, tanb):
	""" Wrapper for likelihood.
	Arguments:
	a0, alphas, invalpha, m0, m12, mb, mt, signmu, tanb - nine elements of cube.
	"""
	ndim=9 # Model parameters - 9 for CMSSM.
	nparams=100 # Approximate number of items in cube.
	cube = [0] * nparams # Initialise cube as empty list.
	# Copy arguments to cube.
	for i, arg in enumerate([a0, alphas, invalpha, m0, m12, mb, mt, signmu, tanb]):
		cube[i] = arg
	chisquared = -2 * Likelihood.myloglike(cube, ndim, nparams) # ndim and nparams are irrelavant.
	return chisquared

# Setup initial values, errors etc.
kwdarg=dict(
a0 = -3000,
error_a0 = 100,
alphas = 1.18400000e-01, 
fix_alphas = True, 
invalpha = 1.27944000e+02,
fix_invalpha = True,
m0 = 400,
error_m0 = 100,
m12 = 900,
error_m12 = 100,
mb = 4.18000000e+00, 
fix_mb = True, 
mt = 1.74500000e+02,
fix_mt = True, 
signmu = 1,
fix_signmu = True, 
tanb = 11,
error_tanb = 3,
errordef=1
)

# Set Minuit likelihood function.
m = Minuit(chisquared, **kwdarg)

# Run migrad.
m.migrad()
print m.values 
print m.errors

#########################################################################
