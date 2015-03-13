#!/usr/bin/env python
#coding=utf-8
import sys
import os
import math

current_word = None
current_word_value_list = []

#获得边界熵
def process_value_list(value_list):
    #step 1，词频统计
    word_dict = {}
    for word in value_list:
        word_dict.setdefault(word,0)
        word_dict[word] += 1

    #step 2,计算熵
    freq_sum = len(value_list) #总的词频
    info_sum = 0
    for word in word_dict:
        prob = float(word_dict[word])/freq_sum
        word_info = -1*prob*math.log(prob, 2) #单个边界词的熵
        info_sum = info_sum + word_info

    return str(info_sum)

for line in sys.stdin:
    line = line.strip()
    (word,count) = line.split("\t")
    
    if current_word == word:#如果词没有变，则累加
        current_word_value_list.append(count)
    else:#如果词发生变化了,则输出
        if current_word != None: 
            #如果读的是第一行，和 None不一致,但不输出，不是第一行才输出
            #输出上一个词
            try:
                print current_word + "\t" + process_value_list(current_word_value_list)
            except:
                continue

       #初始化current_word，current_count为当前词
        current_word = word
        current_word_value_list = []
        current_word_value_list.append(count)

#最后一行处理，如果是和前面一行的词，后续没有词了，则前面没有输出
try:
    print current_word + "\t" + process_value_list(current_word_value_list)
except:
    i = i + 1
