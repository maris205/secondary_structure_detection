#!/usr/bin/env python
#coding=utf-8
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')
#ngram�зֻ�ñ߽��ȶ���
#ֻҪtop100��Ĵʵ�
g_border_length = 1 #�߽�ĳ���
g_max_word_length = 12 #���Ĵʵĳ���


def initial_dict(filename, word_dict):
    dict_file = open(filename, "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#������д�"\t"�ұߴ�
def get_right_border(line, word_length):
    gram_n = word_length + g_border_length  #ngram��Ƭ�γ��ȣ�Ϊ�ʵĳ���+�߽糤��
    #���ngram�з�
    for i in range(len(line)-gram_n+1):
        word = "".join(line[i:i+word_length])
        right_word = "".join(line[i+word_length:i+word_length+g_border_length])
        if word_dict.has_key(word):
            print word + "\t" + right_word
    return 0

#������д�"\t"�ұߴ�
def get_left_border(line, word_length):
    word_list = line.split(" ")
    gram_n = word_length + g_border_length  #ngram��Ƭ�γ��ȣ�Ϊ�ʵĳ���+�߽糤��
    for i in range(len(line)-gram_n+1):
        #���ngram�з�
        left_word = "".join(line[i:i+g_border_length])
        word = "".join(line[i+g_border_length:i+word_length+g_border_length])
        if word_dict.has_key(word):
            print word + "\t" + left_word
    return 0

#���شʵ�
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
