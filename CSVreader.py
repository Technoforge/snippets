# A short program for importing data from a CSV file and analysing the contents.
# A CSV file is just a text file full of Comma Separated Values, easy to import
# into all sorts of programs. Example:
# Name,age,height
# Bob,25,180
# Mary,30,170

# Import the pandas code library and functions.
import pandas

# Import a CSV file full of data.
# This function from the pandas code library requires:
# - The path and name of the file.
# - The separator used in the file.
# - What to do when a column has no data.
df = pandas.read_csv('myData.csv', sep=',', na_values='.')

# Now I have stored the data from the CSV into my variable called df.
# Pandas code turns that data into what its authors called a DATAFRAME.
# A dataframe is a table. So now I have a table of data called df.
# Now I'll print my dataframe, df, to see if it worked.
print(df)
