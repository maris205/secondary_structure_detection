#!/usr/bin/env python
#coding=utf-8
import sys 
import random
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    if len(sys.argv) != 4:
        print "please input acc file name and threshold (%)"
        sys.exit()
    
    data_file = open(sys.argv[1], "r")
    line_list = data_file.readlines()
    threshold = 0.01*float(sys.argv[2])
    threshold_h = 0.01*float(sys.argv[3])
    for i in range(0,len(line_list),4):
        seq = line_list[i+1].strip()
        acc = line_list[i+2].strip()
        if len(seq)<10:
            continue
        #print  ">" + str(i) + ":A"
        print line_list[i].strip()
        print seq.replace(" ","")
        acc_value_list = acc.split(" ")
        acc_st_list = []
        for item in acc_value_list:
            """
            if float(item)<=threshold:
                acc_st_list.append("B")
            else:
                acc_st_list.append("E")
            """
            
            if float(item)<threshold:
                acc_st_list.append("B")
            elif float(item)>=threshold_h:
                acc_st_list.append("E")
            else:
                acc_st_list.append("I")
            
        print "".join(acc_st_list)
        print ""
