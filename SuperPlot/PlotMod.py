#########################################################################
#                                                                       #
#     P l o t   M o d                                                   #
#                                                                       #
#########################################################################

# General functions for plotting data, defined once so that they can be used/edited 
# in a consistent manner.

# External packages.
from pylab import *
import os
import gobject
import pygtk
pygtk.require('2.0')
import gtk
import sys
from datafile.extractfile import dataFile as DF
from matplotlib import rc
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullLocator
import matplotlib.pyplot as plt
import pickle
import re

# Internal packages.
import numpy as NP
import ParamNames as PN
import Appearance as AP

def OpenData():
    """ Wrapper for opening and labelling a chain.
    
    Returns:
    data -- Dictionary with chain.
    label -- Dictionary with chain's labels.
    """
    # Select file with a GUI.
    filename = OpenFileGUI()
    
    if filename is None:
        sys.exit("No data file was selected - did you press cancel?")
    
    # Open file.
    data = OpenChain(filename)
    # Assign labels.
    label = LabelChain(data, PN.names)
    
    return label, data

def OpenFileGUI():
    """ GUI for opening a file with a file browser.
    
    Return:
    filename -- Name of file selected with GUI.
    """
    # Select the file from a dialog box.
    dialog = gtk.FileChooserDialog("Open..",
                                   None,
                                   gtk.FILE_CHOOSER_ACTION_OPEN,
                                   (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                    gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    dialog.set_default_response(gtk.RESPONSE_OK)

    # Only show particular files.
    filter = gtk.FileFilter()
    filter.set_name("Text files, pickled data or info file.")
    filter.add_pattern("*.txt")
    filter.add_pattern("*.pkl")
    filter.add_pattern("*.info")
    dialog.add_filter(filter)
    filter = gtk.FileFilter()
    dialog.add_filter(filter)

    response = dialog.run()
    if response == gtk.RESPONSE_OK:
        print 'File:', dialog.get_filename(), 'selected.'
    elif response == gtk.RESPONSE_CANCEL:
        print 'Error: no file selected.'
        
    # Save the file name/path
    filename = dialog.get_filename()
    dialog.destroy()

    return filename 

def OpenChain(filename):
    """ Open a data file or pickle. If opening a data file, make a pickle for future plots.
    
    Arguments:
    filename -- Name of chain file.
    
    Returns:
    data -- Dictionary of chain.    
    """ 
    # If pickle, open it. Else open a data file and make a pickle too,
    # with the same name but with the pkl suffix.
    name, extension = os.path.splitext(filename)
    if 'pkl' in extension:
            picklef = open(filename, 'rb')
            data = pickle.load(picklef)
            picklef.close()
    else: 
            data = DF(filename, quiet=True, index=None)
            picklef = open( name+'.pkl', 'wb')
            pickle.dump(data, picklef)
            picklef.close()
    
    return data

def LabelChain(data, names):
    """ Match labels to the data. 
    i) Match list of labels.
    ii) If it doesn't match, try to load an *info file.
    iii) If that doesn't match, use data indicies.
    Arguments:
    data -- Data chain, to match arguments with.
    names -- List of names, for labels.
    
    Return:
    label -- Dictonary of labels, indexed with the same
    indicies as the data chain.
    """
    label = {}
    # Match labels with names provided.
    print "Trying parameter names."
    if len(data.keys()) == len(names):
            for i, key in enumerate(data.keys()):
                    label[key] = names[i]
            return label
    
    # Attempt to load a SuperBayeS style info file.
    print "Parameter name length didn't match chain length.\n Try an info file."
    label = ReadInfo()
    if len(data.keys()) == len(label):
        return label
    
    # Admit defeat - use chain indicies.
    print "Parameter names from info file didn't match chain length.\n Basic labels!"
    label = {}
    for key in data.keys():
        label[key] = key
    return label


def ReadInfo():
    """ Read labels from a SuperBayeS style info file.
    The file is chosen with a GUI.
    """
    label = {}
    # Open the info file with a GUI.
    filename = OpenFileGUI()
    
    if filename is None:
        return label
    
    info = open(filename, 'rb')
    for line in info:
        # Look for labX=string.
        if line.startswith('lab'):
            string = line.strip().split('=')[::-1][0]
            index=re.findall(re.escape('lab')+"(.*)"+re.escape('='),line)[0]
            
            # Correct index - SuperBayeS info files begin at 1, and ignore
            # posterior weight and ChiSq in positions 0 and 1 of the chain.
            index = str(int(index) + 1)
            
            # Correct Latex, by adding $$ for maths, but excluding (GeV).
            string = '$' + string + '$'
            string = string.replace('(GeV)$', '$ (GeV)')
            label[index] = string
    info.close()
    
    # Add posterior weight and ChiSq.
    label['0'] = '$p_i$'
    label['1'] = '$\chi^2$'

    return label
                             
def PlotData(x, y, Scheme):     
    """ Plot a point with a particular scheme.
    Arguments:
    x -- data to be plotted on x-axis.
    y -- data to be plotted on y-axis.
    Scheme -- Object containing plot options.
    """
    plt.plot(x, y, Scheme.Symbol, color=Scheme.Colour,label=Scheme.Label, ms=Scheme.Size)            

def NewPlot():              
    """ Clear the plot so we start afresh."""
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    return ax 

def SavePlot(name):
    """ Save the plot, with a descriptive name.
    Arguments:
    name -- suffix of filename, without extension.
    """
    plt.savefig(name+'.pdf', dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1)
                                      
def Appearance():
    """ Specify the plots appearance, with e.g. font types etc.
    """
   
    # Make the lines thicker.
    plt.rcParams['lines.linewidth'] = 4

    # Plot gridlines over the plot - can be useful
    plt.grid(True)
    
    # Set the fonts - I like mathpazo/Palatino, but
    # that would introduce an unneccesasry dependency.
    rc('text', usetex=True)
    rc('font', **{'family':'serif','serif':['Computer Modern Roman']})
        
def Legend(title=None):        
    """ Turn on the legend.
    Arguments:
    title -- Title of legend.
    """
    leg = plt.legend(prop={'size':12}, shadow=False, fancybox=True,
                    title=title, loc='best', borderaxespad=1.,
                    scatterpoints=1, numpoints=1)
    leg.get_frame().set_alpha(0.5)
                
def PlotLimits(plot_limits=None):
    """ If specified plot limits, set them.
    Arguments:
    plot_limits -- Array of plot limits in order xmin, xmax, ymin, ymax.
    """
    if plot_limits is not None:
        plt.axis([plot_limits[0], plot_limits[1], plot_limits[2], plot_limits[3]])

def PlotTicks(xticks,yticks,ax):    
    # Set major x, y ticks.
    ax.xaxis.set_major_locator(MaxNLocator(xticks))
    ax.yaxis.set_major_locator(MaxNLocator(yticks))
    # Auto minor x and y ticks.
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())       

def PlotLabels(xlabel, ylabel, plottitle=''):
    """ Plot axis labels.
    Arguments:
    xlabel -- Label for x-axis.
    ylabel -- Label for y-axis.
    plottile -- Title appearing above plot.
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)   
    # Plot title.
    plt.title(plottitle)

def PlotImage(xdata, ydata, data, Scheme, zlabel=''):
    """ Plot data as an image.
    Arguments:
    xdata -- x-axis data.
    ydata -- y-axis data.
    data -- image data, i.e., z-axis data.
    Scheme -- Object containing appearance options, colours etc.
    zlabel -- Label for colour bar.
    """  
    
    # Set the aspect so that resulting figure is a square.
    extent= NP.zeros((4))
    if Scheme.plot_limits is None:
        extent[0] = min(xdata)
        extent[1] = max(xdata)
        extent[2] = min(ydata)
        extent[3] = max(ydata)    
    else:
        extent = Scheme.plot_limits
    aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])
    PlotLimits(extent)
    
    # Interpolating perhaps misleads, if you don't want it set 
    # interpolation='nearest'. NB that imshow is annoying - it reads y,x 
    # rather than x,y so we take transpose.
    plt.im = plt.imshow(data.T, cmap=Scheme.ColourMap, extent=extent, 
                        interpolation='bilinear', label=Scheme.Label, 
                        origin='lower', aspect=aspect) 
    # Plot a colour bar.
    cb = plt.colorbar(plt.im, orientation='horizontal', shrink=0.5)
    # Colour bar label.
    cb.ax.set_xlabel(zlabel)    

def PlotContour(xdata, ydata, data, levels, names, Scheme):
    """ Make unfilled contours for a plot.
    Arguments:
    xdata -- x-axis data.
    ydata -- y-axis data.
    data -- Data to be contoured.
    levels -- Levels at which to draw contours.
    names -- Labels for the contour levels.
    Scheme -- Object containing appearance options, colours etc.    
    """     
    # Set the aspect so that resulting figure is a square.
    extent= NP.zeros((4))
    if Scheme.plot_limits is None:
        extent[0] = min(xdata)
        extent[1] = max(xdata)
        extent[2] = min(ydata)
        extent[3] = max(ydata)    
    else:
        extent = Scheme.plot_limits
    PlotLimits(extent)
           
    # Make the contours of the levels.
    cset = plt.contour(data.T, levels, linewidths=2, 
                        colors=Scheme.Colour, hold='on', extent=extent, 
                        interpolation='bilinear', origin='lower', linestyles=['--','-'])
    
    # Set the contour labels - they will show labels.        
    fmt = {}
    for i, s in zip(cset.levels, names):
        fmt[i] = s
    plt.clabel(cset, inline=True, fmt=fmt, fontsize=12,  hold='on')    

def PlotFilledContour(xdata, ydata, data, levels, names, Scheme):
    """ Make filled contours for a plot.
    Arguments:
    xdata -- x-axis data.
    ydata -- y-axis data.
    data -- Data to be contoured.
    levels -- Levels at which to draw contours.
    names -- Labels for the contour levels.
    Scheme -- Object containing appearance options, colours etc.    
    """   
    # Set the aspect so that resulting figure is a square.
    extent= NP.zeros((4))
    if Scheme.plot_limits is None:
        extent[0] = min(xdata)
        extent[1] = max(xdata)
        extent[2] = min(ydata)
        extent[3] = max(ydata)    
    else:
        extent = Scheme.plot_limits
    PlotLimits(extent)
    
    # We need to ensure levels are in ascending order, and append the list with one.
    # This makes 2 intervals (between 3 values) that will be shown with colours.
    levels = NP.append(levels, 1.0) 
    
    # Filled contours.  
    cset = plt.contourf(data.T, levels,  
                        colors=Scheme.Colours, 
                        hold='on', extent=extent, 
                        interpolation='bilinear', origin='lower',
                        alpha=0.7)
    
    # Plot a proxy for the legend - plot spurious data outside plot limits, 
    # with legend entry matching colours of filled contours.    
    for i, value in enumerate(Scheme.Colours):
        plt.plot(-1.5*abs(min(xdata)), 1.5*abs(max(ydata)), 's', color=Scheme.Colours[i], label=AP.LevelNames[i], alpha=0.7, ms=15)
