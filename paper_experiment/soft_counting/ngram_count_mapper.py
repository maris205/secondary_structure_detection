#!/usr/bin/env python
#coding=utf-8
import sys
import os
#获得ngram切分

g_contain_se = 0#是否加入开始和结束字符
g_max_word_length = 9 #最大的切分片段的长度，也就是最大的词长度

#输入 line  一个句子
#输入 word_length  词的长度
#输出 ngram 切分
#返回值 0，正确，其它错误
def build_ngram_word(line, word_length):
    #进行ngram交叉切分
    if g_contain_se == 1: #判断是否加入开始和结束标志，开关控制
        letter_list = ["<"] #句子开始标记
        letter_list.extend(line) #加入所有的字
        letter_list.append(">") #句子结束标记
    else:
        letter_list = line

    for i in range(0,len(letter_list)-word_length+1):
        word = "".join(letter_list[i:i+word_length])
        print word + "\t" + "1"

#构建所有长度的切分片段
def build_all_ngram_word(line):
    for word_length in range(1,g_max_word_length+1):
        build_ngram_word(line, word_length)

for line in sys.stdin:
    line = line.strip()
    build_all_ngram_word(line)
