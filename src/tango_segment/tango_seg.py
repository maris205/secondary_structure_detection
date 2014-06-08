#!/usr/bin/env python
#coding=utf-8
import math
import sys 
#����mi���зִ�

word_dict = {}

#���شʵ�
def load_dict(dict_file_name):
    #���س�ʼ�ʵ�
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict_count[key] = value
    #������Ƶ��
    all_freq = sum(word_dict_count.itervalues()) #���дʵĴ�Ƶ
    #����ÿ���ʵĸ���
    for key in word_dict_count:
        value = word_dict_count[key]
        word_dict[key] = value


def get_mi(start, ngram_seg, mi_dict):
    for i in range(1,len(ngram_seg)):
        left_seg = ngram_seg[0:i]
        right_seg = ngram_seg[i:]
        mi = word_dict[ngram_seg]/(word_dict[left_seg]*word_dict[right_seg])
        #print left_seg, right_seg, mi
        
        #�洢
        pos = start + i
        mi_dict.setdefault(pos,[])
        mi_dict[pos].append(mi)
        #print mi_dict


#���л���mi�ķִ�
#ͳ�Ƶ����ݽ����key�Ƿָ��λ�ã�value��һ��list���洢���ֿ��ܵ�mi
def mi_seg(line):
    #ngram segment , ���ÿ��ngramƬ�ε������ָ���mi
    ngram_length = 4
    mi_dict = {}
    for i in range(0,len(line)-ngram_length+1):
        start = i
        ngram_seg = "".join(line[i:i+ngram_length])
        #print ngram_seg
        get_mi(start, ngram_seg, mi_dict)
    
    #print mi_dict
    #ͳ��
    pos_mi_list = []
    for pos in mi_dict:
        mi_list = mi_dict[pos]
        mi_avg = sum(mi_list)/len(mi_list)
        pos_mi_list.append( (pos, mi_avg) )
        #print mi_avg
    print pos_mi_list 

#��ʼ����
#���ȼ��شʵ�
dict_file_name = "swiss_4.dict"
load_dict(dict_file_name)

for line in sys.stdin:
    line = line.strip()
    #����ʵ����з����Ȩֵ
    mi_seg(line)
     

    """
    mi_dict = {}
    start = 0
    ngram_seg = "KKYD"
    get_mi(start, ngram_seg, mi_dict)
    """
