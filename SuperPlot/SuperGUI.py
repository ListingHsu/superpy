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
import ParamNames as PN

# External packages.
from pylab import *
import os
import gobject
import pygtk
pygtk.require('2.0')
import gtk
import sys

#########################################################################

# Open the chain with a GUI.
labels, data = PM.OpenData()

#########################################################################

# This class is a box to select the graph options, and a button to make a graph.
class GUIControl:
    def __init__(self):
        # Make window.
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # Add boxes for selecting parameters.
        x = gtk.combo_box_new_text()
        vbox.add(x)
        x.connect('changed', self.cx)
        x.set_active(0)

        y = gtk.combo_box_new_text()
        vbox.add(y)
        y.connect('changed', self.cy)
        y.set_active(0)

        z = gtk.combo_box_new_text()
        vbox.add(z)
        z.connect('changed', self.cz)
        z.set_active(0)

        # List the available parameter names in a particlular order.
        for key in data.keys():
            name = labels[key]
            x.append_text(name)
            y.append_text(name)
            z.append_text(name)

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

        # Button to make the plot.
        button = gtk.Button('Make plot.')
        button.connect("clicked", self.button)
        vbox.add(button)

        window.show_all()
        return

    # Call-back functions. These functions are executed when buttons
    # are pressed/options selected. The get_active returns the index
    # rather than the label of the option selected. We find the data key
    # corresponding to that index.

    # Function for setting parameter x.
    def cx(self, combobox):
        self.xindex = data.keys()[combobox.get_active()]

    # Function for setting parameter y.
    def cy(self, combobox):
        self.yindex = data.keys()[combobox.get_active()]

    # Function for setting parameter z.
    def cz(self, combobox):
        self.zindex = data.keys()[combobox.get_active()]

    # Function for graph type.
    def changed_type(self, combobox):
        self.type = combobox.get_active()

    # Function for button to make a graph for each option.
    # NB that the 0 is posterior weight, and 1 is chi-squared.
    # Labels is a dictionary, indexed identically to the data.
    def button(self, widget):
        if self.type == 0:
            OneDimPlot.OneDimPlot(data[self.xindex], data[0], data[1], labels[self.xindex])
        elif self.type == 1:
            TwoDimPlot.TwoDimPlotPDF(data[self.xindex],data[self.yindex], data[0], data[1], labels[self.xindex], labels[self.yindex])
        elif self.type == 2:
            TwoDimPlot.TwoDimPlotFilledPDF(data[self.xindex],data[self.yindex], data[0], data[1], labels[self.xindex], labels[self.yindex])
        elif self.type == 3:
            TwoDimPlot.TwoDimPlotPL(data[self.xindex], data[self.yindex], data[0], data[1], labels[self.xindex], labels[self.yindex])
        elif self.type == 4:
            TwoDimPlot.TwoDimPlotFilledPL(data[self.xindex], data[self.yindex], data[0], data[1], labels[self.xindex], labels[self.yindex])
        elif self.type == 5:
            TwoDimPlot.Scatter(data[self.xindex], data[self.yindex], data[self.zindex], data[0], data[1], labels[self.xindex], labels[self.yindex], labels[self.zindex])
        elif self.type == 6:
            OneDimPlot.OneDimChiSq(data[self.xindex], data[1], labels[self.xindex])
def main():
    gtk.main()
    return

if __name__ == "__main__":
    bcb = GUIControl()
    main()

