#########################################################################
#                                                                       #
#    L i k e l i h o o d                                                #
#                                                                       #
#########################################################################

# External packages.
import os
import math
import scipy
import subprocess
import pyslha
import tempfile
import numpy as NP 

# Internal packages.
import Priors
import Cube

# Declare the constraints here.
     
def myloglike(cube, ndim, nparams):
    """ MultiNest callback function. 
    Calculate the model's predictions (by calling external programs), 
    saves the extra parameters, and returns log likelihood to Multinest.
    Arguments: 
    cube -- Unit hypercube from which model parameters are mapped.
    ndim -- Number of model paramers.
    nparams -- Total number of parameters in the cube.
    
    Returns: The total log likelihood for the model parameter. 
    point under consideration.

    """ 
    # Set up constraints class.
    Constraints = CMSSMConstraintTracker()

    # Copy cube to constraints, so it can work out predictions etc.
    for i, name in enumerate(sorted(Priors.CMSSMModelTracker().param.keys(), key=str.lower)):
        Constraints.param[name] = cube[i]  
    
    # Set predictions and loglikes.
    Constraints.SetPredictions()
    Constraints.SetLogLike()
    
    # Copy constraints to cube.
    for name in sorted(Constraints.constraint.keys(), key=str.lower):
        Cube.AddCube(cube, Constraints.constraint[name].theory, Cube.label, name )
    
    # Copy associated chi2s to cube. Better to print chi2 than loglike, 
    # beceause MultiNest prints chi2 and they can be treated in the 
    # same way when plotting.
    for name in sorted(Constraints.constraint.keys(), key=str.lower):
        Cube.AddCube(cube, -2 * Constraints.constraint[name].loglike, Cube.label, 'chi2:'+name)
    
    # Copy SLHA masses to the cube.
    for key in Constraints.masses:
        Cube.AddCube(cube, Constraints.masses[key], Cube.label, 'Mass:'+str(key))
                                                                                                                                      
    # Print-out cube for debugging.
    print 'Predictions:'        
    for label, param in zip(Cube.label.itervalues(), cube):
        print label, param
    print 'Total loglike', Constraints.loglike

    # Start cube count from 0 again.
    Cube.AddCube.reset() 
    
    # Print an info file for the cube.
    Cube.PrintInfo() 

    # Return the loglikelihood to MultiNest.
    return  Constraints.loglike
    

#########################################################################

# This class evalulates likelihoods and the model's predictions etc.

