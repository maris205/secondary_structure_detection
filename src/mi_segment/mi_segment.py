#!/usr/bin/env python
#coding=utf-8
#############################################################
#function: mi segment
#         
#
#input: dict file
#output: segmented words, divide by delimiter " "
#author: wangliang.f@gmail.com
##############################################################

import math
import sys 
#����mi���зִ�

g_max_word_length = 8 #�����з�Ƭ�εĳ��ȣ�Ҳ�������Ĵʳ���

class MISegment:
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
    def get_prob(self, ngram_seg):
        if self.word_dict.has_key(ngram_seg):
            return self.word_dict[ngram_seg]
        else: #+1ƽ��
            return 10./(self.g_all_freq*10**len(ngram_seg))
            #return 7.07914797767e-100

    def get_mi(self, start, ngram_seg, mi_dict):
        for i in range(1,len(ngram_seg)):
            left_seg = ngram_seg[0:i]
            right_seg = ngram_seg[i:]
            mi = self.get_prob(ngram_seg)/( self.get_prob(left_seg)*self.get_prob(right_seg))
            #�洢
            pos = start + i
            mi_dict.setdefault(pos,[])
            mi_dict[pos].append(mi)
            #print mi_dict
        return 0


    #���л���mi�ķִ�
    #ͳ�Ƶ����ݽ����key�Ƿָ��λ�ã�value��һ��list���洢���ֿ��ܵ�mi
    def mi_seg(self, line):
        #ngram segment , ���ÿ��ngramƬ�ε������ָ���mi
        ngram_length = g_max_word_length
        mi_dict = {}
        for i in range(0,len(line)-ngram_length+1):
            start = i
            ngram_seg = "".join(line[i:i+ngram_length])
            #print ngram_seg
            self.get_mi(start, ngram_seg, mi_dict)
        #print mi_dict

        #ͳ��
        pos_mi_list = []
        pos_mi_list.append( (0,0) ) #begin pos
        for pos in mi_dict:
            mi_list = mi_dict[pos]
            mi_avg = sum(mi_list)/len(mi_list)
            pos_mi_list.append( (pos, mi_avg) )
            #print mi_avg
        pos_mi_list.append( (0,0) ) #end pos

        #print pos_mi_list 
        seg_pos_list = []
        seg_pos_list.append(0) # first node
        for i in range(1, len(pos_mi_list)-1):
            cur = pos_mi_list[i][1] 
            pre = pos_mi_list[i-1][1]
            next = pos_mi_list[i+1][1]
            pos = pos_mi_list[i][0] 
            if cur<pre and cur<next:
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
        #print  seg_sequence
        return seg_sequence



if __name__=="__main__":
    #��ʼ����
    #���ȼ��شʵ�
    dict_file_name = "dict_9"
    myseg = MISegment()
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
