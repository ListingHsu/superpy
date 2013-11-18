#########################################################################
#                                                                       #
#    2 D    P l o t                                                     #
#                                                                       #
#########################################################################

# Internal packages.
import TwoDim
import Stats
import PlotMod as PM
import Appearance as AP

# External packages.
import matplotlib.pyplot as plt
import numpy as NP

def TwoDimPlotFilledPDF(xdata, ydata, posterior, chisq, xlabel='', ylabel='', plottitle=AP.plottitle, legtitle=AP.PDFTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a two dimensional plot with filled credible regions only, showing 
    best-fit and posterior mean.
    Arguments:
    xdata -- x-axis data from chain.
    ydata -- y-axis data from chain, same length as xdata.
    posterior -- posterior weight from chain, same length as xdata.
    chisq -- chi-squared from chain, same length as xdata.
    xlabel -- label for x-axis.
    ylabel -- label for y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """
    
    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = min(ydata)
    extent[3] = max(ydata)
    bin_limits = [[extent[0],extent[1]],[extent[2],extent[3]]]

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
    PM.PlotData(Stats.BestFit(chisq,xdata), Stats.BestFit(chisq,ydata), AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), Stats.PosteriorMean(posterior,ydata), AP.PosteriorMean)

    pdf = TwoDim.PosteriorPDF(xdata, ydata, posterior, nbins=number_bins, bin_limits=bin_limits).pdf
    levels = TwoDim.CredibleRegions(pdf, epsilon=AP.epsilon).crediblelevel
    # Make sure pdf is correctly normalised.
    pdf = pdf / pdf.sum()
    PM.PlotFilledContour(xdata, ydata, pdf, levels, AP.LevelNames, AP.Posterior, plot_limits=extent)
  
    # Return the plot. 
    PM.Legend(legtitle)  
    return fig
 
def TwoDimPlotFilledPL(xdata, ydata, posterior, chisq, xlabel='',ylabel='', plottitle=AP.plottitle, legtitle=AP.PLTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a two dimensional plot with filled confidence intervals only, showing 
    best-fit and posterior mean.
    Arguments:
    xdata -- x-axis data from chain.
    ydata -- y-axis data from chain, same length as xdata.
    posterior -- posterior weight from chain, same length as xdata.
    chisq -- chi-squared from chain, same length as xdata.
    xlabel -- label for x-axis.
    ylabel -- label for y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """

    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = min(ydata)
    extent[3] = max(ydata)
    bin_limits = [[extent[0],extent[1]],[extent[2],extent[3]]]

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
    PM.PlotData(Stats.BestFit(chisq,xdata), Stats.BestFit(chisq,ydata), AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), Stats.PosteriorMean(posterior,ydata), AP.PosteriorMean)
    
    proflike = TwoDim.ProfileLike(xdata, ydata, chisq, nbins=number_bins, bin_limits=bin_limits).proflike
    levels = TwoDim.ConfidenceIntervals(epsilon=AP.epsilon).deltaPL
    PM.PlotFilledContour(xdata, ydata, proflike, levels, AP.LevelNames, AP.ProfLike, plot_limits=extent)
      
    # Show the plot.
    PM.Legend(legtitle)
    return fig

