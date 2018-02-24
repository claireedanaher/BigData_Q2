#!/usr/bin/python

import sys, re

def main(argv):
    file=os.environ["map_input_file"]
    line=sys.stdin.readline()
	try:
		while line:
			for val in line:
				print "LongValueSum:" + file + val+"\t" + "1"
		line = sys.stdin.readline()
    except "end of file":
        return None
if __name__ == "__main__":
  main(sys.argv)
                     
                