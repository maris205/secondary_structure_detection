#!/usr/bin/env python
#coding=utf-8
import sys
import random
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')
#get filtered data
#example,./get_experiment_data.py ss.fasta.uniq.pid ss.txt

if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please pid file and original structure file name"
        sys.exit()

    
    id_dict = {}
    dict_file = open(sys.argv[1], "r")
    for line in dict_file:
        line = line.strip()
        id_dict.setdefault(line,1)
 
    data_file = open(sys.argv[2], "r")
    i = 0
    seq = ""
    seq_list = []
    for line in data_file:
        line = line.replace("\n","") #
        if line.find(">") == 0: #find head of a record
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
        pdb_id = seq_list[i]
        seq = seq_list[i+1] #protein sequence
        stu = seq_list[i+3] #structure
        if seq.find("X") != -1: #delete sequence containing unknown 
            continue

        if id_dict.has_key(pdb_id):
            stu = stu.replace(" ","X") #convert space to X in structure
            print seq
            print stu
            print ""
