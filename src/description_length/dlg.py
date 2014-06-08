#!/usr/bin/env python
#coding=utf-8
import sys 
import math
reload(sys)
sys.setdefaultencoding('utf-8')

#MDL，(minimum description length),最小描述长度
#输入，原始字符串语料
word_dict = {} #word词典
letter_dict = {} #letter词典
ori_letter_seq_seq = "" #原始字符串长度
ori_letter_info = 0 #原始字符串的信息量

#获得一个词的描述增益
def get_dlg(word):
    global ori_letter_seq_len
    global ori_letter_info
    new_letter_length = ori_letter_seq_len - word_dict[word]*len(word)\
            + word_dict[word] + len(word) + 1# +1?
    #print "ori_letter_length", len(ori_letter_seq)
    #print "new_letter_length", new_letter_length
    word_info_sum = 0
    #step 1, 计算词本身的累加墒
    word_self_info = word_dict[word] * math.log(word_dict[word]/new_letter_length, 2)
    #print "word_self_info", word_self_info
    word_info_sum += word_self_info

    #step 2, 计算替换后的字符串墒
    letter_info = 0
    #print "letter_dict", letter_dict
    for letter in letter_dict:
        letter_num = letter_dict[letter]
        letter_in_word_num = word.count(letter)#letter在word中出现的次数
        letter_num = letter_num - \
                word_dict[word]*letter_in_word_num + letter_in_word_num
        if letter_num<=0:
            return -100
        letter_info += letter_num*math.log(float(letter_num)/new_letter_length, 2)
    
    word_info_sum += letter_info
    word_info = -1*word_info_sum
    #print "word_info", word_info
    dlg = ori_letter_info - word_info
    return dlg/word_dict[word]

#加载词典
def load_dict(filename):
    dict_file = open(filename, "r")
    for line in dict_file:
        line = line.strip()
        word = line.split("\t")[0]
        freq = float( line.split("\t")[1] )
        #freq = float(ori_letter_seq.count(word))
        word_dict[word] = freq
        #print word + "\t" + str(freq)
    return 0

#加载语料,获得原始字符串，以及原始字符串的墒
def load_corpus(word_seq_file_name):
    global ori_letter_seq_len
    global ori_letter_info
    ori_letter_seq_len = 0
    data_file = open(word_seq_file_name, "r")
    for line in data_file:
        line = line.strip()
        ori_letter_seq_len += len(line)
    
        #统计letter
        for letter in line:
            letter_dict.setdefault(letter, 0)
            letter_dict[letter] += 1
    
    #only leave 20 protein letters
    #计算原始字符串的字母的描述长度
    letter_info = 0
    for letter in letter_dict:
        letter_num = letter_dict[letter]
        letter_info += letter_num*math.log(float(letter_num)/ori_letter_seq_len, 2)

    ori_letter_info = -1*letter_info
    #print "ori_letter_info", ori_letter_info
    return 0


if __name__=="__main__":
    if len(sys.argv)!=3:
        print "please input word corpus and dict filename"
        sys.exit()
    load_corpus(sys.argv[1])
    load_dict(sys.argv[2])
    
    dict_file = open(sys.argv[2], "r")
    for line in dict_file:
        line = line.strip()
        word = line.split("\t")[0]
        dlg = get_dlg(word)
        print word + "\t" + str(dlg)
