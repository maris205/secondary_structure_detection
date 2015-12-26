#!/usr/bin/env python
#coding=utf-8
import sys 
#��ôʵ����ǴʵĲ���

BORDER_INFO_THRESHOLD = 2
if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input dict and border info file name"
        sys.exit()

    word_file = open(sys.argv[1], "r")
    word_dict = {}
    for line in word_file:
        line = line.strip()
        word = line.split("\t")[0]
        freq = float(line.split("\t")[1])
        word_dict[word] = freq

    #�����ұ߽��أ�û�еľͲ�Ҫ�ˣ�������0
    info_file = open(sys.argv[2], "r")
    for line in info_file:
        line = line.strip()
        word = line.split("\t")[0]
        value = float(line.split("\t")[1])
        if word_dict.has_key(word):#������������б߽���
            if len(word)==1: #����ĸ���ʣ����뱣��
                print word + "\t" + str(word_dict[word])
                continue
            if value > BORDER_INFO_THRESHOLD:
                print word + "\t" + str(word_dict[word])
