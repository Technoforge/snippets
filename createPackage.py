# Python script to create package templates.

# IMPORT MODULES.

import os, sys, shutil, datetime

# GLOBAL VARIABLES

# The directory in which you are running the script.

sourceDirectory = './'

# The name passed in to this script.

packageName = sys.argv[1]

# This will be your new package name.

destinationDirectory = packageName+'/'

# Full path to destination directory.

path = os.path.join(sourceDirectory, destinationDirectory)

# Store file names.

fileName = ''

# A list of files created by this script.

listOfPackageFiles = []

# Set directory access mode.

mode = 0o666

# Get current date and time.

now = datetime.datetime.now()

# FUNCTIONS

def createFile(fileName, fileContent):
       with open(fileName, 'w') as f:
              f.write(fileContent)

def moveFiles(listOfPackageFiles):
       for f in listOfPackageFiles:
              src = sourceDirectory+f
              dst = destinationDirectory+f
              shutil.move(src, dst)

# Check if the package path already exists, and if so, print a message and quit.

if(os.path.exists(path)):
       print('That package already exists. Try another name.')
       quit()

# Create package directory.

try:
       os.mkdir(path, mode)
except OSError as error:
       print(error)

# Create setup.cfg file content.

fileContent = """[metadata]
name = packageMaker
version = 0.0.1
author = Your Name
author_email = some@email.com
description = Bare bones Python package creation.
long_description = file: read.me
long_description_content_type = text/markdown
url = https://www.technoforge.com.au
license_files = licence.me
classifiers =
       Programming Language :: Python :: 3
       Licence :: Technoforge FOSS Licence
       Operating System :: OS Independent
[options]
packages = find:
       python_requires = >=3.7
       include_package_data = True"""

# Create the setup.cfg file.

fileName = 'setup.cfg'

# Send file name and content to createFile function.

createFile(fileName, fileContent)

# Add that file to the list of files.

listOfPackageFiles.append(fileName)

# Create __init__.py file content (null).

fileContent = ""
fileName = '__init__.py'
createFile(fileName, fileContent)
listOfPackageFiles.append(fileName)

# Create licence.me file content.

fileContent = packageName + " Insert whatever licence information you like."
fileName = 'licence.me'
createFile(fileName, fileContent)
listOfPackageFiles.append(fileName)

# Create the read.me file.

fileContent = packageName + " Insert whatever readme information you like."
fileName = 'read.me'
createFile(fileName, fileContent)
listOfPackageFiles.append(fileName)

# Create the main.py file.

fileContent = "# " + packageName + "\n# " + now.strftime('%Y-%m-%d') + "\n# Purpose: \n"
fileName = 'main.py'
createFile(fileName, fileContent)
listOfPackageFiles.append(fileName)

# Move files into package folder.

moveFiles(listOfPackageFiles)

# Send a message saying the job is done.

print('\nPackage ' + packageName + ' created. Have a nice day!\n')