class CMSSMConstraintTracker:
    """ Contains CMSSM constraints and functions to 
    evaluate the model's predictions. """
    def __init__(self):
        """ Sets-up the model. """
        # Holds model's parameters.
        self.param = {}
        # Holds constraint information.
        self.constraint = {}
        # Whether the model has an acceptable mass spectrum, EWSB etc.
        self.physical = True
        # The total loglike associated with model.
        self.loglike = -1e101
        # SLHA masses in column.
        self.masses = []
        
        # You set the constraint values here. You must also make sure that
        # the number of constraints matches that in your model, and that you have
        # computed all the relevant theoretical values.

        # LHC 2011 Higgs constraints - from SoftSUSY.                          
        self.constraint['Higgs'] = GaussConstraint(125, 2, 2)    
        
        # Relic density of chi1 - from micrOMEGAs. 
        self.constraint['oh2'] = GaussConstraint(0.112, 0.0056, 0.0112)
        
        # Anomalous magnetic moment of muon - from micrOMEGAs.       
        self.constraint['gm2'] = GaussConstraint(28.7e-10, 8e-10, 1e-10)
        
        # b -> s gamma - from SuperIso. 
        self.constraint['bsg'] = GaussConstraint(3.6e-4, 0.23e-4, 0.21e-4)
        
        # Bs -> mu mu - from micrOMEGAs. 
        self.constraint['bsmumu'] = UpperConstraintFractionalTau(4.5e-9, 0.14)                    
        
        # Ratio b -> tau nu / SM - from micrOMEGAs.  
        self.constraint['btaunu'] = GaussConstraint(0.93, 0.41, 0)
        
        # sigma SI p - from micrOMEGAs.  
        self.constraint['sigsip'] = DummyConstraint()
        
        # Precision MW - from FeynHiggs. 
        self.constraint['mw'] = GaussConstraint(80.399, 0.023, 0.015)
        
        # Precision sin eff theta - from FeynHiggs. 
        self.constraint['sineff'] = GaussConstraint(0.23116, 0.00013, 15e-5)
        
        # delta MBs - from FeynHiggs. 
        self.constraint['deltaMb'] = GaussConstraint(17.77, 0.12, 2.4)  
        
        # sigma * BR(h gamma gamma) - from FeynHiggs. 
        self.constraint['hgg'] = DummyConstraint()
        
        # R_hZZ -ratio of ghZZ SUSY to SM - from FeynHiggs. 
        self.constraint['hzz'] = DummyConstraint()                                                                  
        
        # The constraint from LHC CMS alphaT 1/fb on the m0-m12 plane.
        # Fine to use relative path here - converted to full path later.
        self.constraint['LHC'] = InterpolateLowerConstraint('alphaT_1invfb_m0m12.dat', 10)   
        
        # Nusiance parameters - best not to apply these if you use Gaussian priors.
        self.constraint['mb'] = DummyConstraint()
        self.constraint['mt'] = DummyConstraint()
        self.constraint['alphas'] = DummyConstraint()
        self.constraint['invalpha'] = DummyConstraint()
        
    def SetPredictions(self): 
        """ Run the auxilliary programs, if the point is physical.
        """
        self.spectrum()
        self.readslha() # Regardless of whether physical.
        if self.physical: self.feynhiggs()
        if self.physical: self.micromegas()
        if self.physical: self.superiso()

        # Set the (m0,m12) arguments - x will be m0, y will be m12.
        self.constraint['LHC'].theoryx = self.param['m0']
        self.constraint['LHC'].theoryy = self.param['m12']
      
        # Set the nuisance parameters here.
        self.constraint['mt'].theory = self.param['mt']
        self.constraint['mb'].theory = self.param['mb']
        self.constraint['alphas'].theory = self.param['alphas']
        self.constraint['invalpha'].theory = self.param['invalpha']
    
    def spectrum(self): 
        """Calls SoftSUSY to obtain predictions 
        for model.
        """ 
        # Set up SLHA input file.
        SLHAIN = tempfile.NamedTemporaryFile(delete=False)
        # Pass information in SLHA format. NB that you could easily add more
        # parameters to the EXTPAR section, to relax the CMSSM.
        SLHAIN.write("""
Block MODSEL                    # Select model
 1   1                          # sugra
Block SMINPUTS                  # Standard Model inputs
 1   %s                         # alpha^(-1) SM MSbar(MZ)
 2   1.16637000e-05             # G_Fermi
 3   %s                         # alpha_s(MZ) SM MSbar
 4   9.11876000e+01             # MZ(pole)
 5   %s                         # mb(mb) SM MSbar
 6   %s                         # mtop(pole)
 7   1.77700000e+00             # mtau(pole)
Block MINPAR    # Input parameters
 1   %s                         # m0
 2   %s                         # m12
 3   %s                         # tanb
 4   %s                         # sign(mu)
 5   %s                         # A0
Block SOFTSUSY  # SOFTSUSY-specific parameters
 1   1.000000000e-03            # Numerical precision
 2   0.000000000e+00            # Quark mixing parameter
 5   1.000000000e+00            # Include 2-loop 
#Block EXTPAR                   # Non-universal terms here""" % (
        str(self.param['invalpha']), str(self.param['alphas']), str(self.param['mb']), str(self.param['mt']),\
        str(self.param['m0']), str(self.param['m12']), str(self.param['tanbeta']), str(self.param['signmu']),\
        str(self.param['a0'])))

        # Set SoftSUSY command - model independent SLHA.
        SoftSUSY  = ['./softsusy-*/softpoint.x leshouches <' + 
                 SLHAIN.name]
        # Now close the SLHA input file.
        SLHAIN.close()  
                     
        # Dump sterr messages to a scratch file. SoftSUSY uses sterr
        # for messages (not error messages) which can mess up SLHA file.
        ERROR = tempfile.NamedTemporaryFile()
        
        # Unfortunately, best not to pipe SLHA files, as it can exceed
        # the 64kb limit. So use scratch instead, but we don't want to 
        # delete it on close.
        self.SLHA = tempfile.NamedTemporaryFile(delete=False)
        
        # Call SoftSUSY, with the above command. 
        # Don't use Popen - you will have to wait for it to complete,
        # and you end up with half an SLHA file etc.
        # Need shell=True for the < direct.
        try:
                subprocess.call(SoftSUSY, stderr=ERROR.fileno(),
                stdout=self.SLHA.fileno(), shell=True)       
        except:
                self.physical = False
                print 'Trouble in SoftSUSY.'
        else:             
                # Check for an instance of invalid or problem in the SLHA.
                # They will appear if any physicality problems with model,
                # or if something other than chi1 is LSP.
                for line in open(self.SLHA.name):
                    if 'problem' in line or 'invalid' in line or 'Warning' in line:
                        self.physical = False
                        print 'Caught unphysical point SLHA:'
                        print line
                        break 
                
                # Now close the files.
                ERROR.close()
                self.SLHA.close()       
 
    def readslha(self):
        """ Read an SLHA file.
        """
        blocks={}
        try:
            blocks, decays = pyslha.readSLHAFile(self.SLHA.name)
        except:
            # With expected running, shouldn't get any problems. But best
            # to be defensive. A missing mass block would cause an 
            # exception, but e.g. stau LSP would not.
            self.physical = False
            print 'Caught trouble in the SLHA file.'
            
            # Populate mass blocks with 0.
            blocks['MASS'] = pyslha.Block('MASS')
            for pid in [24,25,35,36,37,
                        1000021,1000022,1000023,1000024,1000025,
                        1000035,1000037,1000011,1000013,1000015,
                        2000011,2000013,2000015,1000012,1000014,
                        1000016,1000001,1000003,1000005,2000001,
                        2000003,2000005,1000002,1000004,1000006,
                        2000002,2000004,2000006]:
                blocks['MASS'].add_entry((pid,0)) 
                    
        # Pick out the Higgs mass for my Higgs constraints.
        self.constraint['Higgs'].theory = blocks['MASS'].entries[25]
    
        # Save the mass block.
        self.masses = blocks['MASS'].entries

    def micromegas(self):
        """Calls micrOMEGAs to obtain predictions 
        for model.
        """   
        # microMEGAs command.
        MO = ['./main', self.SLHA.name]    
        # Set up temp files.
        ERROR = tempfile.NamedTemporaryFile()
        # Pipe output straight into micrOMEGAs - no files.
        # This should be fine - there is a a 64kb limit which we
        # shouldn't exceed.
        try:
            micromegas = subprocess.Popen(
                MO, stdout=subprocess.PIPE, 
                stderr=ERROR,
                cwd=os.path.abspath('./micromegas_2.4.5/MSSM'))
        except:
            self.physical = False
            print 'Trouble in microMEGAs.'
        else:
            # Read pipe - use readlines to keep line breaks, rather than read.
            micromegas = micromegas.stdout.readlines()
            # Read the micromegas output into the constraints.
            for line in micromegas:
                # Check for errors.
                if 'error' in line:
                    print 'Caught unphysical point MO:'
                    print line
                    physical = False
                    break               
                if line.startswith('Xf='):
                    # This line needs to be split on Omega=, because line
                    # contrains Xf too.
                    self.constraint['oh2'].theory = float(line.split('Omega=')[-1])
                if line.startswith('gmuon'):
                    self.constraint['gm2'].theory = float(line.split('=')[-1])  
                if line.startswith('bsgnlo'):
                    # This line needs to be split twice, to remove SM info
                    # e.g. bsgnlo=3.57E-04 ( SM 3.26E-04 ). 
                    self.constraint['bsg'].theory = float(line.split('(')[0].split('=')[-1])
                if line.startswith('bsmumu'):         
                    self.constraint['bsmumu'].theory = float(line.split('=')[-1])   
                if line.startswith('btaunu'):          
                    self.constraint['btaunu'].theory = float(line.split('=')[-1])
                # NB leading space.
                if line.startswith(' proton  SI'):
                    # This line needs to be split twice, because line
                    # contrains SD too.
                    self.constraint['sigsip'].theory = float(line.split(' proton  SI')[-1].split('SD')[0])
        # Close temporary file - this will delete it.        
        ERROR.close()    
        
    def superiso(self):
        """Calls SuperIso to obtain predictions 
        for model.
        Arguments:
        """  
        SI = ['./slha.x', self.SLHA.name]    
        # Set up temp files.
        ERROR = tempfile.NamedTemporaryFile()
        # Pipe output straight into SuperISO - no files.
        # This should be fine - there is a a 64kb limit which we
        # shouldn't exceed.
        try:
            superiso =  subprocess.Popen(
                SI, stdout=subprocess.PIPE, 
                stderr=ERROR,
                cwd=os.path.abspath('./superiso_v3.3/'))
        except:
            self.physical = False
            print 'Trouble in SuperISO.'
        else:
            # Read pipe - use readlines to keep line breaks, rather than read.
            superiso = superiso.stdout.readlines()
            # Read the SuperISO output into the constraints.
            for line in superiso:             
                if line.startswith('BR(b->s gamma)'):       
                    self.constraint['bsg'].theory = float(line.split(')')[-1])   
        # Close temporary file - this will delete it.        
        ERROR.close()            
        
    def feynhiggs(self):
        """Calls FeynHiggs to obtain predictions 
        for model.
        """    
        FH = ['./SuperPyFH', self.SLHA.name]  
        # Set up temp files.
        ERROR = tempfile.NamedTemporaryFile()
        # Pipe output straight into FH - no files.
        # This should be fine - there is a a 64kb limit which we
        # shouldn't exceed.
        try:
            feynhiggs =  subprocess.Popen(
                FH, stdout=subprocess.PIPE, 
                stderr=ERROR,
                cwd=os.path.abspath('./FeynHiggs-2.9.4'))
        except:
           self.physical = False
           print 'Trouble in FeynHiggs.'
        else:
            # Read pipe - use readlines to keep line breaks, rather than read.
            feynhiggs = feynhiggs.stdout.readlines()
            # Read the FH output into the constraints. NB leading whitespace.
            for line in feynhiggs:
                # Check for errors.
                if 'error' in line:
                    print 'Caught unphysical point FH:'
                    print line
                    self.physical = False
                    break 
                if line.startswith(' MWMSSM'): 
                    self.constraint['mw'].theory = float(line.split('=')[-1]) 
                if line.startswith(' SW2MSSM'):
                    self.constraint['sineff'].theory = float(line.split('=')[-1]) 
                if line.startswith(' deltaMsMSSM'):        
                    self.constraint['deltaMb'].theory = float(line.split('=')[-1]) 
                if line.startswith(' sigma * BR(h->gamma gamma)'):        
                    self.constraint['hgg'].theory = float(line.split('=')[-1]) 
                if line.startswith(' R_ZZh MSSM/SM'):        
                    self.constraint['hzz'].theory = float(line.split('=')[-1]) 

        # Close temporary file - this will delete it.        
        ERROR.close()       
            
    
    def SetLogLike(self):    
        """ Loops over the constraints, calculates each log likelihood 
        and sums the log likelihoods.
        """
        if self.physical:
            # Set the loglikelhoods from the constraints's SetLogLike functions.
            self.loglike = 0
            for name in self.constraint.keys():
                self.loglike = self.loglike + self.constraint[name].SetLogLike()
        else:
            # If the point is unphysical, all loglikelihoods = biggest possible.
            # Logzero is -1e101.
            for name in self.constraint.keys():
                self.constraint[name].loglike = -1e101
            self.loglike = -1e101    
    
