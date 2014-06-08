#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import numpy

word_dict={}
#装载词典
def load_dict(dict_file_name):
    #加载初始词典
    dict_file = open(dict_file_name, "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value        

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input  data file name"
        sys.exit()

    load_dict(sys.argv[1])

    #step 1, 获得每个长度词的平均值
    len_word_list = {} #不同长度的词的列表，key为长度，value为对应长度的词的数值列表
    for word in word_dict:
        key = len(word)
        len_word_list.setdefault(key, [])
        len_word_list[key].append( word_dict[word] )
    
    max_word_length = len(len_word_list) #词的最大长度

    #求均值
    length_mean_score = {}
    for word_length in range(1,max_word_length+1):
        length_mean_score[word_length] = numpy.mean( len_word_list[word_length] )

    #print "均值",length_avg_score
    
    #求标准差
    length_std_score = {}
    for word_length in range(1,max_word_length+1):
        length_std_score[word_length] = \
                numpy.std( len_word_list[word_length], ddof=1  )

    #print "标准差", length_std_score

    #计算每个词的相对数值
    word_score = {}
    for word in word_dict:
        value = ( word_dict[word] - length_mean_score[len(word)] ) / length_std_score[len(word)]
        word_score[word] = value

    #sort
    word_score_list = sorted(word_score.iteritems(), key = lambda d:d[1], reverse=True)
    for key,value in word_score_list:
        print key + "\t" + str(value)
