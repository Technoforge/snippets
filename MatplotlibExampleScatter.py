# Here is an example of a SCATTER chart using the matplotlib code library.

# Import matplpotlib and give it a shorter name.
import matplotlib.pyplot as plt

# Import the NumPy library for numeric functions.
import numpy

# Create an array of X points.
xpoints = numpy.array([4,2,7,5,2,6])

# Create an array of Y points.
ypoints = numpy.array([5,8,3,6,1,6])

# Create the SCATTER chart.
plt.scatter(xpoints, ypoints)

# Show the created graph or chart.
plt.show()
