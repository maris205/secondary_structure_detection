#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import random
import numpy
#�жϳ�ȡ�ʵ�׼ȷ��
#�����ļ���ʽΪword+\t+��ֵ+\t+label
data_list = []
#dict_word_num = 430341 #�ʵ��С����������recall
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


#���׼ȷ��, �Զ��б�threshold
def get_prf():
    #step 1,������ֵ������
    #max_value = max(data_list[i][0] for i in range(len(data_list)))
    #min_value = min(data_list[i][0] for i in range(len(data_list)))
    step = 100 #�ֳ�100��
    min_value = 1
    max_value = len(data_list)
    for top_num in  numpy.linspace(min_value, max_value-1, num=step):
        word_num = 0 #�ʵ���Ŀ
        no_word_num = 0 #�Ǵʵ���Ŀ
        for item in data_list[0:int(top_num)]:
            label = item[1]
            value = item[0]
            if label == 0 :#������Ǵ�
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

#���׼ȷ��, ��Ҫ����������Сֵ,�Լ��ֳɶ��ٷ�
def get_prf_threshold(min_value, max_value, step=100):
    for threshold in  numpy.linspace(min_value, max_value-1, num=step):
        word_num = 0 #�ʵ���Ŀ
        no_word_num = 0 #�Ǵʵ���Ŀ
        for item in data_list:
            label = item[1]
            value = item[0]
            if value>threshold: 
                if label == 0 :#������Ǵ�
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

    #���������б�
    filename = sys.argv[1]
    load_data(filename)

    #����׼ȷ��
    #get_prf()
    get_prf_threshold(1, 200, 100)
