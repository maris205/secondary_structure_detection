#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import viterbi_segment
import structure_segment

if __name__=="__main__":
    if len(sys.argv) != 4:
        print "please input dict file , test data file, and max word length"
        sys.exit()

    MAX_WORD_LEGNTH = int(sys.argv[3])
    #训练的词典
    dict_file_name = sys.argv[1]
    my_seg = viterbi_segment.ViterbiSegment()
    my_seg.initial_dict(dict_file_name)
    
    #读取测试文件并测试
    test_file = open(sys.argv[2], "r")
    line_list = test_file.readlines()

    for i in range(0,len(line_list),3):
        #字符串
        line = line_list[i].strip()
        seq_letter_list = line
        
        #结构串
        struct_line = line_list[i+1].strip()
        struct_letter_list = struct_line

        standard_seg_list = structure_segment.stu_seg(seq_letter_list, struct_letter_list).split(" ")
        new_seg_list = []
        for seg in standard_seg_list:
            if len(seg)>MAX_WORD_LEGNTH: #如果长度大于最长词长度，分词为更小的片段
                try:
                    my_seg_list = my_seg.mp_seg(seg).split(" ")
                    new_seg_list.extend(my_seg_list)
                except:
                    continue
            else:
                new_seg_list.append(seg)

        print " ".join(new_seg_list)
