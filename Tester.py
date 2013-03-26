#########################################################################
#                                                                       #
# T e s t e r                          
#                                                                       #
#########################################################################

# Tests an input point, run with 
#	python Tester.py a0, alphas, invalpha, m0, m12, mb, mt, signmu, tanb

# Internal packages.
import Debug as DB # Debug options.
import Likelihood # Constraints and likelihood functions.

# External packages.
import sys

# Initialise the cube.
cols = 100
nparams = cols - 2 # Subract 2 for chi-squared and posterior weight.
ndim = 9 # For CMSSM.

# Read the input parameters into the cube.
cube = [0] * nparams # Initialise cube to an empty list.
if len(sys.argv) != ndim + 1: # Plust one to ignore first argument is name of file, e.g. python Tester.py arg1 arg2 etc
	sys.exit('You should supply a0, alphas, invalpha, m0, m12, mb, mt, signmu, tanb')

for i in range(len(sys.argv)):
	if i == 0: continue # Ignore name of file.
	cube[i-1] = float(sys.argv[i]) # Minus one to ignore name of file, which is zeroth argument, and convert string to float.

# Call likelihood function.
loglike = Likelihood.myloglike(cube, ndim, nparams)

#########################################################################
