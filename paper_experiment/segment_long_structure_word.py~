#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import viterbi_segment
import structure_segment
#get standard seg
#use dict of secondary structure word
    
if __name__=="__main__":
    if len(sys.argv) != 4:
        print "please input dict file,test data file, max word length"
        sys.exit()


    #max word length
    max_word_length = int(sys.argv[3])

    #load dict of secondary structure word
    dict_file_name = sys.argv[1]
    my_seg = viterbi_segment.DNASegment()
    my_seg.initial_dict(dict_file_name, max_word_length)
    
    #read test file
    test_file = open(sys.argv[2], "r")
    line_list = test_file.readlines()
    
    for i in range(0,len(line_list),3):
        #read protein sequence 
        line = line_list[i].strip()
        seq_letter_list = line
        
        #read structure sequence
        struct_line = line_list[i+1].strip()
        struct_letter_list = struct_line

        standard_seg_list = structure_segment.stu_seg(seq_letter_list, struct_letter_list).split(" ")
        new_seg_list = []
        for seg in standard_seg_list:
            #if more than max word length, divide into shorter words
            if len(seg)>max_word_length:
                my_seg_list = my_seg.mp_seg(seg).split(" ")
                new_seg_list.extend(my_seg_list)
            else:
                new_seg_list.append(seg)

        print " ".join(new_seg_list)
