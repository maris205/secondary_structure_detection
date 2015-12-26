#!/usr/bin/env python
#coding=utf-8
import math
import sys

word_dict={}

#加载词典，并归一化
def load_dict(dict_file_name):
    #加载初始词典
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict_count[key] = value
    #计算总频率
    all_freq = sum(word_dict_count.itervalues()) #所有词的词频
    #计算每个词的概率
    for key in word_dict_count:
        value = word_dict_count[key]
        word_dict[key] = value/all_freq

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()

    #load file
    load_dict(sys.argv[1])

    #out put
    for word in word_dict:
        print word + "\t" + str(word_dict[word])
