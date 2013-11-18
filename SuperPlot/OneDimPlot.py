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
import numpy as NP

def OneDimPlot(xdata, posterior, chisq, xlabel='x', ylabel='', plottitle=AP.plottitle, legtitle=AP.PDFTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a one dimensional plot, showing profile likelihood,
    marginalised posterior, and statistics.
    Arguments:
    xdata -- Data column from chain of variable to be plotted.
    posterior -- Posterior weight from chain, same length as xdata.
    chisq -- Chi-squared from chain, same length as xdata.
    xlabel -- String for labelling the x-axis.
    ylabel -- String for labelling the y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """

    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = 0
    extent[3] = 1.2
    bin_limits = [extent[0], extent[1]]

    # If plot limits is None, make it the full extent of the data.
    if plot_limits is None:  
        plot_limits = extent

    # Initialise plot.
    fig, ax = PM.NewPlot()
    PM.PlotTicks(AP.xticks,AP.yticks, ax)  
    PM.PlotLabels(xlabel, ylabel, plottitle)
    PM.PlotLimits(ax, plot_limits)
    PM.Appearance()    
  
    # Points of interest.
    PM.PlotData(Stats.BestFit(chisq,xdata), 0.02, AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), 0.02, AP.PosteriorMean)
    
    # Data itself.
    pdf = OneDim.PosteriorPDF(xdata, posterior, nbins=number_bins, bin_limits=bin_limits).pdf
    x = OneDim.PosteriorPDF(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).bins
    PM.PlotData(x, pdf, AP.Posterior)
    
    proflike = OneDim.ProfileLike(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).proflike
    profchisq = OneDim.ProfileLike(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).profchisq
    x = OneDim.ProfileLike(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).bins
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
        PM.PlotData(confint[i,:], [1]*int(number_bins), AP.ConfInterval[i])

    # Show the plot.
    PM.Legend(AP.OneDimTitle)   
    return fig
    
def OneDimChiSq(xdata, chisq, xlabel='x', ylabel='$\Delta \chi^2$', plottitle=AP.plottitle, legtitle=AP.ChiSqTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a one dimensional plot, showing delta-chisq only,
    and excluded regions.
    Arguments:
    xdata -- Data column from chain of variable to be plotted.
    chisq -- Chi-squared from chain, same length as xdata.
    xlabel -- String for labelling the x-axis.
    ylabel -- String for labelling the y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """

    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = 0
    extent[3] = 1.2
    bin_limits = [extent[0], extent[1]]

    # If plot limits is None, make it the full extent of the data.
    if plot_limits is None:  
        plot_limits = extent

    # Initialise plot.
    fig, ax = PM.NewPlot()
    PM.PlotTicks(AP.xticks,AP.yticks, ax)  
    PM.PlotLabels(xlabel, ylabel, plottitle)
    PM.Appearance()    

    # Data itself.   
    profchisq = OneDim.ProfileLike(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).profchisq
    x = OneDim.ProfileLike(xdata, chisq, nbins=number_bins, bin_limits=bin_limits).bins
    PM.PlotData(x, profchisq, AP.ProfChiSq)
    
    # Plot the delta chi-squared between default range, 0 - 10.
    PM.PlotLimits(ax, plot_limits)
    
    # Bestfit point.
    PM.PlotData(Stats.BestFit(chisq,xdata), 0.08, AP.BestFit)
    
    # Confidence intervals as filled.
    deltachisq = OneDim.ConfidenceIntervals(profchisq, x, epsilon=AP.epsilon).deltachisq
    for i, dchi in enumerate(deltachisq):
        ax.fill_between(x, 0, 10, where=profchisq>=dchi, facecolor=AP.ProfChiSq.Colours[i], interpolate=False, alpha=0.7)
        # Plot a proxy for the legend - plot spurious data outside plot limits, 
        # with legend entry matching colours of filled regions.    
        plt.plot(-1, -1, 's', color=AP.ProfChiSq.Colours[i], label=AP.ChiSqLevelNames[i], alpha=0.7, ms=15)
    
    if AP.Tau is not None:
        # Plot the theory error as a band around the usual line.
        PM.PlotBand(x, profchisq, AP.Tau, ax)
        
    # Show the plot. 
    PM.Legend(legtitle)     
    return fig
        
  
