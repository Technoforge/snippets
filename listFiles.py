# List files in directory as links in webpage.

import os 
mydir='/home/fluffy/Pictures'
outputfile = open("filelist.html", "w+")
print("<html><body><h1>Files.</h1><ul>", file=outputfile)
for x in os.listdir(mydir):
      if x.endswith(".jpg"):
            print("{}{}{}{}{}".format('<li><a href=\"', x, '\">', x, '</a></li>'), file=outputfile)
print("</ul></body></html>", file=outputfile)
outputfile.close()
