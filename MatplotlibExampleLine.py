# Here is an example of a LINE chart using the matplotlib code library.

# Import matplpotlib and give it a shorter name.
import matplotlib.pyplot as plt

# Import the NumPy library for numeric functions.
import numpy

# Create an array of X points.
xpoints = numpy.array([1,2,3,4,5,6])

# Create an array of Y points.
ypoints = numpy.array([5,8,3,6,1,6])

# Create the LINE chart.
plt.plot(xpoints, ypoints)

# Show the created chart.
plt.show()
