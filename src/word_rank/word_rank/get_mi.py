#!/usr/bin/env python
#coding=utf-8
import sys 
import e_segment_mi
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    if len(sys.argv)!=3:
        print "please input dict and sequence data filename"
        sys.exit()

    #分词初始化
    myseg = e_segment_mi.DNASegment()
    myseg.initial_dict(sys.argv[1])

    filename = sys.argv[2]
    data_file = open(filename,'r')
    
    for line in data_file:
        line = line.strip()
        word = line.split("\t")[0]
        if len(word) > 3: #mi只针对长度大一些的词
            mi = myseg.get_word_mi(word)
            print word + "\t" + str(mi)
