# Here is an example of a PIE chart using the matplotlib code library.

# Import matplpotlib and give it a shorter name.
import matplotlib.pyplot as plt

# Import the NumPy library for numeric functions.
import numpy

# Create an array of labels.
myLabels = numpy.array(['Apples', 'Bananas', 'Oranges', 'Blueberries', 'Strawberries', 'Pears'])

# Create an array of pie slices.
pieSlices = numpy.array([5,8,3,6,1,6])

# Create the PIE chart.
plt.pie(pieSlices, labels=myLabels)

# Show the created chart.
plt.show()
