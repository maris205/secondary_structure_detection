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
        #print key,value

#将feature file的特征加到 pre dict file之后
#初始的pre dict file应该是word + "\t" + label
if __name__=="__main__":
    if len(sys.argv) != 4:
        print "please input feature file, pre dict file, feature id"
        sys.exit()

    #load dict
    load_dict(sys.argv[1])

    #读取新的字典文件
    dict_file = open(sys.argv[2], "r")
    feature_id = sys.argv[3]

    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        
        if word_dict.has_key(key):
            print sequence + " " + feature_id + ":" + str(word_dict[key])
        else: #no this feature
            print sequence + " " + feature_id + ":0" 
    
