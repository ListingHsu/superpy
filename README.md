# SuperPy
`SuperPy` is a Python code that scans the CMSSM's parameter to find the regions which agree best with experimental data with Bayesian statistics. 

1. It draws a model from the CMSSM with your priors, with `MultiNest`.
2. It calculates predictions for the model with `SoftSUSY`, `SuperISO`, `microMEGAs` and `FeynHiggs`.
3. It calculates the chi-squared by comparing these predictions with experimental data.
4. Returns this chi-squared to MultiNest, which explores the parameter space with an efficient algorithm.

`SuperPy` is **easy** to modify to alter the likelihoods, priors or model.

# SuperPlot
`SuperPlot` is a GUI that plots `SuperPy`, `SuperBayeS` (with its information file format) or generally `MultiNest` results. It can calculate and plot:
* One- and two-dimensional marginalised posterior pdf and credible regions.
* One- and two-dimensional marginalised profile likelihood and confidence intervals.
* Best-fit points.
* Posterior means.
* Three-dimensional scatter plots.

# Installation
From within the `SuperPy` directory,
    make all

or, for only the `SuperPlot` routines,
    make python
    
You might need to install the `matplotlib` Python plotting library. 

# Running SuperPy
From within the `SuperPy` directory,
    python SuperPy.py
Alter the settings in 
* Likelihoods in `Likelihood.py`
* Priors in `Prior.py`
* Scanning options in `MNOptions.py`

# Running SuperPlot
From within the `/SuperPlot` sub-directory,
    python SuperGUI.py
A GUI window will appear, to select a chain. Select e.g. the *.txt file in the `/examples` sub-directory. A second GUI window will appear. to select an information file. Select e.g. the *.txt file in the `/examples` sub-directory. Finally, select the variables and the plot type in the resulting GUI, and click `Make Plot`.

