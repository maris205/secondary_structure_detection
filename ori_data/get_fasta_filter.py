#!/usr/bin/env python
#coding=utf-8
import sys
import random
import re
import random
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()

    data_file = open(sys.argv[1], "r")
    i = 0
    seq = ""
    seq_list = []
    for line in data_file:
        line = line.replace("\n","") #注意，不要用strip，否则会去掉空格
        if line.find(">") == 0: #如果发现序列开头
            if seq!="":
                seq_list.append(seq)#加入序列队列
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
        seq = seq_list[i+1]
        stu = seq_list[i+3]
        
        if seq.find("X") != -1: #如果序列中包含X，未知字符，则略去
            continue
        if len(seq) < 80: #delete sequence length less than 80
            continue

        stu = stu.replace(" ","X") #stu中的空格换成X，方便后续处理
        print pdb_id
        print seq
