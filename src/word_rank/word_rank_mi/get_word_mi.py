#!/usr/bin/env python
#coding=utf-8
import sys 
import e_segment_mi
import math
reload(sys)
sys.setdefaultencoding('utf-8')
myseg = e_segment_mi.DNASegment()

def get_rank_mi(word):
    #2-ngram切分
    ngram_length = 2
    mi_list = []
    for i in range(0,len(word)-ngram_length+1):
        seg ="".join(word[i:i+ngram_length])
        mi = myseg.get_word_mi(seg)
        mi_list.append(mi)

    return min(mi_list)


if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input dict filename"
        sys.exit()

    #分词初始化
    myseg.initial_dict(sys.argv[1])

    filename = sys.argv[1]
    data_file = open(filename,'r')
    
    for line in data_file:
        line = line.strip()
        word = line.split("\t")[0]
        if len(word) > 1:
            mi = get_rank_mi(word)
            print word + "\t" + str(math.exp(mi))
        else:
            print word + "\t1"
