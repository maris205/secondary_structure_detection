#!/usr/bin/env python
#coding=utf-8
import math
import sys

#计算两个词典的差异
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
        print "please input ori dict file and new dict file name"
        sys.exit()

    #load ori file
    load_dict(sys.argv[1])

    #读取新的字典文件
    diff_sum = 0
    dict_file = open(sys.argv[2], "r")
    num = 0
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        if word_dict.has_key(key):
            diff = abs(word_dict[key] - value)
            diff_sum += diff
            num += 1

    print "all diff",diff_sum
    print "average diff",diff_sum/num
