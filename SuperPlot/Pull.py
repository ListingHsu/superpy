#########################################################################
#                                                                       #
#    P u l l / c h i - s q u a r e d     P l o t                        #
#                                                                       #
#########################################################################

import PlotMod as PM
import Stats
import Appearance as AP
import ParamNames as PN
import OneDim
# External packages.
import matplotlib.pyplot as plt
import numpy as NP
import math

# Open the chain with a GUI.
labels, data = PM.OpenData()

# Find minimum chi-squared.
chisq = data[1]
row = NP.argmin(chisq)
mchisq = chisq[row]

# Experimental data.
vars = [25, 21, 22, 11, 24, 17, 23, 18, 17] # Position of data in chain.
mus = [125.8, 80.39, 0.23146, 0.1120, 3.43e-4, 1.66e-4, 17.719, 3.2e-9, 28.7e-10]
sigmas = [0.6, 0.023, 1.3e-4, 0.0056, 0.22e-4, 0.33e-4, 0.043, 1.5e-9, 8.0e-10]
taus = [3, 0.015, 1.5e-4, 0.1*0.114, 0.21e-4, 0.38e-4, 2.40, 0.1*3.334e-09, 1.0e-10]

# Labels for plot.
chilabel='Total'
title = 'Basic'

# Initalise counter, list of names.
dummy=0 # Counter for y-axis label.
names = [] # List of labels for y-axis.

# Initialise plot.
fig, ax = PM.NewPlot()
PM.PlotTicks(10, 11, ax)  
PM.PlotLabels('$\chi^2$', 'Contribution', '')
PM.Appearance()  

# Alter some default settings.
#plt.rcParams['lines.linewidth'] = 18 # Thick lines.
plt.grid(True, which='minor', axis='x') # Minor grid lines for x-axis.
ax.tick_params(axis='y', which='minor', left='off') # No minor ticks for y-axis.

# Make second axis with standard deviations.
axabove = ax.twiny()
axabove.set_xlabel('Standard deviations $\sigma$')

# Plot limit for chi-squared
limchisq = int(math.floor(mchisq))+3 # Minimum chi-squared + padding.

# For standard deviation axis.
pullticks = []
pulllabels = []
for i in range(int(math.ceil(limchisq**0.5))):
	pullticks += [i**2] # Plot tick at 0, 1, 4, 9...
	pulllabels += [i] # With label 0, 1, 2, 3...
axabove.set_xticks(pullticks)
axabove.set_xticklabels(pulllabels)


# Set the plot ticks for chi-squared axis.
ax.set_xticks(range(limchisq)) # 0, 1..., ~ minimum chi-squared. 
ax.set_xlim([0, limchisq]) # 0 - minimum chi-squared + padding.
ax.set_ylim([-1,len(vars)+1]) # Number of items, with padding i.e. -1 and +1.
axabove.set_ylim([-1,len(vars)+1])
axabove.set_xlim([0, limchisq]) 

# Loop over the experimental measurements.
for var, mu, sigma, tau in zip(vars, mus, sigmas, taus):
	    
	    # Find contribution to chi-squared.
	    x = data[var][row]
	    xchisq = (x - mu)**2/(sigma**2+tau**2)
	    
	    # Make names for y-axis, but remove (GeV) etc.
	    name = labels[var].replace('(GeV)', '')
	    names = names + [name]
	    
	    # Plot bar of chi-squared.
	    ax.plot([0,xchisq], [dummy,dummy], '-', color='FireBrick', alpha=0.8, solid_capstyle="butt") 

	    # Increment counter for x-axis "data".
	    dummy+=1
	    
	    print name, xchisq 

# Plot vertical line for total chi-squared.
plt.rcParams['lines.linewidth'] = 4 # Regular lines.
plt.plot([chisq[row],chisq[row]], [-1,len(vars)+1], '--', color='FireBrick', alpha=0.8, label=chilabel, solid_capstyle="butt")  
print 'tchisq', chisq[row]

# Make particle name ticks.
plt.yticks(range(len(names)), names)
plt.subplots_adjust(left=0.4, bottom=0.1) # Might be necessary to make extra space.

# Make plot. 
PM.Legend(title) 
PM.SavePlot('ChiSq') 

