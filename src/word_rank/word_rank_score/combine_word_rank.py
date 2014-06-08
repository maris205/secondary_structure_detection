#!/usr/bin/env python
#coding=utf-8
import sys 
import math
#合并左右边界熵，取小的，没有的看做是0
#he ,she这样的会不会被干掉

if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input left and right border info file name"
        sys.exit()

    left_file = open(sys.argv[1], "r")
    left_info_dict = {}
    for line in left_file:
        line = line.strip()
        word = line.split("\t")[0]
        info = float(line.split("\t")[1])
        left_info_dict[word] = info

    #遍历右边界熵，没有的就不要了，当做是0
    right_file = open(sys.argv[2], "r")
    border_info = {}
    for line in right_file:
        line = line.strip()
        word = line.split("\t")[0]
        info = float(line.split("\t")[1])
        if left_info_dict.has_key(word):#如果包含才算有边界熵
                border_info[word] = 35.0 + math.log(info*left_info_dict[word])

    #排序输出
    border_info_list = sorted(border_info.iteritems(), key=lambda d:d[1], \
            reverse=True)
    for key,value in border_info_list:
        #if value > 0:#大于0的才要
        print key + "\t" + str(value)
