#########################################################################
#                                                                       #
""" G U I   P l o t t i n g

    Run this GUI interactively to look at your results.
    Project: SuperPlot.
    Author: Andrew Fowlie, University of Sheffield.
    Version: 1.0.
"""
#                                                                       #
#########################################################################

# Internal packages.
import OneDimPlot
import TwoDimPlot
import PlotMod as PM
import Appearance as AP
import ParamNames as PN

# External packages.
import re
from pylab import *
import os
import gobject
import pygtk
pygtk.require('2.0')
import gtk
import sys
import numpy as NP
# Uncomment to select /GTK/GTKAgg/GTKCairo
#from matplotlib.backends.backend_gtk import FigureCanvasGTK as FigureCanvas
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
#from matplotlib.backends.backend_gtkcairo import FigureCanvasGTKCairo as FigureCanvas

#########################################################################

# Open the chain with a GUI.
labels, data = PM.OpenData()

#########################################################################

# This class is a box to select the graph options, and a button to make a graph.
class GUIControl:
    def __init__(self, labels, data, dx=2, dy=3, dz=4, dtype=0):
        """ Initialise GUI.
        labels -- list of data labels.
        data -- data itself.
        dx, dy, dz -- indexes of default data to be plotted on x, y, z axis.
        dtype -- default plot type.
        """
        
        # Import data and labels as local variables, etc.
        self.data = data
        self.labels = labels
        self.dx = dx
        self.dy = dy
        self.dz = dz

        ########################################################################    

        # Make main GUI window.
        self.window = gtk.Window()
        self.window.maximize() # Window is maximised.
        self.window.set_title("SuperPlot") # With this title in the header.
        self.window.connect('destroy', lambda w: gtk.main_quit()) # Quit when we press cross.

        # Add a table of boxes to the window.
        self.gridbox = gtk.Table(14, 4, False) # 9 rows and 4 columns that are NOT homegenous.
        self.window.add(self.gridbox) # Add table to our window.
        self.gridbox.show() # Show the table.

        ########################################################################
    
        # Box to select  type of plot.
        # Title.
        typetitle = gtk.Button("Plot type:")    
        self.gridbox.attach(typetitle, 0, 1, 0, 1, xoptions=gtk.FILL)
        # Combo-box for various plot types.
        typebox = gtk.combo_box_new_text()
        self.gridbox.attach(typebox, 1, 2, 0, 1, xoptions=gtk.FILL)
        typebox.append_text('One-dimensional plot.')
        typebox.append_text('Two-dimensional posterior pdf.')
        typebox.append_text('Two-dimensional posterior pdf, filled contours only.')
        typebox.append_text('Two-dimensional profile likelihood.')
        typebox.append_text('Two-dimensional profile likelihood, filled contours only.')
        typebox.append_text('Three-dimensional scatter plot.')
        typebox.append_text('One-dimensional chi-squared plot.')
        typebox.connect('changed', self.ctype)
        typebox.set_active(dtype) # Set to default plot type.

        ########################################################################
    
        # x-axis.
        # Name of variable.
        xtitle = gtk.Button("x-axis variable:")    
        self.gridbox.attach(xtitle, 0, 1, 1, 2, xoptions=gtk.FILL)
        # Combo-box for variables.
        self.x = gtk.combo_box_new_text()
        # List the available parameter names in a particlular order
        # in the combo-boxes.
        for key in self.data.keys():
            name = self.labels[key].replace('$', '') # Remove $ from GUI, but not from plot labels.
            self.x.append_text(name)
        self.x.set_wrap_width(5) # Make box wider for long lists.
        self.gridbox.attach(self.x, 1, 2, 1, 2, xoptions=gtk.FILL)
        self.x.connect('changed', self.cx)  

        # Text box to alter x-axis label.    
        self.xtext = gtk.Entry()
        self.xtext.set_text(self.labels[self.dx])
        self.gridbox.attach(self.xtext, 1, 2, 2, 3, xoptions=gtk.FILL)
        self.xtext.connect("changed", self.cxtext) 

        # Set default plot variable.
        self.x.set_active(self.dx) 

        # y-axis.
        # Name of variable.
        ytitle = gtk.Button("y-axis variable:")    
        self.gridbox.attach(ytitle, 0, 1, 3, 4, xoptions=gtk.FILL)
        # Combo-box for variables.
        self.y = gtk.combo_box_new_text()
        # List the available parameter names in a particlular order
        # in the combo-boxes.
        for key in self.data.keys():
            name = self.labels[key].replace('$', '') # Remove $ from GUI, but not from plot labels.
            self.y.append_text(name) 
        self.y.set_wrap_width(5) # Make box wider for long lists.
        self.gridbox.attach(self.y, 1, 2, 3, 4, xoptions=gtk.FILL)
        self.y.connect('changed', self.cy)

        # Text box to alter y-axis label.  
        self.ytext = gtk.Entry()
        self.ytext.set_text(self.labels[self.dy])
        self.gridbox.attach(self.ytext, 1, 2, 4, 5, xoptions=gtk.FILL)
        self.ytext.connect("changed", self.cytext)       

        # Set default plot variable.
        self.y.set_active(self.dy)

        # z-axis.
        # Name of variable.
        ztitle = gtk.Button("z-axis variable:")    
        self.gridbox.attach(ztitle, 0, 1, 5, 6, xoptions=gtk.FILL)
        # Combo-box for variables.
        self.z = gtk.combo_box_new_text()
        # List the available parameter names in a particlular order
        # in the combo-boxes.
        for key in self.data.keys():
            name = self.labels[key].replace('$', '') # Remove $ from GUI, but not from plot labels.
            self.z.append_text(name) 
        self.z.set_wrap_width(5) # Make box wider for long lists.
        self.gridbox.attach(self.z, 1, 2, 5, 6, xoptions=gtk.FILL)
        self.z.connect('changed', self.cz)

        # Text box to alter z-axis label.  
        self.ztext = gtk.Entry()
        self.ztext.set_text(self.labels[self.dz])
        self.gridbox.attach(self.ztext, 1, 2, 6, 7, xoptions=gtk.FILL)
        self.ztext.connect("changed", self.cztext) 

        # Set default plot variable.
        self.z.set_active(self.dz)

        ########################################################################

        # Check-box to indicate that chain ought to be relabelled.
        self.checklabel = gtk.CheckButton('Relabel chain.')
        self.gridbox.attach(self.checklabel, 1, 2, 7, 8, xoptions=gtk.FILL)    

        ######################################################################## 

        # Text boxes for titles.

        # Main title.
        tplottitle = gtk.Button("Plot title:")    
        self.gridbox.attach(tplottitle, 0, 1, 9, 10, xoptions=gtk.FILL)
        # Text box to alter title.  
        self.plottitle = gtk.Entry()
        self.plottitle.set_text(AP.plottitle)
        self.gridbox.attach(self.plottitle, 1, 2, 9, 10, xoptions=gtk.FILL)

        # Legend title.
        tlegtitle = gtk.Button("Legend title:")    
        self.gridbox.attach(tlegtitle, 0, 1, 10, 11, xoptions=gtk.FILL)
        # Text box to alter title.  
        self.legtitle = gtk.Entry()
        self.legtitle.set_text("")
        self.gridbox.attach(self.legtitle, 1, 2, 10, 11, xoptions=gtk.FILL)

        ######################################################################## 

        # Number of bins per dimension.
        tbins = gtk.Button("Bins per dimension:")    
        self.gridbox.attach(tbins, 0, 1, 11, 12, xoptions=gtk.FILL)
        # Text box to alter bins.  
        self.bins = gtk.SpinButton()
        self.bins.set_increments(1,5)
        self.bins.set_range(5,100)
        self.bins.set_value(AP.nbins)
        self.gridbox.attach(self.bins, 1, 2, 11, 12, xoptions=gtk.FILL)

        ######################################################################## 

        # Axes limits! 
        tlimits = gtk.Button("Comma separated plot limits\nx_min, x_max, y_min, y_max:")    
        self.gridbox.attach(tlimits, 0, 1, 12, 13, xoptions=gtk.FILL)
        # Text box to alter title.  
        self.limits = gtk.Entry()
        self.gridbox.attach(self.limits, 1, 2, 12, 13, xoptions=gtk.FILL)
        self.limits.connect("changed", self.climits) 
        self.limits.append_text("")

        ########################################################################

        # Button to make the plot.
        makeplot = gtk.Button('Make plot.')
        makeplot.connect("clicked", self.pmakeplot)
        self.gridbox.attach(makeplot, 1, 2, 13, 14, xoptions=gtk.FILL)

        ########################################################################

        # Show all boxes so far regardless.
        
        self.window.show_all()

        return

    ############################################################################

    # Call-back functions. These functions are executed when buttons
    # are pressed/options selected. The get_active returns the index
    # rather than the label of the option selected. We find the data key
    # corresponding to that index.

    def cx(self, combobox):
        """ Callback function for setting parameter x from combo-box
        and updating the text-box.
        """
        self.xindex =  self.data.keys()[combobox.get_active()] # Set variable.
        self.xtext.set_text(self.labels[self.xindex]) # Update text-box.

    def cy(self, combobox):
        """ Callback function for setting parameter y from combo-box
        and updating the text-box.
        """
        self.yindex =  self.data.keys()[combobox.get_active()]
        self.ytext.set_text(self.labels[self.yindex])

    def cz(self, combobox):
        """ Callback function for setting parameter z from combo-box
        and updating the text-box.
        """
        self.zindex =  self.data.keys()[combobox.get_active()]
        self.ztext.set_text(self.labels[self.zindex])

    def cxtext(self, textbox):
        """ Callback function for changing x label.
        """
        self.labels[self.xindex] = textbox.get_text()

    def cytext(self, textbox):
        """ Callback function for changing y label.
        """
        self.labels[self.yindex] = textbox.get_text()

    def cztext(self, textbox):
        """ Callback function for changing z label.
        """
        self.labels[self.zindex] = textbox.get_text()

    def ctype(self, combobox):
        """ Callback function for selecting plot type. 
        """
        self.type = combobox.get_active()

    def climits(self, textbox):

        # If no limits, return None.
        if textbox.get_text() is "": 
            self.plot_limits = None
            return

        # Split text by commas etc.
        self.plot_limits = re.split(r"\s*[,;]\s*", textbox.get_text())
        # Convert to floats.
        self.plot_limits = [float(i) for i in self.plot_limits]
               
    def pmakeplot(self, button):
        """ Callback function for pressing make plot. 
        Main action is that it calls a ploting function that returns a figure object,
        that is attached to our window.
        """

        # If required, relabel chain.
        if self.checklabel.get_active(): self.relabel()

        # Reload modules, in case of changes.
        self.reload()

        # Make plot depending on type selected.
        # NB that the 0 is posterior weight, and 1 is chi-squared.
        # Labels is a dictionary, indexed identically to the  self.data.
        if self.type == 0:
            self.fig = OneDimPlot.OneDimPlot(self.data[self.xindex], self.data[0], self.data[1], labels[self.xindex],
                                            plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(),
                                            number_bins=self.bins.get_value(), plot_limits=self.plot_limits)
        elif self.type == 1:
            self.fig = TwoDimPlot.TwoDimPlotPDF(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], 
                                               self.labels[self.xindex], self.labels[self.yindex], 
                                               plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(),
                                               number_bins=self.bins.get_value(), plot_limits=self.plot_limits)

        elif self.type == 2:
            self.fig = TwoDimPlot.TwoDimPlotFilledPDF(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], 
                                                     self.labels[self.xindex], self.labels[self.yindex], 
                                                     plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(),
                                                     number_bins=self.bins.get_value(), plot_limits=self.plot_limits)

        elif self.type == 3:
            self.fig = TwoDimPlot.TwoDimPlotPL(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], 
                                              self.labels[self.xindex], self.labels[self.yindex], 
                                              plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(),
                                              number_bins=self.bins.get_value(), plot_limits=self.plot_limits)
        elif self.type == 4:
            self.fig = TwoDimPlot.TwoDimPlotFilledPL(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], 
                                                    self.labels[self.xindex], self.labels[self.yindex], 
                                                    plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(),
                                                    number_bins=self.bins.get_value(), plot_limits=self.plot_limits)

        elif self.type == 5:
            self.fig = TwoDimPlot.Scatter(self.data[self.xindex], self.data[self.yindex], self.data[self.zindex], 
                                         self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex], labels[self.zindex],
                                         plottitle=self.plottitle.get_text(), legtitle=self.legtitle.get_text(), 
                                         number_bins=self.bins.get_value(), plot_limits=self.plot_limits)
        elif self.type == 6:
            self.fig = OneDimPlot.OneDimChiSq(self.data[self.xindex], self.data[1], 
                                             self.labels[self.xindex], plottitle=self.plottitle.get_text(),
                                             legtitle=self.legtitle.get_text(), number_bins=self.bins.get_value(), plot_limits=self.plot_limits)

        # Put figure in plot box.
        canvas = FigureCanvas(self.fig)  # A gtk.DrawingArea.
        self.gridbox.attach(canvas, 2, 4, 0, 13)

        # Button to save the plot. 
        save = gtk.Button('Save plot.')
        save.connect("clicked", self.psave)
        self.gridbox.attach(save, 2, 4, 13, 14)

        # Show new buttons etc.
        self.window.show_all()

    def psave(self, button):
        """ Callback function to save a plot via a dialogue box. 
        NB differs from toolbox save, because it's figure object, rather 
        than image in the canvas box.
        """
        name = PM.SaveFileGUI() # Get name to save to from a dialogue box.
        if type(name) is not str: return # Case in which no file is chosen.
        self.fig.set_size_inches(AP.size) # So that figure is correct size for saving - showing a figure changes its size...
        PM.SavePlot(name)

    ############################################################################

    # Other (not callback) functions.

    def reload(self):
        """ Reload the modules - we might have altered the plot options etc, but not want to exit the GUI.
        If you want to change chains, exit the GUI - seems like the best way.
        """
        reload(PM)
        reload(OneDimPlot)
        reload(TwoDimPlot)
        reload(AP)
        reload(PN)

    def relabel(self):
        """ Reload the labels from altered module or info file.
        """
        self.labels = PM.LabelChain(self.data, PN.names)
        # Restart GUI so that labels are updated.
        self.window.hide()
        self.__init__(self.labels, self.data, self.xindex, self.yindex, self.zindex, self.type)
        return
        
def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = GUIControl(labels, data)
    main()

