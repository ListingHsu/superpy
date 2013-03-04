#########################################################################
#                                                                       #
""" S u p e r P y                            

    Finds regions of SUSY models' parameter spaces that are in
    best agreement with experimental data.
    Project: SuperPy.
    Author: Andrew Fowlie, University of Sheffield.
    Version: 1.0
    Date: 03/13

"""
#                                                                       #
#########################################################################

# External packages.
import pymultinest
import sys
import os

# Internal packages.
import Debug as DB # Debug options.
import Priors # Priors specfied.
import Likelihood # Constraints and likelihood functions.
import MNOptions as MN # Sampling options.


# Check that MuliNest won't clobber existing data.
if not MN.resume and os.path.isfile(MN.outputfiles_basename + '.txt'):
        sys.exit('''MultiNest would clobber existing data files:
        i) Within MNOptions.py, set resume=True, or
        ii) Within MNOptions.py, change outputfiles_basename, or
        iii) Delete the (unwanted?) data files.''')
                          
#########################################################################
#                                                                       #
#    M u l t i n e s t                                                  #
#    Run and track Multinest.                                           #
#                                                                       #
#########################################################################

if DB.Debug:
    # Begin progress watcher, to track the output continuously.
    # It will print no. of alive and rejected points by checking the data 
    # files every 10 seconds or so.
    printer =  pymultinest.ProgressPrinter(n_params = MN.n_dims,
               interval_ms = 500, outputfiles_basename = MN.outputfiles_basename)
    printer.start()

# Run MultiNest!
pymultinest.run(LogLikelihood=MN.LogLikelihood, Prior=MN.Prior, n_dims=MN.n_dims,
n_params=MN.n_params, n_clustering_params=MN.n_clustering_params,
wrapped_params=MN.wrapped_params,multimodal=MN.multimodal,
const_efficiency_mode=MN.const_efficiency_mode, n_live_points=MN.n_live_points,
evidence_tolerance=MN.evidence_tolerance, sampling_efficiency=MN.sampling_efficiency,
n_iter_before_update=MN.n_iter_before_update,
null_log_evidence=MN.null_log_evidence, max_modes=MN.max_modes,
outputfiles_basename=MN.outputfiles_basename,
seed=MN.seed, verbose=MN.verbose, resume=MN.resume, context=MN.context)

if DB.Debug:
    # Stop our progress watcher - since MultiNest ought to now have finished.
    printer.stop()

#########################################################################