#########################################################################

# These classes are various likelihoods for experimental measurements.
# I have included Gaussians, error functions etc. They all have a SetLogLike
# function, from which the loglikelhood is calculated.

@Cube.memoize
class GaussConstraint:
    """ A Gaussian likelihood constraint. """
    def __init__(self, mu, sigma, tau=0):
        """ Initializes a Gaussian constraint.
        Arguments:
        mu --    Experimental mean of measurement.
        sigma -- Experimental variance of measurement.
        tau --   Theoretical error in calculation.

        Returns:

        """
        self.mu = mu
        self.sigma = sigma 
        self.tau = tau
        self.theory = 0
        self.loglike = -1e101
        self.arg = self.args
                
    def SetLogLike(self):
        """ Caclulate Gaussian likelihood from model's predictions and 
        data.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        self.loglike = - math.pow(self.mu - self.theory,2) /\
                       (2 * (math.pow(self.sigma,2) +\
                       math.pow(self.tau,2)))
        return self.loglike

@Cube.memoize
class GaussConstraintFractionalTau:
    """ A Gaussian likelihood constraint, with a fractional
    theoretical error.
    """
    def __init__(self, mu, sigma, tau):
        """ Initializes a Gaussian constraint, with a fractional 
        theoretical error.
        Arguments:
        mu --    Experimental mean of measurement.
        sigma -- Experimental variance of measurement.
        tau --   Fractional theoretical error in calculation.

        Returns:

        """
        self.mu = mu
        self.sigma = sigma 
        self.tau = tau
        self.theory = 0
        self.loglike = -1e101
        self.arg = self.args
                
    def SetLogLike(self):
        """ Caclulates Gaussian likelihood from model's predictions and 
        data.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # NB that here theory error = tau * theoretical value.
        self.loglike = - math.pow(self.mu - self.theory,2) /\
                       (2 * (math.pow(self.sigma,2) +\
                       math.pow(self.tau * self.theory,2)))
        return self.loglike

