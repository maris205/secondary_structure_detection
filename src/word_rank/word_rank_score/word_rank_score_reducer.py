#!/usr/bin/env python
#coding=utf-8
import sys
import os
import math

current_word = None
current_word_value_list = []

def initial_dict(filename, word_dict):
    dict_file = open(filename, "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#获得word rank score
def process_value_list(value_list):
    score_sum = 0
    for word in value_list:
        if word_dict.has_key(word):
            score_sum += word_dict[word] 

    return str(score_sum)


#加载词典,记录word rank score
dict_file = "word_rank_score"
word_dict = {}
initial_dict(dict_file, word_dict)

for line in sys.stdin:
    line = line.strip()
    (word,count) = line.split("\t")
    
    if current_word == word:#如果词没有变，则累加
        current_word_value_list.append(count)
    else:#如果词发生变化了,则输出
        if current_word != None: 
            #如果读的是第一行，和 None不一致,但不输出，不是第一行才输出
            #输出上一个词
            print current_word + "\t" + process_value_list(current_word_value_list)
        #初始化current_word，current_count为当前词
        current_word = word
        current_word_value_list = []
        current_word_value_list.append(count)

#最后一行处理，如果是和前面一行的词，后续没有词了，则前面没有输出
if current_word:
    print current_word + "\t" + process_value_list(current_word_value_list)
