#!/usr/bin/env python
#coding=utf-8
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')
#ngram切分获得边界稳定性
#只要top100万的词的
g_border_length = 1 #边界的长度
g_max_word_length = 12 #最大的词的长度


def initial_dict(filename, word_dict):
    dict_file = open(filename, "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#输出所有词"\t"右边词
def get_right_border(line, word_length):
    gram_n = word_length + g_border_length  #ngram的片段长度，为词的长度+边界长度
    #获得ngram切分
    for i in range(len(line)-gram_n+1):
        word = "".join(line[i:i+word_length])
        right_word = "".join(line[i+word_length:i+word_length+g_border_length])
        if word_dict.has_key(word):
            print word + "\t" + right_word
    return 0

#输出所有词"\t"右边词
def get_left_border(line, word_length):
    word_list = line.split(" ")
    gram_n = word_length + g_border_length  #ngram的片段长度，为词的长度+边界长度
    for i in range(len(line)-gram_n+1):
        #获得ngram切分
        left_word = "".join(line[i:i+g_border_length])
        word = "".join(line[i+g_border_length:i+word_length+g_border_length])
        if word_dict.has_key(word):
            print word + "\t" + left_word
    return 0

#加载词典
dict_file_name = "data.dict" 
word_dict = {}
initial_dict(dict_file_name, word_dict)

for line in sys.stdin:
    line = line.strip()
    for word_length in range(1, g_max_word_length+1):
        try:
            get_right_border(line, word_length)
        except:
            continue