@Cube.memoize
class UpperConstraint:
    """ Upper bound, Gaussian error function constraint. """
    def __init__(self, limit, tau):
        """ Initializes an upper bound constraint .
        Arguments:
        limit -- Upper bound of measurement.
        tau --   Theoretical error in calculation.

        Returns:

        """
        self.limit = limit
        self.tau = tau
        self.theory = 0
        self.loglike = -1e101
        self.arg = self.args
                
    def SetLogLike(self):
        """ Calcualte upper bound likelihood with Gaussian error 
        function from model's predictions and data.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # NB that erfc is a complementary error function.
        try:
            self.loglike = math.log(0.5 * scipy.special.erfc((self.theory -\
                           self.limit) /\
                           (math.sqrt(2) * self.tau)))
        # Sometimes we are trying to take log zero.
        except ValueError:
            self.loglike = -1e101
        return self.loglike

@Cube.memoize       
class UpperConstraintFractionalTau:
    """ Upper bound, Gaussian error function constraint, with fractional 
    theory error.
    """
    def __init__(self, limit, tau):
        """ Initializes an upper bound constraint .
        Arguments:
        limit -- Upper bound of measurement.
        tau --   Theoretical error in calculation.

        Returns:

        """
        self.limit = limit
        self.tau = tau
        self.theory = 0
        self.loglike = -1e101
        self.arg = self.args
                
    def SetLogLike(self):
        """ Calcualte upper bound likelihood with Gaussian error 
        function from model's predictions and data.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # NB that erfc is a complementary error function.
        # NB that here theory error = tau * theoretical value.
        try:
            self.loglike = math.log(0.5 * scipy.special.erfc((self.theory -\
                           self.limit) /\
                           (math.sqrt(2) * self.tau * self.theory)))
        # Sometimes we are trying to take log zero.
        except ValueError:
            self.loglike = -1e101
        return self.loglike       

