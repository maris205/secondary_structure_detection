#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#segment the protein sequence according to its secondary structure
def stu_seg(seq_letter_list, struct_letter_list):

    #step 1,read segment pos
    pre_letter = struct_letter_list[0]
    change_pos_list = []
    for j in range(1,len(struct_letter_list)):
        if struct_letter_list[j] != pre_letter:
            change_pos_list.append(j)
            pre_letter = struct_letter_list[j]
    change_pos_list.append(len(struct_letter_list))
    #print change_pos_list

    #segment sequence 
    pre_pos = 0
    seq_with_cixing_list = []
    for item in change_pos_list:
        cur_pos = item
        cur_stru_seg = struct_letter_list[pre_pos:cur_pos]
        cur_seq_seg = seq_letter_list[pre_pos:cur_pos]
        cur_sentence = "".join(cur_seq_seg)
        cixing = cur_stru_seg[0]
        pre_pos = cur_pos
        #seq_with_cixing_list.append(cur_sentence + "/" + cixing)
        seq_with_cixing_list.append(cur_sentence)
    #print " ".join(seq_with_cixing_list)
    return " ".join(seq_with_cixing_list)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input data filename"
        sys.exit()

    filename = sys.argv[1]
    data_file = open(filename,'r')

    line_list = data_file.readlines()
    for i in range(0,len(line_list),3):

        #amino acid letter
        line = line_list[i].strip()
        seq_letter_list = line
        #struct letter
        struct_line = line_list[i+1].strip()
        struct_letter_list = struct_line

        segment = stu_seg(seq_letter_list, struct_letter_list)
        segment_list = segment.split(" ")
        print " ".join(segment_list)
