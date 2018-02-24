#!/usr/bin/python
import sys, re

def main(argv):
  file=os.environ["map_input_file"]
  line = sys.stdin.readline()
  pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
  try:
    while line:
      for word in pattern.findall(line):
        print "LongValueSum:" + file + "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)
