#!/usr/bin/env python
#coding=utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#基本的词频过滤，就是如果子字符串的词频和该词一致，则删掉子字符串

word_dict={}
#装载词典
def load_dict(dict_file_name):
    #加载初始词典
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#过滤词典
def filter_dict(word):
    for ngram_length in range(1,len(word)):
        #获得每个ngram_length长度的片段
        for i in range(0,len(word)-ngram_length+1):
            sub_word = word[i:i+ngram_length]
            #判断sub_word是否该删除
            if word_dict.has_key(sub_word):
                if word_dict[sub_word] != 0:
                    if word_dict[sub_word] == word_dict[word]: #如果词频相等
                        #删掉这个词，置为0
                        word_dict[sub_word] = 0
                    
if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input dict  filename"
        sys.exit()

    #load dict
    load_dict(sys.argv[1])
    #检测每个词
    
    #读取字典文件,过滤
    dict_file = open(sys.argv[1], "r")
    for line in dict_file:
        line = line.strip()
        word = line.split("\t")[0]
        if word_dict.has_key(word):
            if word_dict[word] != 0:
                filter_dict(word)

    #输出
    for key in word_dict:
        if word_dict[key] != 0:
            print key + "\t" + str(word_dict[key])
