#!/usr/bin/env python
#coding=utf-8
import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')
#ngram�зֻ�ñ߽��ȶ���
#ֻҪtop100��Ĵʵ�
g_max_word_length = 16 #���Ĵʵĳ���


def initial_dict(filename, word_dict):
    dict_file = open(filename, "r")
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#������д�"\t"�ұߴ�
def get_right_border(line, word_length, border_length):
    gram_n = word_length + border_length  #ngram��Ƭ�γ��ȣ�Ϊ�ʵĳ���+�߽糤��
    #���ngram�з֣�����������
    for i in range(len(line)-gram_n+1):
        word = "".join(line[i:i+word_length])
        right_word = "".join(line[i+word_length:i+word_length+border_length])
        if word_dict.has_key(word) and word_dict.has_key(right_word):
            print word + "\t" + right_word
    return 0

#������д�"\t"�ұߴ�
def get_left_border(line, word_length, border_length):
    gram_n = word_length + border_length  #ngram��Ƭ�γ��ȣ�Ϊ�ʵĳ���+�߽糤��
    for i in range(len(line)-gram_n+1):
        #���ngram�з�
        left_word = "".join(line[i:i+border_length])
        word = "".join(line[i+border_length:i+word_length+border_length])
        if word_dict.has_key(word) and word_dict.has_key(left_word):
            print word + "\t" + left_word
    return 0

#���شʵ�
dict_file_name = "swiss.pr.len40.sort" 
word_dict = {}
initial_dict(dict_file_name, word_dict)

for line in sys.stdin:
    line = line.strip()
    for word_length in range(1, g_max_word_length+1):
        for border_length in range(1, g_max_word_length+1):
            try:
                get_left_border(line, word_length, border_length)
                #get_right_border(line, word_length, border_length)
            except:
                continue
