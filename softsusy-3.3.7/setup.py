#########################################################################
#                                                                       #
""" W r a p p e r s                           

    Python wrappers for SoftSUSY.
    Project: SuperPy.
    Author: Andrew Fowlie, University of Sheffield.
    Version: 2.0
    Date: 03/13

"""
#                                                                       #
#########################################################################
# PYTHONPATH=$PYTHONPATH:./softsusy-*/
# python setup.py build
# PYTHONPATH=$PYTHONPATH:./build/lib.*/
# export PYTHONPATH


from distutils.core import setup, Extension
 
module1 = Extension('softsusy', sources = ['pysoftsusy.cpp', 'softsusy.cpp', 'lowe.cpp', 'def.cpp', 'rge.cpp', 'physpars.cpp', 'susy.cpp', 'linalg.cpp', 'numerics.cpp', 'softpars.cpp', 'utils.cpp'])
   
setup (name = 'softsusy',
        version = '1.0',
        description = 'Python interface to SOFTSUSY.',
        ext_modules = [module1])        
       
