#!/usr/bin/env python

import sys, re, csv

def main(path):
    #line=sys.stdin.readline()
    output=[]
    output2=[]
    s=''
    with open(path,'r') as f:
        reader = csv.reader(f, delimiter="\t")
        if path=="C:\\WPI\\BigData\\Quiz2\\matrix\\matrix_m.txt":
            for row in reader:
                row=str(row[1])"\t"
               s+=  + "\t"+ "[M,"+row[0]+ ","+row[2]+"]")
        if path=="C:\\WPI\\BigData\\Quiz2\\matrix\\matrix_n.txt":
            for row in reader:
                oprint(row[0]  + "\t"+ "[N,"++row[1]+","+row[2]+"]")

    for i in output:
        print(output)
       

 
path1="C:\\WPI\\BigData\\Quiz2\\matrix\\matrix_m.txt"

main(path1)  
