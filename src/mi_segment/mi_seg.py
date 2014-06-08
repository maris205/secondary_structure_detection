#!/usr/bin/env python
#coding=utf-8
import math
import sys 
#根据mi进行分词

g_max_word_length = 10 #最大的切分片段的长度，也就是最大的词长度
word_dict = {}
g_all_freq = 0

#加载词典
def load_dict(dict_file_name):
    #加载初始词典
    global g_all_freq
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict_count[key] = value
    #计算总频率
    g_all_freq = sum(word_dict_count.itervalues()) #所有词的词频
    #计算每个词的概率
    for key in word_dict_count:
        value = word_dict_count[key]
        word_dict[key] = value/g_all_freq

#获得片段的概率
def get_prob(ngram_seg):
    global g_all_freq
    if word_dict.has_key(ngram_seg):
        return word_dict[ngram_seg]
    else: #+1平滑
        #return 10./(g_all_freq*10**len(ngram_seg))
        return 7.07914797767e-100

def get_mi(start, ngram_seg, mi_dict):
    for i in range(1,len(ngram_seg)):
        left_seg = ngram_seg[0:i]
        right_seg = ngram_seg[i:]
        mi = get_prob(ngram_seg)/(get_prob(left_seg)*get_prob(right_seg))
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
    ngram_length = g_max_word_length
    mi_dict = {}
    for i in range(0,len(line)-ngram_length+1):
        start = i
        ngram_seg = "".join(line[i:i+ngram_length])
        #print ngram_seg
        get_mi(start, ngram_seg, mi_dict)
    
    #print mi_dict
    #统计
    pos_mi_list = []
    pos_mi_list.append( (0,0) ) #begin pos
    for pos in mi_dict:
        mi_list = mi_dict[pos]
        mi_avg = sum(mi_list)/len(mi_list)
        pos_mi_list.append( (pos, mi_avg) )
        #print mi_avg
    pos_mi_list.append( (0,0) ) #end pos

    #print pos_mi_list 
    seg_pos_list = []
    seg_pos_list.append(0) # first node
    for i in range(1, len(pos_mi_list)-1):
        cur = pos_mi_list[i][1] 
        pre = pos_mi_list[i-1][1]
        next = pos_mi_list[i+1][1]
        pos = pos_mi_list[i][0] 
        if cur<pre and cur<next:
            seg_pos_list.append(pos)

    seg_pos_list.append(len(line)) # last node
    #print seg_pos_list

    #构建分词
    word_list = []
    for i in range(len(seg_pos_list)-1):
        left = seg_pos_list[i]
        right = seg_pos_list[i + 1]
        word = line[left:right]
        word_list.append(word)
    
    seg_sequence = " ".join(word_list)
    #print  seg_sequence
    return seg_sequence


#开始运行
#首先加载词典
dict_file_name = "dict_9"
load_dict(dict_file_name)

for line in sys.stdin:
    line = line.strip()
    #输出词的所有分配的权值
    print mi_seg(line)
     

    """
    mi_dict = {}
    start = 0
    ngram_seg = "KKYD"
    get_mi(start, ngram_seg, mi_dict)
    """
