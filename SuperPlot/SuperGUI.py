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
from pylab import *
import os
import gobject
import pygtk
pygtk.require('2.0')
import gtk
import sys
import numpy as NP

#########################################################################

# Open the chain with a GUI.
labels, data = PM.OpenData()

#########################################################################

# This class is a box to select the graph options, and a button to make a graph.
class GUIControl:
    def __init__(self, labels, data):
        
        # Import data and labels as local variables.
        self.data =  data
        self.labels = labels
    
        # Make self.window.
        self.window = gtk.Window()
        self.window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox(False, 0)
        self.window.add(vbox)
        vbox.show()

        # Add boxes for selecting parameters.
        x = gtk.combo_box_new_text()
        x.set_wrap_width(5) # Make box wider for long lists.
        vbox.add(x)
        x.connect('changed', self.cx)    

        y = gtk.combo_box_new_text()
        y.set_wrap_width(5) # Make box wider for long lists.
        vbox.add(y)
        y.connect('changed', self.cy)
        
        z = gtk.combo_box_new_text()
        z.set_wrap_width(5) # Make box wider for long lists.
        vbox.add(z)
        z.connect('changed', self.cz)

        # List the available parameter names in a particlular order.
        for key in  self.data.keys():
            name = self.labels[key].replace('$', '') # Remove $ from GUI, but not from plot labels.
            x.append_text(name)
            y.append_text(name)
            z.append_text(name)

        # Set the active boxes - let's ignore posterior weight and chi-squared.
        x.set_active(2)
        y.set_active(3)
        z.set_active(4)
    
        # Box to select  type of plot.
        typebox = gtk.combo_box_new_text()
        vbox.add(typebox)
        typebox.append_text('One-dimensional plot.')
        typebox.append_text('Two-dimensional posterior pdf.')
        typebox.append_text('Two-dimensional posterior pdf, filled contours only.')
        typebox.append_text('Two-dimensional profile likelihood.')
        typebox.append_text('Two-dimensional profile likelihood, filled contours only.')
        typebox.append_text('Three-dimensional scatter plot.')
        typebox.append_text('One-dimensional chi-squared plot.')
        typebox.connect('changed', self.changed_type)
        typebox.set_active(0)

        # Button to reload labels, modules etc.
        button = gtk.Button('Reload labels, modules etc.')
        button.connect("clicked", self.reload)
        vbox.add(button)

        # Button to make the plot.
        button = gtk.Button('Make plot.')
        button.connect("clicked", self.button)
        vbox.add(button)

        self.window.show_all()
        return

    # Call-back functions. These functions are executed when buttons
    # are pressed/options selected. The get_active returns the index
    # rather than the label of the option selected. We find the data key
    # corresponding to that index.

    # Function for setting parameter x.
    def cx(self, combobox):
        self.xindex =  self.data.keys()[combobox.get_active()]

    # Function for setting parameter y.
    def cy(self, combobox):
        self.yindex =  self.data.keys()[combobox.get_active()]

    # Function for setting parameter z.
    def cz(self, combobox):
        self.zindex =  self.data.keys()[combobox.get_active()]

    # Function for graph type.
    def changed_type(self, combobox):
        self.type = combobox.get_active()

    # Function for button to make a graph for each option.
    # NB that the 0 is posterior weight, and 1 is chi-squared.
    # Labels is a dictionary, indexed identically to the  self.data.
    def button(self, widget):

        # Make plot depending on type selected.
        if self.type == 0:
            OneDimPlot.OneDimPlot(self.data[self.xindex], self.data[0], self.data[1], labels[self.xindex])
        elif self.type == 1:
            TwoDimPlot.TwoDimPlotPDF(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex])
        elif self.type == 2:
            TwoDimPlot.TwoDimPlotFilledPDF(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex])
        elif self.type == 3:
            TwoDimPlot.TwoDimPlotPL(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex])
        elif self.type == 4:
            TwoDimPlot.TwoDimPlotFilledPL(self.data[self.xindex], self.data[self.yindex], self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex])
        elif self.type == 5:
            TwoDimPlot.Scatter(self.data[self.xindex], self.data[self.yindex], self.data[self.zindex], self.data[0], self.data[1], self.labels[self.xindex], self.labels[self.yindex], labels[self.zindex])
        elif self.type == 6:
            OneDimPlot.OneDimChiSq(self.data[self.xindex], self.data[1], self.labels[self.xindex])

    def reload(self, widget):
            
        # Reload the modules - we might have altered the plot options etc, but not want to exit the GUI.
        # If you want to change chains, exit the GUI - seems like the best way.
        reload(PM)
        reload(OneDimPlot)
        reload(TwoDimPlot)
        reload(AP)
        reload(PN)
        # Reload the labels from altered module or info file.
        self.labels = PM.LabelChain(self.data, PN.names)
        # Restart GUI.
	self.window.hide()
        self.__init__(self.labels, self.data)
        return
    
def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = GUIControl(labels, data)
    main()


