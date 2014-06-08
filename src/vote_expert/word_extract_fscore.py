#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import random
import numpy
#判断抽取词的准确率
#输入文件格式为word+\t+数值+\t+label
data_list = []
#dict_word_num = 430341 #词典大小，用来计算recall
dict_word_num = 41202
def load_data(filename):
    global data_list
    data_file = open(filename, "r")
    for line in data_file:
        line = line.strip()
        value = float( line.split("\t")[1] )
        label = int( line.split("\t")[2] )
        data_list.append([value, label])
    #sort
    data_list = sorted(data_list, key=lambda d:d[0], reverse=True)
    return 0


#获得准确率, 自动判别threshold
def get_prf():
    #step 1,计算数值的区间
    #max_value = max(data_list[i][0] for i in range(len(data_list)))
    #min_value = min(data_list[i][0] for i in range(len(data_list)))
    step = 100 #分成100份
    min_value = 1
    max_value = len(data_list)
    for top_num in  numpy.linspace(min_value, max_value-1, num=step):
        word_num = 0 #词的数目
        no_word_num = 0 #非词的数目
        for item in data_list[0:int(top_num)]:
            label = item[1]
            value = item[0]
            if label == 0 :#如果不是词
                no_word_num += 1
            else:
                word_num += 1

    
        if (word_num + no_word_num) > 0:
            precision = float(word_num)/(word_num + no_word_num)
        else:
            precision = 0

        recall = float(word_num)/dict_word_num
        
        if (precision+recall)>0:
            fscore = 2*precision*recall/(precision+recall)
        else:
            fscore = 0

        threshold = data_list[int(top_num)][0] 
        print ">threshold", threshold
        print "p",precision,"r",recall,"f",fscore

#获得准确率, 需要设置最大和最小值,以及分成多少份
def get_prf_threshold(min_value, max_value, step=100):
    for threshold in  numpy.linspace(min_value, max_value-1, num=step):
        word_num = 0 #词的数目
        no_word_num = 0 #非词的数目
        for item in data_list:
            label = item[1]
            value = item[0]
            if value>threshold: 
                if label == 0 :#如果不是词
                    no_word_num += 1
                else:
                    word_num += 1

        if (word_num + no_word_num) > 0:
            precision = float(word_num)/(word_num + no_word_num)
        else:
            precision = 0

        recall = float(word_num)/dict_word_num

        if (precision+recall)>0:
            fscore = 2*precision*recall/(precision+recall)
        else:
            fscore = 0

        print ">threshold", threshold
        print "p",precision,"r",recall,"f",fscore


if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input filename"
        sys.exit()

    #加载数据列表
    filename = sys.argv[1]
    load_data(filename)

    #计算准确率
    #get_prf()
    get_prf_threshold(1, 200, 100)
