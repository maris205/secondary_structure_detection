#!/usr/bin/env python
#coding=utf-8
#############################################################
#function: tango segment
#         
#
#input: dict file
#output: segmented words, divide by delimiter " "
#author: wangliang.f@gmail.com
##############################################################

import math
import sys 
#����mi���зִ�

g_max_word_length = 10 #�����з�Ƭ�εĳ��ȣ�Ҳ�������Ĵʳ���

class TangoSegment:
    def __init__(self):
        self.word_dict = {} #�ʵĸ���
        self.g_all_freq = 0 #���дʵĴ�Ƶ

    #���شʵ�
    def load_dict(self, dict_file_name):
        #���س�ʼ�ʵ�
        dict_file = open(dict_file_name, "r")
        word_dict_count = {}
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            word_dict_count[key] = value
        #������Ƶ��
        self.g_all_freq = sum(word_dict_count.itervalues()) #���дʵĴ�Ƶ
        #����ÿ���ʵĸ���
        for key in word_dict_count:
            value = word_dict_count[key]
            self.word_dict[key] = value/self.g_all_freq

    #���Ƭ�εĸ���
    def get_freq(self, ngram_seg):
        if self.word_dict.has_key(ngram_seg):
            return self.word_dict[ngram_seg]
        else: #+1ƽ��
            return 1

    #���tangoֵ
    def get_tango(self, start, ngram_seg, tango_dict):
        word_length = len(ngram_seg)/2
        s_l = ngram_seg[0:word_length]
        s_r = ngram_seg[word_length:]
        #print s_l,s_r

        vote = 0
        for i in range(1, word_length):
            t = ngram_seg[i:i+word_length]
            #print t
            #����ͶƱֵ
            if self.get_freq(s_l) > self.get_freq(t):
                vote += 1
            if self.get_freq(s_r) > self.get_freq(t):
                vote += 1

        tango_value = float(vote)/( 2*(word_length-1) )
        pos = start + word_length
        tango_dict.setdefault(pos, [])
        tango_dict[pos].append(tango_value)
        return 0


    #���л���tango�ķִ�
    #ͳ�Ƶ����ݽ����key�Ƿָ��λ�ã�value��һ��list���洢���ֿ��ܵ�mi
    def mi_seg(self, line):
        #ngram segment
        tango_dict = {}
        for word_length in range(2,g_max_word_length):
            ngram_length = 2*word_length
            for i in range(0,len(line)-ngram_length+1):
                start = i
                ngram_seg = "".join(line[i:i+ngram_length])
                self.get_tango(start, ngram_seg, tango_dict)

        #ͳ��
        pos_tango_list = []
        pos_tango_list.append( (0,0) ) #begin pos
        pos_tango_list.append( (1,0) ) #second pos

        for pos in tango_dict:
            tango_list = tango_dict[pos]
            tango_avg = sum(tango_list)/len(tango_list)
            pos_tango_list.append( (pos, tango_avg) )
            #print mi_avg
        pos_tango_list.append( (0,0) ) #end pos
        pos_tango_list.append( (0,0) ) #end pos

        #print pos_tango_list 
        for item in pos_tango_list:
            print item[1]

        seg_pos_list = []
        seg_pos_list.append(0) # first node
        for i in range(1, len(pos_tango_list)-1):
            cur = pos_tango_list[i][1] 
            pre = pos_tango_list[i-1][1]
            next = pos_tango_list[i+1][1]
            pos = pos_tango_list[i][0] 
            if cur>pre and cur>next:
                if cur>0.36:
                    seg_pos_list.append(pos)

        seg_pos_list.append(len(line)) # last node
        #print seg_pos_list

        #�����ִ�
        word_list = []
        for i in range(len(seg_pos_list)-1):
            left = seg_pos_list[i]
            right = seg_pos_list[i + 1]
            word = line[left:right]
            word_list.append(word)
        
        seg_sequence = " ".join(word_list)
        return seg_sequence


if __name__=="__main__":
    #��ʼ����
    #���ȼ��شʵ�
    dict_file_name = "dict_0"
    myseg = TangoSegment()
    myseg.load_dict(dict_file_name)

    for line in sys.stdin:
        line = line.strip()
        #����ʵ����з����Ȩֵ
        print myseg.mi_seg(line)
     

    """
    mi_dict = {}
    start = 0
    ngram_seg = "KKYD"
    get_mi(start, ngram_seg, mi_dict)
    """
