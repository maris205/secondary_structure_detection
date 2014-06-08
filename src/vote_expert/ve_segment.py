#!/usr/bin/env python
#coding=utf-8
#############################################################
#function: voting expert segment
#         
#
#input: dict file
#output: segmented words, divide by delimiter " "
#author: wangliang.f@gmail.com
##############################################################

import math
import sys 
#根据ve进行分词
window_length = 7 #窗口的长度

class VESegment:
    def __init__(self):
        self.word_freq_dict = {} #词频词典
        self.word_bf_dict = {} #边界熵词典

    #加载词频词典
    def load_freq_dict(self, dict_file_name):
        #加载初始词典
        dict_file = open(dict_file_name, "r")
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            self.word_freq_dict[key] = value

    #加载边界熵词典
    #加载词典
    def load_bf_dict(self, dict_file_name):
        #加载初始词典
        dict_file = open(dict_file_name, "r")
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            self.word_bf_dict[key] = value

    #获得一个窗口内的vote值
    def get_vote(self, window):
        freq_vote_list = []
        bf_vote_list = []
        #获得每个点的
        for i in range(1,len(window)+1):
            #获得词频的投票值
            left_sub_word = window[0:i]
            right_sub_word = window[i:]
            freq_vote_value = 0 #判断是否获得过投票
            is_get_value = 0
            if self.word_freq_dict.has_key(left_sub_word):
                freq_vote_value += self.word_freq_dict[left_sub_word]
                is_get_value = 1
            if self.word_freq_dict.has_key(right_sub_word):
                freq_vote_value += self.word_freq_dict[right_sub_word]
                is_get_value = 1

            if is_get_value == 0: #如果没有赋值过，也就是两个词典都没有
                freq_vote_value = -100 #给予一个很小的值
            freq_vote_list.append(freq_vote_value)

        for i in range(1,len(window)+1):
            #获得bf的投票值
            sub_word = window[0:i]
            if self.word_bf_dict.has_key(sub_word):
                bf_vote_value = self.word_bf_dict[sub_word]
            else:
                bf_vote_value =  -10000 #如果没有，则给一个非常小的值
            bf_vote_list.append(bf_vote_value)

        #获得最大值
        freq_vote_pos = freq_vote_list.index( max(freq_vote_list) ) + 1 #list的第一个元素是字符串1位置：
        bf_vote_pos = bf_vote_list.index( max(bf_vote_list) ) + 1
        return freq_vote_pos, bf_vote_pos

    #获得每个点的vote值
    def get_vote_list(self, line):
        vote_dict = {}
        #获得ngram窗口
        for i in range(len(line)-window_length+1):
            window = line[i:i+window_length]
            #get vote value
            (freq_vote_pos, bf_vote_pos) = self.get_vote(window)
            freq_vote_pos += i #加上起始位置
            bf_vote_pos += i #加上起始位置
            
            #sum vote value 
            vote_dict.setdefault(freq_vote_pos, 0)
            vote_dict[freq_vote_pos] += 1
            
            vote_dict.setdefault(bf_vote_pos, 0)
            vote_dict[bf_vote_pos] += 1
        #输出
        vote_list = []
        for i in range(len(line)+1):
            if vote_dict.has_key(i):
                vote_list.append(vote_dict[i])
            else:
                vote_list.append(0) #如果没有投票，当成0
        return vote_list

    #ve segment
    def ve_seg(self, line):
        vote_list = self.get_vote_list(line)
        seg_pos_list = []
        seg_pos_list.append(0) # first node
        for i in range(1, len(vote_list)-1):
            cur = vote_list[i] 
            pre = vote_list[i-1]
            next = vote_list[i+1]
            pos = i
            if cur>pre and cur>next:
                if cur>2:
                    seg_pos_list.append(pos)

        seg_pos_list.append(len(line)) # last node
            
        #构建分词
        word_list = []
        for i in range(len(seg_pos_list)-1):
            left = seg_pos_list[i]
            right = seg_pos_list[i + 1]
            word = line[left:right]
            word_list.append(word)

        seg_sequence = " ".join(word_list)
        return seg_sequence
    
    #初始词典
    def initial(self, freq_file, rf_file):
        self.load_freq_dict(freq_file)
        self.load_bf_dict(rf_file)

if __name__=="__main__":
    #开始运行
    my_seg = VESegment()
    my_seg.initial("english.freq.norm", "english.rf.norm")

    line = "itwasabrightcolddayinaprilandtheclockswerestrikingthirteen"
    #输出词的所有分配的权值
    print my_seg.ve_seg(line)