@Cube.memoize
class LowerConstraint:
    """ Lower bound, Gaussian error function constraint. """
    def __init__(self, limit, tau):
        """ Initializes a lower bound constraint. 
        Arguments:
        limit -- Lower bound of measurement.
        tau --   Theoretical error in calculation.

        Returns:

        """
        self.limit = limit
        self.tau = tau
        self.theory = 0
        self.loglike = -1e101
        self.arg = self.args
        
    def SetLogLike(self):
        """ Calcualte upper bound likelihood with Gaussian error 
        function from model's predictions and data.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # NB that erf is an error function.
        try:
            self.loglike = math.log(0.5 * (1 + scipy.special.erf((\
                           self.theory - self.limit) /\
                           (math.sqrt(2) * self.tau))))
        # Sometimes we are trying to take log zero.
        except ValueError:
            self.loglike = -1e101
        return self.loglike

@Cube.memoize
class InterpolateLowerConstraint:
    """ Interpolate a lower 2D limit from a data file. """
    def __init__(self, file, tau):
        """ Initializes a lower bound constraint.
        The constraint is on the y-co-ordinate, and is calculated as
        a function of x. 
        Arguments:
        file --  Name of the data file.
        tau --   Theoretical error in calculation.

        Returns:

        """
        self.file = os.path.abspath(file)
        # The x parameter.
        self.theoryx = 0
        # The y parameter.
        self.theoryy = 0
        # The derived limit on the y-parameter, which is a function of x.
        self.theory = 0
        self.loglike = -1e101
        self.limit = 0
        self.tau = tau
        self.arg = self.args
        self.data = None
        
    def SetLogLike(self):
        """ Calcualte lower bound with interpolation 
        function, then apply an error function.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # Load the data file containing the limit, if it hasn't been loaded already.
        if self.data is None:

            # Find number of rows and columns
            cols = len(open(self.file, 'rb').readline().split())
            rows = len(open(self.file, 'rb').readlines())
        
            # Initialise data as dictionary of arrays.
            self.data = {}
            for key in range(cols):
                self.data[key] = NP.zeros(rows)
        
            # Populate data - NB we convert from string to float.
            row=0
            for line in open(self.file, 'rb'):
                for key, word in enumerate(line.split()):
                    self.data[key][row] = float(word)
                row += 1

        # Use NP.interp to interpolate the limit.  
	# Assume the data is x, y. s  
        self.theory = NP.interp(self.theoryx, self.data[0],\
                      self.data[1], left=None, right=None)
        
        # Now calcualte lower bound with Gaussian error function - erf.
        try:
            self.loglike = math.log(0.5 * (1 + scipy.special.erf((\
                           self.theoryy - self.theory) /\
                           (math.sqrt(2) * self.tau))))
        # Sometimes we are trying to take log zero.
        except ValueError:
            self.loglike = -1e101

        return self.loglike

