#!/usr/bin/python
import sys, re

def main(argv):
  line = sys.stdin.readline()
  pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
  try:
    while line:
      for word in pattern.findall(line):
          import random	
          x = 1 / random.randint(0,1000)
          print "LongValueSum:" + word.lower() + "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)