#!/usr/bin/env python
#coding=utf-8
import sys 
import math
reload(sys)
sys.setdefaultencoding('utf-8')

#MDL，(minimum description length),最小描述长度
#输入，分好词的文件，格式为 词 空格 词 空格...
word_dict = {}

#加载语料，统计词和词频，用于后续的处理
def load_corpus(word_seq_file_name):
    data_file = open(word_seq_file_name, "r")
    for line in data_file:
        line = line.strip()
        word_list = line.split(" ")
        for word in word_list:
            word_dict.setdefault(word,float(0))
            word_dict[word] += 1
    return 0

#获得字母的描述长度值
#目前只处理单字节的字母
def get_letter_info():
    letter_dict = {}
    #统计letter
    for word in word_dict:
        for letter in word:
            letter_dict.setdefault(letter, 0)
            letter_dict[letter] += 1
    
    #计算字母的描述长度
    letter_num = float(len(letter_dict))
    letter_info = math.log(letter_num, 2)

    return letter_info

#获得词典的词的总长度
def get_dict_info():
    word_length_sum = 0
    for word in word_dict:
        word_length_sum += len(word)

    return word_length_sum

#获得单词序列的描述长度
def get_word_seq_info():
    word_info_sum = 0
    freq_sum = sum(word_dict.itervalues()) #所有词的词频
    for word in word_dict:
        word_freq = word_dict[word]
        word_info = word_freq * ( math.log(word_freq, 2) - math.log(freq_sum, 2) )
        word_info_sum += word_info
    
    word_seq_info = -1*word_info_sum
    return word_seq_info

#获得最终的mdl
def get_mdl():
    letter_info = get_letter_info()
    dict_info = get_dict_info()
    word_seq_info = get_word_seq_info()
    mdl = letter_info*dict_info + word_seq_info
    return mdl

if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input word corpus filename"
        sys.exit()
    load_corpus(sys.argv[1])
    print get_mdl()
