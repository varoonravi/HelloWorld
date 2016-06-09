#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  l = [] 
  b=[]
  g=[]
  input_dir = r"E:Python Exercises\Google Exercises\google-python-exercises\babynames"
  input_filename = input_dir + '\\' + filename
  output_filename = r'E:\output1.txt'
  print input_filename, output_filename
  
  o = open(input_filename, 'a')
  pattern = '.html$'
  match = re.search(pattern, filename)
  year = filename[5:match.start()]
  o.write("*******************************"+year+"***********************************")
  o.write("\n")
  
  
  f = open(filename,'r')
  for i in f:
    m = re.search(r'<tr align="right"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', i)
    if m:
       
        seperator = ':'       
        rank, boy, girl =  m.groups()
        b.append(boy + " " + rank)
        g.append(girl +" " + rank)
#        g.append(girl)
#        g.append(rank)
#        bb.append( seperator.join(b))
#        gg.append( seperator.join(g))
        
        
      
        l.append(seperator.join(m.groups()))
     
#  for i in bb:
#      print i
#      print "\n"
#  for i in gg:
#      print i
#      print "\n"

  b.append('**************************************')
  g.append('**************************************')
  
  
  o.write("\n")
  o.write("Boys")
  o.write("\n")
  for i in sorted(b):
      o.write(i)
      o.write('\n')
  
  o.write("\n")    
  o.write("Girls")
  o.write("\n")    
  for i in sorted(g):
      o.write(i)
      o.write('\n')
      
  
        
  

  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
#  
#  f = open('E:\Python Exercises\Google Exercises\google-python-exercises\babynames\filename','r')
#  match = re.findall(r'\w?',f.read(),re.IGNORECASE)
#  print match.group()
#      
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for i in args:
      extract_names(i)
  
if __name__ == '__main__':
  main()
  