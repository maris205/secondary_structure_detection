#!/usr/bin/env python
#coding=utf-8
import math
import sys 
#根据mi进行分词

word_dict = {}

#加载词典
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
        word_dict[key] = value


def get_mi(start, ngram_seg, mi_dict):
    for i in range(1,len(ngram_seg)):
        left_seg = ngram_seg[0:i]
        right_seg = ngram_seg[i:]
        mi = word_dict[ngram_seg]/(word_dict[left_seg]*word_dict[right_seg])
        #print left_seg, right_seg, mi
        
        #存储
        pos = start + i
        mi_dict.setdefault(pos,[])
        mi_dict[pos].append(mi)
        #print mi_dict


#进行基于mi的分词
#统计的数据结果，key是分割点位置，value是一个list，存储几种可能的mi
def mi_seg(line):
    #ngram segment , 获得每个ngram片段的三个分割点的mi
    ngram_length = 4
    mi_dict = {}
    for i in range(0,len(line)-ngram_length+1):
        start = i
        ngram_seg = "".join(line[i:i+ngram_length])
        #print ngram_seg
        get_mi(start, ngram_seg, mi_dict)
    
    #print mi_dict
    #统计
    pos_mi_list = []
    for pos in mi_dict:
        mi_list = mi_dict[pos]
        mi_avg = sum(mi_list)/len(mi_list)
        pos_mi_list.append( (pos, mi_avg) )
        #print mi_avg
    print pos_mi_list 

#开始运行
#首先加载词典
dict_file_name = "swiss_4.dict"
load_dict(dict_file_name)

for line in sys.stdin:
    line = line.strip()
    #输出词的所有分配的权值
    mi_seg(line)
     

    """
    mi_dict = {}
    start = 0
    ngram_seg = "KKYD"
    get_mi(start, ngram_seg, mi_dict)
    """
