#!/usr/bin/python
import sys, re

def main(argv):
  line = sys.stdin.readline()
  row=line.split('\t')
  try:
    while line:
      for val in row:
        print "LongValueSum:" + str(val)+ "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)
