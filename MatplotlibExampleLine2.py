# Here is an example of a LINE chart without X points using the matplotlib code library.

# Import matplpotlib and give it a shorter name.
import matplotlib.pyplot as plt

# Import the NumPy library for numeric functions.
import numpy

# Similar to the previous example, but if we do NOT specify the 
# X points, Matplotlib will assume they are 1,2,3,4... etc.

# Create an array of Y points.
ypoints = numpy.array([5,8,3,6,1,6])

# Create the LINE chart.
# Because we didn't create an array of xpoints, we are only using ypoints.
plt.plot(ypoints)

# Show the created chart.
plt.show()
