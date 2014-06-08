#!/usr/bin/env python
#coding=utf-8
import sys 
import random
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')

def convert(stu_list):
    new_list = []
    for item in stu_list:
        if item in ["H","E","C"]:
            new_list.append(item)
        elif item == "G":
            new_list.append("H")
        elif item == "B":
            new_list.append("E")
        else:
            new_list.append("C")
    return new_list

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()

    data_file = open(sys.argv[1], "r")
    line_list = data_file.readlines()
    for i in range(0,len(line_list),3):
        seq_line = line_list[i].strip()
        stu_line = line_list[i+1].strip()

        stu_list = stu_line

        stu_list = convert(stu_list)
        stu_out = "".join(stu_list)
        
        print seq_line
        print stu_out.strip()
        print ""
