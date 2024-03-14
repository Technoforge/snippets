# List files in directory as links in webpage.

import os 
MyDir='/home/SomeFolder/Pictures'
OutputFile = open("FileList.html", "w+")
print("<html><body><h1>Files.</h1><ul>", file=OutputFile)
for x in os.listdir(MyDir):
      if x.endswith(".jpg"):
            print("{}{}{}{}{}".format('<li><a href=\"', x, '\">', x, '</a></li>'), file=OutputFile)
print("</ul></body></html>", file=OutputFile)
OutputFile.close()
