#!/usr/bin/env python
#coding=utf-8
import sys 
import math
#�ϲ����ұ߽��أ�ȡС�ģ�û�еĿ�����0
#he ,she�����Ļ᲻�ᱻ�ɵ�

if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input left and right border info file name"
        sys.exit()

    left_file = open(sys.argv[1], "r")
    left_info_dict = {}
    for line in left_file:
        line = line.strip()
        word = line.split("\t")[0]
        info = float(line.split("\t")[1])
        left_info_dict[word] = info

    #�����ұ߽��أ�û�еľͲ�Ҫ�ˣ�������0
    right_file = open(sys.argv[2], "r")
    border_info = {}
    for line in right_file:
        line = line.strip()
        word = line.split("\t")[0]
        info = float(line.split("\t")[1])
        if left_info_dict.has_key(word):#������������б߽���
                border_info[word] = 35.0 + math.log(info*left_info_dict[word])

    #�������
    border_info_list = sorted(border_info.iteritems(), key=lambda d:d[1], \
            reverse=True)
    for key,value in border_info_list:
        #if value > 0:#����0�Ĳ�Ҫ
        print key + "\t" + str(value)
