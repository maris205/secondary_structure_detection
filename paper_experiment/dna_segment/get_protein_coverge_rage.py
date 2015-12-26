#!/usr/bin/env python
#coding=utf-8
#get percentage of coding region
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_protein_region(seq):
    letter_sum = 0
    protein_sum = 0
    for word in seq.split(" "):
        letter_sum += len(word)
        if len(word)>1:
            protein_sum += len(word)
    return float(protein_sum)/letter_sum

if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input data filename"
        sys.exit()

    filename = sys.argv[1]
    data_file = open(filename,'r')
    for line in data_file:
        line = line.strip()
        if len(line)<5:
            continue
        per = get_protein_region(line)
        print per
