#!/usr/bin/env python
#coding=utf-8
import sys
import random
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')
#get fasta format file from structure file


if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()

    data_file = open(sys.argv[1], "r")
    i = 0
    seq = ""
    seq_list = []
    for line in data_file:
        line = line.replace("\n","") 
        if line.find(">") == 0: #head of a record
            if seq!="":
                seq_list.append(seq)
                seq = ""
            line = line.split(":")[0] + ":" + line.split(":")[1]
            seq_list.append(line)
        else:
            if line.find(">") == -1:
                seq += line
    #last line
    seq_list.append(seq)
    
    for i in range(0,len(seq_list),4):
        pdb_id = seq_list[i] #pdb id
        seq = seq_list[i+1] #protein sequence 
        stu = seq_list[i+3] #secondary structure
        
        if seq.find("X") != -1: #delete sequence containing unkown letter
            continue
        if len(seq) < 30: #delete sequence length less than 30
            continue

        print pdb_id
        print seq
