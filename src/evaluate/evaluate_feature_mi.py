#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import random
#特征有效性的mi判别
#输入文件格式为数值+\t+label
data_list = []

def load_data(filename):
    data_file = open(filename, "r")
    for line in data_file:
        line = line.strip()
        value = float( line.split("\t")[1] )
        label = int( line.split("\t")[2] )
        data_list.append([value, label])
    return 0

#获得threshold下的特征分辨率
def get_mi(threshold):
    #计算H(C)
    w_num = 0 #词的数目
    not_w_num = 0 #非词的数目
    for item in data_list:
        label = item[1]
        if label == 0 :#如果不是词
            not_w_num += 1
        else:
            w_num += 1

    w_num_prob = float(w_num)/(w_num + not_w_num)
    not_w_num_prob = float(not_w_num)/(w_num + not_w_num)
    h_c = -1*w_num_prob*math.log(w_num_prob, 2)-\
            not_w_num_prob*math.log(not_w_num_prob, 2)
    
    print "word num",w_num,"no word num",not_w_num,"h_c",h_c

    #计算H(C|T) = H(C|t) + H(C|!t)
    #计算H(C|t)，其中t为大于阈值的特征
    #H(C|t) = P(t)[  H(C1|t)+H(C2|t) ]=P(t)[  -P(C1|t)logP(C1|t) + -P(C2|t)logP(C2|t)]
    t_c1_num = 0 #类别1的数目，也就是词的数目
    t_c2_num = 0 #类别2的数目，也就是非词的数目
    for item in data_list:
        value = item[0]
        label = item[1]
        if value > threshold:#大于阈值
            if label == 1: # 是词的
                t_c1_num += 1
            else:
                t_c2_num += 1
    p_t = float( t_c1_num + t_c2_num )/len(data_list)
    t_c1_prob = float(t_c1_num)/(t_c1_num + t_c2_num)
    t_c2_prob = float(t_c2_num)/(t_c1_num + t_c2_num)
    h_t_c = p_t*( -1*t_c1_prob*math.log(t_c1_prob, 2) - \
            t_c2_prob*math.log(t_c2_prob, 2) )
    #print "t_c1_prob",t_c1_prob,"t_c2_prob",t_c2_prob,"h_t_c",h_t_c
    print "precision",t_c1_prob,"recall ",float(t_c1_num)/w_num

    #计算H(C|!t)，其中!t为小于等于阈值的特征
    #H(C|!t) = P(!t)[  H(C1|!t)+H(C2|!t) ]=P(!t)[  -P(C1|!t)logP(C1|!t) + -P(C2|t)logP(C2|!t) ]
    nt_c1_num = 0 #类别1的数目，也就是词的数目
    nt_c2_num = 0 #类别2的数目，也就是非词的数目
    for item in data_list:
        value = item[0]
        label = item[1]
        if value <= threshold:#大于阈值
            if label == 1: # 是词的
                nt_c1_num += 1
            else:
                nt_c2_num += 1
    
    p_nt = float( nt_c1_num + nt_c2_num )/len(data_list)
    nt_c1_prob = float(nt_c1_num)/(nt_c1_num + nt_c2_num)
    nt_c2_prob = float(nt_c2_num)/(nt_c1_num + nt_c2_num)
    #print nt_c1_prob, nt_c2_prob
    h_nt_c = p_nt*( -1*nt_c1_prob*math.log(nt_c1_prob, 2) - \
            nt_c2_prob*math.log(nt_c2_prob, 2) )
    #print "nt_c1_prob",nt_c1_prob,"nt_c2_prob",nt_c2_prob,"h_nt_c",h_nt_c
    print "delete not word percent",float(nt_c2_num)/not_w_num 
    #get feature mi
    mi = h_c - (h_t_c + h_nt_c)
    return mi



if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input filename"
        sys.exit()

    #加载数据列表
    filename = sys.argv[1]
    load_data(filename)

    #计算mi
    for threshold in range(0,30):
        try:
            mi = get_mi(float(threshold))
            print threshold,mi
        except:
            continue
