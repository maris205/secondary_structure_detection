#!/usr/bin/env python
#coding=utf-8
import math
import sys

word_dict={}
g_max_word_length = 6

#获得一个句子中的每个词的累计概率,主要概率是原始的形式，而不是log形式
#否则想加就没有意义了
def getprob(sequence):
    s_left = []
    s_right = []

    #从左到右，计算左边词的累积概率
    #其实是分割点的概率累计
    for pos in range(0,len(sequence) + 1):
        if pos == 0:
            s_left.append(1) #0
            continue

        if pos < g_max_word_length:
            max_word_length=pos
        else:
            max_word_length = g_max_word_length

        prob = 0
        for length  in range(1, max_word_length+1):
            word = sequence[pos-length:pos]
            if word_dict.has_key(word):
                prob = prob + (word_dict[word]*s_left[pos-length])
        s_left.append(prob)

    #从右边到左边，计算累计概率，并计算词的概率
    #计算s_right，同时计算每个词的概率
    for pos in range(len(sequence),-1, -1):
        if pos == len(sequence) :
            s_right.append(1) #0
            continue

        if len(sequence)-pos < g_max_word_length:
            max_word_length = len(sequence)-pos
        else:
            max_word_length = g_max_word_length

        prob = 0
        for length  in range(1,max_word_length+1):
            word = sequence[pos:pos+length]
            if word_dict.has_key(word):
                prob = prob + word_dict[word]*s_right[len(sequence) - (pos+length)]
                increase = s_left[pos]*word_dict[word]*s_right[ len(sequence) \
                        - pos-length]/s_left[-1] #注意归一化
                print word + "\t" + str(increase)
        s_right.append(prob)
    return 0

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
        word_dict[key] = value/all_freq

#开始运行
#首先加载词典
dict_file_name = "dict_soft"
load_dict(dict_file_name)

for line in sys.stdin:
    line = line.strip()
    #输出词的所有分配的权值
    try:
        getprob(line)
    except:
        continue
