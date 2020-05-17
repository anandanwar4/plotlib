# -*- coding: utf-8 -*-
import matplotlib as matplotlib;
import matplotlib.pyplot as pyplot;
import math as math;

class TwoDimensionalDataVisualisation:

    def generateSimpleLinePlot(self, plotLabel, xLabel, yLabel, firstAxisData, 
                               secondAxisData, format = ''):
        """Plots line graph in a 2D plane.
        
        Used for 2D plots only. The function internally sets plotLabel, xLabel, \
        yLabel. The plot uses the data given in firstAxisData and \
        secondAxisData. It uses a single axes object given by pyplot.subplots().

        Args:
            plotLabel (String): Title of the plot.\n
            xLabel (String): The label of the x axis in the plot.\n
            yLabel (String): The label of the y axis in the plot.\n
            firstAxisData (Array): The x axis data in the plot.\n
            secondAxisData (Array): The y axis data in the plot.\n
            format (String) [Optional]: The format the plot to be used. It is \
            empty by default. The format of teh string should be:\
            "[marker][line][color]". For exploring the allowed values \
            for all the three please look into the matplotlib official \
            documentation. 
        """
        
        figure, axes = pyplot.subplots();
        self.__initializePlotTitleAndLabels(axes, plotLabel, xLabel, yLabel);
        self.__plotDataInLinePlot(axes, firstAxisData, secondAxisData, fmt = format);
        return;


    def generateMultipleLinePlots(self, listOfDicts):
        """Plots the list of data as line graph in separate plots.
        
        Used for 2D plots only. The function internally uses \
        subplots(num. of rows, 4), to generate group of plots with 4 in a row.\
        The number of plots will be equal to the size of the listOfDictionaries\
        given. 

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL_OF_PLOT>, 'xLabel':<STRING_AS_X_LABEL>, \
                'yLabel':<STRING_AS_Y_LABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>, 'format':<STRING>}] \n
            format (String) [Optional]: The format the plot to be used. It is \
            empty by default. The format of the string should be:\
            "[marker][line][color]". For exploring the allowed values \
            for all the three please look into the matplotlib official \
            documentation. 
        """
        
        size = len(listOfDicts);
        figure, axes = None, None;
        
        if (size <= 4):
            figure, axes = pyplot.subplots(1, size);
        else:
            figure, axes = pyplot.subplots((math.floor(size / 4) + 1), 4);
        
        for index, dict in enumerate(listOfDicts):
            self.__initializePlotTitleAndLabels(axes[index], dict['plotLabel'], 
                                                dict['xLabel'], dict['yLabel']);
            self.__plotDataInLinePlot(axes[index], dict['firstAxisData'], 
                                    dict['secondAxisData'], dict['format']);
        return;


    def generateMultipleOverlappedLinePlots(self, listOfDicts):
        """Plots the list of data as line graph in same plot.
        
        Used for 2D plots only. The function internally uses \
        pyplot.subplots(), to generate a plot.

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>, 'format':<STRING>}] \n
            format (String) [Optional]: The format the plot to be used. It is \
            empty by default. The format of the string should be:\
            "[marker][line][color]". For exploring the allowed values \
            for all the three please look into the matplotlib official \
            documentation. \n
            Note: The firstAxisData should be of same datatype. Otherwise the \
            plotted graph can be ambiguous.\n
        """
        
        figure, axes = pyplot.subplots();
        for index, dict in enumerate(listOfDicts):
            self.__plotDataInLinePlot(axes, dict['firstAxisData'], 
                                    dict['secondAxisData'], dict['format'], 
                                    dict['plotLabel']);
            axes.legend();
        return;


    def generateSimpleBarPlot(self, plotLabel, xLabel, yLabel, firstAxisData, 
                               secondAxisData):
        """Plots bar graph in a 2D plane.
        
        Used for 2D plots only. The function internally sets plotLabel, xLabel, \
        yLabel. The plot uses the data given in firstAxisData and \
        secondAxisData. It uses a single axes object given by pyplot.subplots().

        Args:
            plotLabel (String): Title of the plot.\n
            xLabel (String): The label of the x axis in the plot.\n
            yLabel (String): The label of the y axis in the plot.\n
            firstAxisData (Array): The x axis data in the plot.\n
            secondAxisData (Array): The y axis data in the plot.
        """
        
        figure, axes = pyplot.subplots();
        self.__initializePlotTitleAndLabels(axes, plotLabel, xLabel, yLabel);
        self.__plotDataInBarPlot(axes, firstAxisData, secondAxisData);
        return;


    def generateMultipleBarPlots(self, listOfDicts):
        """Plots the list of data as bar graph in separate plots.
        
        Used for 2D plots only. The function internally uses \
        subplots(num. of rows, 4), to generate group of plots with 4 in a row.\
        The number of plots will be equal to the size of the listOfDictionaries\
        given. 

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL_OF_PLOT>, 'xLabel':<STRING_AS_X_LABEL>, \
                'yLabel':<STRING_AS_Y_LABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>, 'format':<STRING>}]
        """
        
        size = len(listOfDicts);
        figure, axes = None, None;
        
        if (size <= 4):
            figure, axes = pyplot.subplots(1, size);
        else:
            figure, axes = pyplot.subplots((math.floor(size / 4) + 1), 4);
        
        for index, dict in enumerate(listOfDicts):
            self.__initializePlotTitleAndLabels(axes[index], dict['plotLabel'], 
                                                dict['xLabel'], dict['yLabel']);
            self.__plotDataInBarPlot(axes[index], dict['firstAxisData'], 
                                    dict['secondAxisData']);
        return;


    def generateMultipleOverlappedBarPlots(self, listOfDicts):
        """Plots the list of data as bar graph in the same plot.
        
        Used for 2D plots only. The function internally uses \
        pyplot.subplots(), to generate a plot.

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>}] \n
            Note: The firstAxisData should be of same datatype. Otherwise the \
            plotted graph can be ambiguous.\n
        """
        
        figure, axes = pyplot.subplots();
        for index, dict in enumerate(listOfDicts):
            self.__plotDataInBarPlot(axes, dict['firstAxisData'], 
                                    dict['secondAxisData'], dict['plotLabel']);
            axes.legend();
        return;
    
    
    def generateSimpleScatterPlot(self, plotLabel, xLabel, yLabel, firstAxisData, 
                               secondAxisData, color = 0.5):
        """Plots scatter graph in a 2D plane.
        
        Used for 2D plots only. The function internally sets plotLabel, xLabel, \
        yLabel. The plot uses the data given in firstAxisData and \
        secondAxisData. It uses a single axes object given by pyplot.subplots().

        Args:
            plotLabel (String): Title of the plot.\n
            xLabel (String): The label of the x axis in the plot.\n
            yLabel (String): The label of the y axis in the plot.\n
            firstAxisData (Array): The x axis data in the plot.\n
            secondAxisData (Array): The y axis data in the plot.\n
            color (Scalar): The color of the marker.
        """
        
        figure, axes = pyplot.subplots();
        self.__initializePlotTitleAndLabels(axes, plotLabel, xLabel, yLabel);
        self.__plotDataInScatterPlot(axes, firstAxisData, secondAxisData, 
                                     color);
        return;


    def generateMultipleScatterPlots(self, listOfDicts):
        """Plots the list of data as scatter graph in separate plots.
        
        Used for 2D plots only. The function internally uses \
        subplots(num. of rows, 4), to generate group of plots with 4 in a row.\
        The number of plots will be equal to the size of the listOfDictionaries\
        given. 

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL_OF_PLOT>, 'xLabel':<STRING_AS_X_LABEL>, \
                'yLabel':<STRING_AS_Y_LABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>, 'color':<COLOR>}]
        """
        
        size = len(listOfDicts);
        figure, axes = None, None;
        
        if (size <= 4):
            figure, axes = pyplot.subplots(1, size);
        else:
            figure, axes = pyplot.subplots((math.floor(size / 4) + 1), 4);
        
        for index, dict in enumerate(listOfDicts):
            self.__initializePlotTitleAndLabels(axes[index], dict['plotLabel'], 
                                                dict['xLabel'], dict['yLabel']);
            self.__plotDataInScatterPlot(axes[index], dict['firstAxisData'], 
                                    dict['secondAxisData'], dict['color']);
        return;


    def generateMultipleOverlappedScatterPlots(self, listOfDicts):
        """Plots the list of data as scatter graph in the same plot.
        
        Used for 2D plots only. The function internally uses \
        pyplot.subplots(), to generate a plot.

        Args:
            listIfDictionaries (List of dictionaries): This should contain a list\ 
            of dictionaries with the following format:\n
                [{'plotLabel':<STRING_lABEL>, 'firstAxisData':<DATA_array_FOR_X_AXIS>, \
                'secondAxisData':<DATA_ARRAY_FOR_Y_AXIS>, 'color':<COLOR>}] \n
            Note: The firstAxisData should be of same datatype. Otherwise the \
            plotted graph can be ambiguous.\n
        """
        
        figure, axes = pyplot.subplots();
        for index, dict in enumerate(listOfDicts):
            self.__plotDataInScatterPlot(axes, dict['firstAxisData'], 
                                    dict['secondAxisData'], dict['color'], 
                                    label = dict['plotLabel']);
            axes.legend();
        return;


    def __plotDataInLinePlot(self, axes, firstAxisData, secondAxisData, fmt, label = ''):
        """Plots line graph using firstAxisData and secondAxisData. 
        
        Used for 2D plots only. The x label, y label, plot title, etc should \
        ce set in axes before calling this function.

        Args:
            axes (Axes): Axes object\n
            firstAxisData (Array): Array of objects for the x axis of the plot\n
            secodnAxisData (Array): Array of objects for the y axis of the plot\n
            fmt (String) [Optional]: The format the plot to be used. It is \
            empty by default. The format of the string should be:\
            "[marker][line][color]". For exploring the allowed values \
            for all the three please look into the matplotlib official \
            documentation. \n
            label (String): label of the plot.\n
            
        Returns:
            lines (List(Line2D)): A list of Line2D representing plot of data
        """
        
        lines = axes.plot(firstAxisData, secondAxisData, fmt, label = label);
        return lines;
        

    def __plotDataInBarPlot(self, axes, firstAxisData, secondAxisData, label = ''):
        """Plots bar graph using firstAxisData and secondAxisData. 
        
        Used for 2D plots only. The x label, y label, plot title, etc should \
        be set in axes before calling this function.

        Args:
            axes (Axes): Axes object\n
            firstAxisData (Array): Array of objects for the x axis of the plot\n
            secodnAxisData (Array): Array of objects for the y axis of the plot\n
            label (String): label of the plot.\n
            
        Returns:
            lines (List(Line2D)): A list of Line2D representing plot of data
        """
        
        lines = axes.bar(firstAxisData, secondAxisData, label = label);
        return lines;
    
    
    def __plotDataInScatterPlot(self, axes, firstAxisData, secondAxisData, 
                                color, label = ''):
        """Plots scatter graph using firstAxisData and secondAxisData. 
        
        Used for 2D plots only. The x label, y label, plot title, etc should \
        be set in axes before calling this function.

        Args:
            axes (Axes): Axes object\n
            firstAxisData (Array): Array of objects for the x axis of the plot\n
            secodnAxisData (Array): Array of objects for the y axis of the plot\n
            color (Number): Number for color for representing data\n
            label (String): label of the plot.\n
            
        Returns:
            lines (List(Line2D)): A list of Line2D representing plot of data
        """
        
        lines = axes.scatter(firstAxisData, secondAxisData, color, 
                             label = label);
        return lines;


    def __initializePlotTitleAndLabels(self, axes, plotLabel, xLabel, yLabel):
        """Initializes axes with the provided labels.
        

        Args:
            axes (Axes): Axes object\n
            plotLabel (String): Title of the plot.\n
            xLabel (String): The label of the x axis in the plot.\n
            yLabel (String): The label of the y axis in the plot.

        """
        
        axes.set_title(plotLabel);
        axes.set_xlabel(xLabel);
        axes.set_ylabel(yLabel);
        return;


    def generateSamplePlot(self):
        """Generates a sample plot.
        
        Uses title as samplePlot, x axis label as xLabel, y axis label as \
        yLabel, and data as xAxis = [1,2,3,4], yAxis = [1,3,5,3].
        """
        
        self.generateSimpleLinePlot("samplePlot", "x Axis", "y Axis", 
                                   ['a', 'b', 'c', 'd'], [1,3,5,8]);
        
        listOfDicts =  [{'plotLabel':"plot 1", 'xLabel':"xLabel 1", 
                'yLabel':"yLabel 1", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,3,5,7], 'format':'b-'},
                 {'plotLabel':"plot 2", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,2,9,2], 'format':'r^'},
                {'plotLabel':"plot 3", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,3,5,8], 
                'secondAxisData':[1,5,10,1], 'format':'b^'}];
        
        self.generateMultipleLinePlots(listOfDicts);
        self.generateMultipleOverlappedLinePlots(listOfDicts);
        
        
        self.generateSimpleBarPlot("samplePlot", "x Axis", "y Axis", 
                                   ['a', 'b', 'c', 'd'], [1,3,5,8]);
        
        listOfDicts =  [{'plotLabel':"plot 1", 'xLabel':"xLabel 1", 
                'yLabel':"yLabel 1", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,3,5,7]},
                 {'plotLabel':"plot 2", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,2,9,2]},
                {'plotLabel':"plot 3", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,3,5,8], 
                'secondAxisData':[1,5,10,1]}];
        
        self.generateMultipleBarPlots(listOfDicts);
        self.generateMultipleOverlappedBarPlots(listOfDicts);
        
        
        self.generateSimpleScatterPlot("samplePlot", "x Axis", "y Axis", 
                                   ['a', 'b', 'c', 'd'], [1,3,5,8], 0.5);
        
        listOfDicts =  [{'plotLabel':"plot 1", 'xLabel':"xLabel 1", 
                'yLabel':"yLabel 1", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,3,5,7], 'color':0.25, 'size':10**2},
                 {'plotLabel':"plot 2", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,2,3,4], 
                'secondAxisData':[1,2,9,2], 'color':0.5, 'size':10**2},
                {'plotLabel':"plot 3", 'xLabel':"xLabel 2", 
                'yLabel':"yLabel 2", 'firstAxisData':[1,3,5,8], 
                'secondAxisData':[1,5,10,1], 'color':0.75, 'size':10**2}];
        
        self.generateMultipleScatterPlots(listOfDicts);
        self.generateMultipleOverlappedScatterPlots(listOfDicts);
        
        
        return;


matplotlib.use('qt5agg'); # Not recommended
twoDimensionalDataVisualisation = TwoDimensionalDataVisualisation();
twoDimensionalDataVisualisation.generateSamplePlot();