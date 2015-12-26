#!/usr/bin/env python
#coding=utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
#�����Ĵ�Ƶ���ˣ�����������ַ����Ĵ�Ƶ�͸ô�һ�£���ɾ�����ַ���

word_dict={}
#װ�شʵ�
def load_dict(dict_file_name):
    #���س�ʼ�ʵ�
    dict_file = open(dict_file_name, "r")
    word_dict_count = {}
    for line in dict_file:
        sequence = line.strip()
        key = sequence.split('\t')[0]
        value = float(sequence.split('\t')[1])
        word_dict[key] = value

#���˴ʵ�
def filter_dict(word):
    for ngram_length in range(1,len(word)):
        #���ÿ��ngram_length���ȵ�Ƭ��
        for i in range(0,len(word)-ngram_length+1):
            sub_word = word[i:i+ngram_length]
            #�ж�sub_word�Ƿ��ɾ��
            if word_dict.has_key(sub_word):
                if word_dict[sub_word] != 0:
                    if word_dict[sub_word] == word_dict[word]: #�����Ƶ���
                        #ɾ������ʣ���Ϊ0
                        word_dict[sub_word] = 0
                    
if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input dict  filename"
        sys.exit()

    #load dict
    load_dict(sys.argv[1])
    #���ÿ����
    
    #��ȡ�ֵ��ļ�,����
    dict_file = open(sys.argv[1], "r")
    for line in dict_file:
        line = line.strip()
        word = line.split("\t")[0]
        if word_dict.has_key(word):
            if word_dict[word] != 0:
                filter_dict(word)

    #���
    for key in word_dict:
        if word_dict[key] != 0:
            print key + "\t" + str(word_dict[key])
