#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import e_segment
import seg_stru
#�ִ�Ч������
#��÷ִ�׼ȷ�ʺ͸�����
#�ֱ���ر�׼�ʵ��ѵ�������Ĵʵ䣬Ȼ��Ƚ�

#���ݷִʽ������÷ָ��ԣ���Ϊ�ִ�����Ļ�������
def get_seg_node_pair_list(seg_list):
    seg_node_list = []
    start_node = 0
    end_node = 0
    for seg in seg_list:
        end_node = start_node + len(seg)
        seg_node_list.append( (start_node, end_node) )
        start_node = end_node
    return seg_node_list

#���ݷָ��÷ָ��λ���б�
def get_seg_node_list(seg_list):
    seg_node_list = []
    node = 0
    for seg in seg_list:
        seg_node_list.append(node)
        node += len(seg)
    #last node
    seg_node_list.append(node)
    return seg_node_list

#��ñ߽��׼ȷ��
def get_seg_pos_precision(standard_seg_list, my_seg_list):
    #��ͬ�ķָ����Ŀ
    standard_seg_pos_list = get_seg_node_list(standard_seg_list)
    my_seg_pos_list = get_seg_node_list(my_seg_list)

    same_num = len( set(standard_seg_pos_list)&set(my_seg_pos_list) )
    #�߽�׼ȷ�ʣ������ҵķָ�㣬λ�ڱ�׼�ָ��ı���
    precision = float(same_num-1)/(len(my_seg_pos_list)-1)
    
    #�߽縲����,�����ʾ��Ǳ�׼�ָ��λ��Ԥ��ָ��ı���������Ǻ���ָ��
    recall = float(same_num-1)/(len(standard_seg_pos_list)-1)
    return (precision,recall)

def get_pr(standard_seg_list, my_seg_list):
    #ͳ�Ʒָ�λ�õ㣬ǰ�����һ��
    stardard_seg_node_list = get_seg_node_pair_list(standard_seg_list)
    my_seg_node_list = get_seg_node_pair_list(my_seg_list)
    #print stardard_seg_node_list
    #print my_seg_node_list
    #�鿴����list��ͬ�Ĳ��ֵĸ���
    same_num = len( set(stardard_seg_node_list)&set(my_seg_node_list) )
    #׼ȷ��
    precision = float(same_num) /len(my_seg_node_list)
    #������
    recall = float(same_num) /len(stardard_seg_node_list)
    
    return (precision,recall)

    
if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input dict file and test data file"
        sys.exit()


    #ѵ���Ĵʵ�
    dict_file_name = sys.argv[1]
    my_seg = e_segment.DNASegment()
    my_seg.initial_dict(dict_file_name)
    
    #��ȡ�����ļ�������
    test_file = open(sys.argv[2], "r")
    
    
    precison_sum = 0
    recall_sum = 0
    line_num = 0
    seg_pos_precision_sum = 0
    seg_pos_recall_sum = 0
    line_list = test_file.readlines()

    for i in range(0,len(line_list),3):
        #�ַ���
        line = line_list[i].strip()
        seq_letter_list = line
        
        #�ṹ��
        struct_line = line_list[i+1].strip()
        struct_letter_list = struct_line

        try:
            #standard_seg_list = stardard_seg.mp_seg(line).split(" ")
            my_seg_list = my_seg.mp_seg(seq_letter_list).split(" ")
            standard_seg_list = seg_stru.stu_seg(seq_letter_list, struct_letter_list).split(" ")
            #my_seg_list = seg_stru.stu_seg(seq_letter_list, struct_letter_list).split(" ")
        except Exception as e:
            print "line error",e,line
            continue
        #print standard_seg_list
        #print my_seg_list
        #׼ȷ��
        (precison, recall) = get_pr(standard_seg_list, my_seg_list)

        #�ʱ߽��׼ȷ��
        (seg_pos_precision, seg_pos_recall) = get_seg_pos_precision(standard_seg_list, my_seg_list)
        seg_pos_precision_sum += seg_pos_precision
        seg_pos_recall_sum += seg_pos_recall
        print seg_pos_precision
        #print precison, recall
        #������
        precison_sum += precison
        recall_sum += recall
        line_num += 1

    p = float(precison_sum)/line_num
    r = float(recall_sum)/line_num
    f = 2*p*r/(p+r)
    border_p = float(seg_pos_precision_sum)/line_num
    border_r = float(seg_pos_recall_sum)/line_num
    border_f = 2*border_p*border_r/(border_p+border_r)
    print "avg precision", p
    print "avg recall", r
    print "avg f-score", f
    print "avg seg pos precision", border_p
    print "avg seg pos recall", border_r
    print "avg seg pos f-score", border_f