def TwoDimPlotPDF(xdata, ydata, posterior, chisq, xlabel='', ylabel='', plottitle=AP.plottitle, legtitle=AP.PDFTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a two dimensional marginalised posterior plot, showing 
    best-fit and posterior mean and credible regions.
    Arguments:
    xdata -- x-axis data from chain.
    ydata -- y-axis data from chain, same length as xdata.
    posterior -- posterior weight from chain, same length as xdata.
    chisq -- chi-squared from chain, same length as xdata.
    xlabel -- label for x-axis.
    ylabel -- label for y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """

    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = min(ydata)
    extent[3] = max(ydata)
    bin_limits = [[extent[0],extent[1]],[extent[2],extent[3]]]

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
    PM.PlotData(Stats.BestFit(chisq,xdata), Stats.BestFit(chisq,ydata), AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), Stats.PosteriorMean(posterior,ydata), AP.PosteriorMean)
    
    pdf = TwoDim.PosteriorPDF(xdata, ydata, posterior, nbins=number_bins, bin_limits=bin_limits).pdf
    PM.PlotImage(xdata, ydata, pdf, AP.Posterior, AP.PDFTitle, plot_limits=extent)
    
    levels = TwoDim.CredibleRegions(pdf, epsilon=AP.epsilon).crediblelevel
    # Make sure pdf is correctly normalised.
    pdf = pdf / pdf.sum()
    PM.PlotContour(xdata, ydata, pdf, levels, AP.LevelNames, AP.Posterior, plot_limits=extent)

    # Show the plot. 
    PM.Legend(legtitle)
    return fig
        
def TwoDimPlotPL(xdata, ydata, posterior, chisq, xlabel='',ylabel='', plottitle=AP.plottitle, legtitle=AP.PLTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a two dimensional profile likelihood plot, showing 
    best-fit and posterior mean and confidence intervals.
    Arguments:
    xdata -- x-axis data from chain.
    ydata -- y-axis data from chain, same length as xdata.
    posterior -- posterior weight from chain, same length as xdata.
    chisq -- chi-squared from chain, same length as xdata.
    xlabel -- label for x-axis.
    ylabel -- label for y-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """
    
    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = min(ydata)
    extent[3] = max(ydata)
    bin_limits = [[extent[0],extent[1]],[extent[2],extent[3]]]

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
    PM.PlotData(Stats.BestFit(chisq,xdata), Stats.BestFit(chisq,ydata), AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), Stats.PosteriorMean(posterior,ydata), AP.PosteriorMean)
    
    proflike = TwoDim.ProfileLike(xdata, ydata, chisq, nbins=number_bins, bin_limits=bin_limits).proflike
    PM.PlotImage(xdata, ydata, proflike, AP.ProfLike, AP.PLTitle, plot_limits=extent)
    
    levels = TwoDim.ConfidenceIntervals(epsilon=AP.epsilon).deltaPL
    PM.PlotContour(xdata, ydata, proflike, levels, AP.LevelNames, AP.ProfLike, plot_limits=extent)
      
    # Show the plot. 
    PM.Legend(legtitle)
    return fig

def Scatter(xdata, ydata, zdata, posterior, chisq, xlabel='',ylabel='',zlabel='', plottitle=AP.plottitle, legtitle=AP.PLTitle,
    plot_limits=AP.plot_limits, number_bins=AP.nbins):
    """ Makes a three dimensional scatter plot, showing 
    best-fit and posterior mean and credible regions and confidence intervals.
    The scattered points are coloured by the zdata.
    Arguments:
    xdata -- x-axis data from chain, scattered on plot.
    ydata -- y-axis data from chain, same length as xdata, scattered on plot.
    zdata -- y-axis data from chain, same length as xdata, colours the scattered points.
    posterior -- posterior weight from chain, same length as xdata.
    chisq -- chi-squared from chain, same length as xdata.
    xlabel -- label for x-axis.
    ylabel -- label for y-axis.
    zlabel -- label for z-axis.
    plottitle --- title for plot.
    legtitle --- title for legend.
    plot_limits --- limits for plotting.
    number_bins -- number of bins per dimension for histograms.
    """
    
    # Make bin limits equal the full extent.
    extent = NP.zeros((4))
    extent[0] = min(xdata)
    extent[1] = max(xdata)
    extent[2] = min(ydata)
    extent[3] = max(ydata)
    bin_limits = [[extent[0],extent[1]],[extent[2],extent[3]]]

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
    PM.PlotData(Stats.BestFit(chisq,xdata), Stats.BestFit(chisq,ydata), AP.BestFit)
    PM.PlotData(Stats.PosteriorMean(posterior,xdata), Stats.PosteriorMean(posterior,ydata), AP.PosteriorMean)

    # Plot scatter of points.
    sc = plt.scatter(xdata, ydata, s=AP.Scatter.Size, c=zdata, marker=AP.Scatter.Symbol, 
                    cmap=AP.Scatter.ColourMap, norm=None, vmin=None, vmax=None, alpha=0.5,
                    linewidths=None, verts=None)
    # Plot a colour bar.
    cb = plt.colorbar(sc, orientation='horizontal', shrink=0.5)
    # Colour bar label.
    cb.ax.set_xlabel(zlabel) 
    
    # Confidence intervals and credible regions.
    proflike = TwoDim.ProfileLike(xdata, ydata, chisq, nbins=number_bins, bin_limits=bin_limits).proflike
    pdf = TwoDim.PosteriorPDF(xdata, ydata, posterior, nbins=number_bins, bin_limits=bin_limits).pdf
    levels = TwoDim.ConfidenceIntervals(epsilon=AP.epsilon).deltaPL
    PM.PlotContour(xdata, ydata, proflike, levels, AP.LevelNames, AP.ProfLike, plot_limits=extent)
    levels = TwoDim.CredibleRegions(pdf, epsilon=AP.epsilon).crediblelevel
    # Make sure pdf is correctly normalised.
    pdf = pdf / pdf.sum()
    PM.PlotContour(xdata, ydata, pdf, levels, AP.LevelNames, AP.Posterior, plot_limits=extent)
    
    # Show the plot.
    PM.Legend(legtitle)  
    return fig
