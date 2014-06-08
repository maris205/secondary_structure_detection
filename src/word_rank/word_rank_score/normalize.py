#!/usr/bin/env python
#coding=utf-8
import sys
import math

#L2����

word_dict_count = {}
word_dict = {}

#���شʵ䣬Ϊ��\t��Ƶ�ĸ�ʽ
def initial_dict(filename):
    dict_file = open(filename, "r")
    l2_sum = 0
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict_count[key] = value
        l2_sum += value*value
    
    l2_sum_sqrt = l2_sum**(0.5) #����
    #����ÿ�������򻯺��ֵ
    for key in word_dict_count:
        value = word_dict_count[key]
        l2_value = value/l2_sum_sqrt   
        print key + "\t" + str(l2_value)
#main
if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input dict file"
        sys.exit()
    
    initial_dict(sys.argv[1])
