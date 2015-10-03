'''
graphing.py
Frederik Roenn Stensaeth
10.03.15

Python program that reads a document filled with sentiment data and plots it
on a graph. The graph can only hold a certain number of data points, so it
updates (moves) whenever the number of data points becomes too high. 

Credit given to PythonProgramming.net for the general idea of the program.
'''

import matplotlib.pyplot as mplot
import matplotlib.animation as animation
from matplotlib import style

# Changing the style gives us a little nicer looking backframe for the graph.
style.use('ggplot')

figure = mplot.figure()
actual_plot = figure.add_subplot(1, 1, 1)

def update(i):
    lines_feed = open("stream.txt", 'r').read().split('\n')

    # Create lists to hold our data points.
    x_values, y_values = [], []

    x_point = 0
    y_point = 0

    # Only read the last 200 data points as we want to make the graph appear
    # to move when new data points are added.
    for line in lines_feed[-200:]:
        x_point += 1
        if "pos" in line:
            y_point += 1
        elif "neg" in line:
            y_point -= 0.5

        x_values.append(x_point)
        y_values.append(y_point)
        
    actual_plot.clear()
    actual_plot.plot(x_values,y_values, 'k')

ani = animation.FuncAnimation(figure, update, interval=1000)
# animation.FuncAnimation(figure, update, interval=1000)
mplot.show()