@Cube.memoize 
class LikeMapConstraint:
    """ Interpolate likelihood data file. """
    def __init__(self, file):
        """ Interpolates a likelihood from a data file
        Arguments:
        file --  Name of the data file.

        Returns:

        """
        self.file = os.path.abspath(file)
        # The x parameter.
        self.theoryx = 0
        # The y parameter.
        self.theoryy = 0
        self.loglike = -1e101
        self.theory = 0
        self.arg = self.args
	self.data = None
                
    def SetLogLike(self):
        """ Calcualte lower bound with interpolation 
        function, then apply an error function.
        Arguments:
        
        Returns: The loglike from this constraint.

        """
        # Load the data file containing the limit, if it hasn't been loaded already.
        if self.data is None:

            # Find number of rows and columns
            cols = len(open(self.file, 'rb').readline().split())
	    rows = len(open(self.file, 'rb').readlines())
        
            # Initialise data as dictionary of arrays.
            self.data = {}
            for key in range(cols):
                self.data[key] = NP.zeros(rows)
        
            # Populate data - NB we convert from string to float.
            row=0
            for line in open(self.file, 'rb'):
                for key, word in enumerate(line.split()):
                    self.data[key][row] = float(word)
                row += 1
        
        try:
            # Use scipy to interpolate the like.
            self.loglike = math.log(mlab.griddata(
                self.data[0], self.data[1], self.data[2],
                NP.array([self.theoryx]), NP.array([self.theoryy]), 
                interp='nn'))
            
        # Sometimes we are trying to take log zero.
        except ValueError:
            self.loglike = -1e101
        self.theory = -2 * self.loglike
        return self.loglike   
    
# This class is useful if you want to 'switch off' a constraint, 
# but still write it to the chain etc.
@Cube.memoize
class DummyConstraint:
    """ No contribution to likelihood - a placeholder for turning off a 
    constraint. 
    """
    def __init__(self):
        """ Dummy constraint with no contribution to the likelhoood.
        Arguments:
        
        Returns:

        """
        self.theory = 0
        self.loglike = -1e101        
        self.arg = self.args
                
    def SetLogLike(self):
        """ Dummy constraint - log likelihood always 0.
        Arguments:
        
        Returns: The loglike from this constraint - always 0.

        """
        self.loglike = 0

        return self.loglike    

