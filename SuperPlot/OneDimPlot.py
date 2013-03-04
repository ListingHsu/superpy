#########################################################################
#                                                                       #
#    1 D    P l o t                                                     #
#                                                                       #
#########################################################################

# Internal packages.
import OneDim
import Stats
import PlotMod as PM
import Appearance as AP

# External packages.
import matplotlib.pyplot as plt

def OneDimPlot(xdata, posterior, chisq, xlabel='x', ylabel=''):
    """ Makes a one dimensional plot, showing profile likelihood,
    marginalised posterior, and statistics.
    Arguments:
    xdata -- Data column from chain of variable to be plotted.
    posterior -- Posterior weight from chain, same length as xdata.
    chisq -- Chi-squared from chain, same length as xdata.
    xlabel -- String for labelling the x-axis.
    ylabel -- String for labelling the y-axis.
    """
    # Initialise plot.
    ax = PM.NewPlot()
    PM.PlotTicks(AP.xticks,AP.yticks, ax)  
    PM.PlotLabels(xlabel, ylabel, AP.plottitle)
    PM.PlotLimits(AP.plot_limits)
    PM.Appearance()    
    
    # Points of interest.
    PM.PlotData(Stats.BestFit(chisq,xdata), 0.02, AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), 0.02, AP.PosteriorMean)
    
    # Data itself.
    pdf = OneDim.PosteriorPDF(xdata, posterior, nbins=AP.nbins, bin_limits=AP.bin_limits).pdf
    x = OneDim.PosteriorPDF(xdata, chisq, nbins=AP.nbins, bin_limits=AP.bin_limits).bins
    PM.PlotData(x, pdf, AP.Posterior)
    
    proflike = OneDim.ProfileLike(xdata, chisq, nbins=AP.nbins, bin_limits=AP.bin_limits).proflike
    profchisq = OneDim.ProfileLike(xdata, chisq, nbins=AP.nbins, bin_limits=AP.bin_limits).profchisq
    x = OneDim.ProfileLike(xdata, chisq, nbins=AP.nbins, bin_limits=AP.bin_limits).bins
    PM.PlotData(x, proflike, AP.ProfLike)
    
    # Plot credible regions/confidence intervals above data.
    lowercredibleregion = OneDim.CredibleRegions(pdf, x, epsilon=AP.epsilon).lowercredibleregion
    uppercredibleregion = OneDim.CredibleRegions(pdf, x, epsilon=AP.epsilon).uppercredibleregion
    confint = OneDim.ConfidenceIntervals(profchisq, x, epsilon=AP.epsilon).confint
    
    # Plot credible region at 1.1 - just above plotted data which has its maximum at 1.
    # Plot confidence intervals at 1.  
    for i, value in enumerate(lowercredibleregion):
        PM.PlotData([lowercredibleregion[i], uppercredibleregion[i]],[1.1,1.1], 
                        AP.CredibleRegion[i])
        PM.PlotData(confint[i,:], [1]*AP.nbins, AP.ConfInterval[i])

    # Show the plot.
    PM.Legend(AP.OneDimeTitle)   
    plt.show()   
    
       

        
  
