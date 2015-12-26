#!/usr/bin/env python
#coding=utf-8
import sys
import math
import e_segment
reload(sys)
sys.setdefaultencoding('utf-8')

#输出所有词"\t"右边词
def get_right_border(line):
    seg = myseg.mp_seg(line)
    word_list = seg.split(" ")
    gram_n = 2
    for i in range(len(word_list)-gram_n+1):
        #获得ngram切分
        word = word_list[i]
        right_word = word_list[i+1]
        print word + "\t" + right_word
    return 0

#输出所有词"\t"右边词
def get_left_border(line):
    seg = myseg.mp_seg(line)
    word_list = seg.split(" ")
    gram_n = 2 
    for i in range(len(word_list)-gram_n+1):
        #获得ngram切分
        left_word = word_list[i]
        word = word_list[i+1]
        print word + "\t" + left_word
    return 0

for line in sys.stdin:
    line = line.strip()
    #输出所有可能的右边界词
    #get_left_border(line)
    try:
        #get_left_border(line)
        get_right_border(line)
    except:
        continue
