#!/usr/bin/env python
#coding=utf-8
import sys
import os
#ngram统计，reducer部分

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    (word,count) = line.split("\t")
    count = int(count)
    if current_word == word:#如果词没有变，则累加
        current_count = current_count + count
    else:#如果词发生变化了,则输出
        if current_word != None: 
            #如果读的是第一行，和 None不一致,但不输出，不是第一行才输出
            #输出上一个词
            print current_word + "\t" + str(current_count)
        #初始化current_word，current_count为当前词
        current_word = word
        current_count = count

#最后一行处理，如果是和前面一行的词，后续没有词了，则前面没有输出
if current_word:
    print current_word + "\t" + str(current_count)
