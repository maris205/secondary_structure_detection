#!/usr/bin/env python
#coding=utf-8
import math
import sys

#��ȡngram����������������Ƿ��Ǵʵ�label
word_dict={}
#װ�شʵ�
def load_dict(dict_file_name):
    #���س�ʼ�ʵ�
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value
        #print key,value

#��feature file�������ӵ� pre dict file֮��
#��ʼ��pre dict fileӦ����word + "\t" + label
if __name__=="__main__":
    if len(sys.argv) != 4:
        print "please input feature file, pre dict file, feature id"
        sys.exit()

    #load dict
    load_dict(sys.argv[1])

    #��ȡ�µ��ֵ��ļ�
    dict_file = open(sys.argv[2], "r")
    feature_id = sys.argv[3]

    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        
        if word_dict.has_key(key):
            print sequence + " " + feature_id + ":" + str(word_dict[key])
        else: #no this feature
            print sequence + " " + feature_id + ":0" 
    
