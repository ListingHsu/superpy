#########################################################################
#                                                                       #
#    P r i o r s                                                        #
#    Priors are set here.                                               #
#                                                                       #
#########################################################################

# External packages.
import math
import scipy
from scipy import special
import numpy as NP 
import Cube

def myprior(cube, ndim, nparams):
    """ MultiNest callback function. Sets the model parameters
    from the unit hypercube.
    Arguments: 
    cube -- Unit hypercube from which model parameters are mapped.
    ndim -- Number of model paramers.
    nparams -- Total number of parameters in the cube .

    Returns:

    """        
    # Set-up the paramters - CMSSM model.
    Model = CMSSMModelTracker()
    
    # Set the model parameters from the cube.
    Model.SetParams(cube)
    
    # Copy them to the cube so that they are printed, in alphabetical order.
    for name in sorted(Model.param.keys(), key=str.lower):
        Cube.AddCube(cube, Model.param[name].value, Cube.label, name )
        
    # Print-out cube model parameters for debugging.
    print '*****************************************************'
    print 'Parameters:'
    for i in range(Cube.AddCube.count()+1): # Count begins at 0 - need +1.
        print Cube.label[i], cube[i]


#########################################################################

# Model class - this is where everything is stored.
# This class contains all the parameters for the model,
# and the functions to evalulate them.

class CMSSMModelTracker:
    """ Contains CMSSM model parameters, priors and functions to 
    evaluate the parameters. """
    def __init__(self):
        """ Sets-up the model. """
        # Holds model's parameters.
        self.param = {}
        
        # Set the priors for each parameter. NB Gaussian priors are in a way 
        # infinite, so you don't need to specify upper and lower bounds.
        # NB If you use a log parameter, be sure its always strictly > 0.
        # The parameters are in GeV.
        self.param['m0'] = LogParameter(100, 4000)    
        self.param['m12'] = LogParameter(100, 2000)    
        self.param['a0'] = LinearParameter(-4000, 4000)
        self.param['tanbeta'] = LinearParameter( 3, 62)    
        self.param['signmu'] = FixedParameter(1) 
        # Nusisance parameters from PDG 09/12.       
        self.param['mb'] = GaussParameter(4.18, 0.03)  
        self.param['mt'] = GaussParameter(173.5, 1.0) 
        self.param['alphas'] = GaussParameter(0.1184, 0.0007)    
        self.param['invalpha'] = GaussParameter(127.944, 0.014)
            
    def SetParams(self, x):    
        """ Sets the parameters from the unit hypercube.
        Arguments:
        x -- The whole unit hypercube vector.
        
        Returns: 

        """
        for i, name in enumerate(self.param.keys()):
            self.param[name].SetValue(x[i])

#########################################################################

# These classes are all the types of prior one might use, they all have a 
# SetValue function, which sets the value of parameter from MultiNest's unit
# hypercube. i.e. all priors are mapped from a Uniform(0,1) distribution.
        
@Cube.memoize
class LogParameter:
    """ A parameter with a log prior. """
    def __init__(self,min, max):
        """ Initializes a parameter with a log prior.
        Arguments:
        min --  Minimum of prior.
        max --  Maximum of prior.

        Returns:

        """
        self.minimum = min
        self.maximum = max
        self.value = 0
        self.arg = self.args
     
    def SetValue(self, x):
        """ Calculates value of parameter with log prior from unit
        hypercube. 
        Arguments:
        x -- One element of unit hypercube.

        Returns:

        """
        # Log the ranges, map from 0-1 to min-max in log space, 
        # then exponentiate.
        self.value = math.pow(10, math.log10(self.minimum) + x *\
                     (math.log10(self.maximum) -\

                     math.log10(self.minimum)))        

@Cube.memoize
class LinearParameter:
    """ A parameter with a linear prior. """
    def __init__(self, min, max):
        """ Initializes a parameter with a linear prior .
        Arguments:
        min --  Minimum of prior.
        max --  Maximum of prior.

        Returns:

        """
        self.minimum = min
        self.maximum = max
        self.value = 0
        self.arg = self.args
        
    def SetValue(self, x):
        """ Calculates value of parameter with a linear prior from unit
        hypercube.
        Arguments:
        x -- One element of unit hypercube.

        Returns:

        """
        # Map from 0-1 to min-max.
        self.value = self.minimum + x * (self.maximum - self.minimum)

@Cube.memoize
class FixedParameter:
    """ A parameter with a fixed value. """
    def __init__(self, fixed):
        """ Initializes a parameter with a fixed value.
        You might, for example, want to fix sgn mu in the CMSSM.
        Arguments:
        fixed -- Fixed value of parameters.

        Returns:

        """
        self.fix = fixed
        self.value = 0
        self.arg = self.args
        
    def SetValue(self, x):
        """ Sets value of parameter with a fixed prior, ignore unit 
        hypercube.
        Arguments:
        x -- One element of unit hypercube, ignored.

        Returns:

        """
        # NB that although x isn't used, it should stil be here
        # so that this class can be used like the others.
        self.value = self.fix
        self.arg = self.args

@Cube.memoize
class SignParameter:
    """ A parameter that is either +/- 1 """
    def __init__(self):
        """ Initializes a parameter that is either +/- 1.
        For example, sign mu in the CMSSM.
        Arguments:

        Returns:

        """
        self.value = 0
        self.arg = self.args
        
    def SetValue(self, x):
        """ Sets value of parameter to +/- 1, with equal probability.
        Arguments:
        x -- One element of unit hypercube.

        Returns:

        """
        # You could change this to favour a particular sign.
        if x > 0.5:
            self.value = +1
        else:
            self.value = -1
@Cube.memoize          
class GaussParameter:
    """ A parameter with a Gaussian prior """
    def __init__(self, mu, sigma):
        """ Initializes a parameter with a Gaussian prior.
        Arguments:
        mu -- Mean of Gaussian.
        sigma -- Variance of Gaussian.

        Returns:

        """
        self.mu = mu
        self.sigma = sigma
        self.value = 0
        self.arg = self.args
                
    def SetValue(self, x):
        """ Sets value of parameter with a Gaussian prior from unit
        hypercube.
        Arguments:
        x -- One element of unit hypercube.

        Returns:

        """    
        # Map from 0-1 to a Gaussian! erfcinv is a the inverse of the
        # complementary Gaussian error function.
        self.value = self.mu + self.sigma * math.sqrt(2) *\
                     scipy.special.erfcinv(2 * (1 - x))
