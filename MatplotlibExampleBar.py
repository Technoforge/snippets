# Here is an example of a BAR chart using the matplotlib code library.

# Import matplpotlib and give it a shorter name.
import matplotlib.pyplot as plt

# Import the NumPy library for numeric functions.
import numpy

# Create an array of X points.
xpoints = numpy.array(['Apples', 'Bananas', 'Oranges', 'Blueberries', 'Strawberries', 'Pears'])

# Create an array of Y points.
ypoints = numpy.array([5,8,3,6,1,6])

# Create the BAR chart.
plt.bar(xpoints, ypoints)

# Show the created graph or chart.
plt.show()
