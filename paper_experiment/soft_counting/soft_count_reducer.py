#!/usr/bin/env python
#coding=utf-8
import sys
import os
import math

current_word = None
current_word_value_list = []

#��ñ߽���
def process_value_list(value_list):
    return str( sum(value_list) )

for line in sys.stdin:
    line = line.strip()
    (word,count) = line.split("\t")
    count = float(count) #��ֵҪת����

    if current_word == word:#�����û�б䣬���ۼ�
        current_word_value_list.append(count)
    else:#����ʷ����仯��,�����
        if current_word != None:
            #��������ǵ�һ�У��� None��һ��,������������ǵ�һ�в����
            #�����һ����
            print current_word + "\t" + process_value_list(current_word_value_list)
        #��ʼ��current_word��current_countΪ��ǰ��
        current_word = word
        current_word_value_list = []
        current_word_value_list.append(count)

#���һ�д�������Ǻ�ǰ��һ�еĴʣ�����û�д��ˣ���ǰ��û�����
if current_word:
    print current_word + "\t" + process_value_list(current_word_value_list)
