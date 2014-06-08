#!/usr/bin/env python
#coding=utf-8
import math
import sys

#抽取ngram的特征，并标记上是否是词的label
word_dict={}
#装载词典
def load_dict(dict_file_name):
    #加载初始词典
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input dict file and feature file name"
        sys.exit()

    #load dict
    load_dict(sys.argv[1])

    #读取新的字典文件
    dict_file = open(sys.argv[2], "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        
        if word_dict.has_key(key):
            print key + "\t" + str(value) + "\t1" #is word
        else:
            print key + "\t" + str(value) + "\t0" #not word
    
