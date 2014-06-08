#!/usr/bin/env python
#coding=utf-8
import sys 
import math
import e_segment
import seg_stru
#分词效果评测
#获得分词准确率和覆盖率
#分别加载标准词典和训练出来的词典，然后比较

#根据分词结果，获得分割点对，作为分词评测的基础数据
def get_seg_node_pair_list(seg_list):
    seg_node_list = []
    start_node = 0
    end_node = 0
    for seg in seg_list:
        end_node = start_node + len(seg)
        seg_node_list.append( (start_node, end_node) )
        start_node = end_node
    return seg_node_list

#根据分割，获得分割点位置列表
def get_seg_node_list(seg_list):
    seg_node_list = []
    node = 0
    for seg in seg_list:
        seg_node_list.append(node)
        node += len(seg)
    #last node
    seg_node_list.append(node)
    return seg_node_list

#获得边界的准确率
def get_seg_pos_precision(standard_seg_list, my_seg_list):
    #共同的分割点数目
    standard_seg_pos_list = get_seg_node_list(standard_seg_list)
    my_seg_pos_list = get_seg_node_list(my_seg_list)

    same_num = len( set(standard_seg_pos_list)&set(my_seg_pos_list) )
    #边界准确率，就是我的分割点，位于标准分割点的比例
    precision = float(same_num-1)/(len(my_seg_pos_list)-1)
    
    #边界覆盖率,覆盖率就是标准分割点位于预测分割点的比例，这个是核心指标
    recall = float(same_num-1)/(len(standard_seg_pos_list)-1)
    return (precision,recall)

def get_pr(standard_seg_list, my_seg_list):
    #统计分割位置点，前后点算一个
    stardard_seg_node_list = get_seg_node_pair_list(standard_seg_list)
    my_seg_node_list = get_seg_node_pair_list(my_seg_list)
    #print stardard_seg_node_list
    #print my_seg_node_list
    #查看两个list共同的部分的个数
    same_num = len( set(stardard_seg_node_list)&set(my_seg_node_list) )
    #准确率
    precision = float(same_num) /len(my_seg_node_list)
    #覆盖率
    recall = float(same_num) /len(stardard_seg_node_list)
    
    return (precision,recall)

    
if __name__=="__main__":
    if len(sys.argv) != 3:
        print "please input dict file and test data file"
        sys.exit()


    #训练的词典
    dict_file_name = sys.argv[1]
    my_seg = e_segment.DNASegment()
    my_seg.initial_dict(dict_file_name)
    
    #读取测试文件并测试
    test_file = open(sys.argv[2], "r")
    
    
    precison_sum = 0
    recall_sum = 0
    line_num = 0
    seg_pos_precision_sum = 0
    seg_pos_recall_sum = 0
    line_list = test_file.readlines()

    for i in range(0,len(line_list),3):
        #字符串
        line = line_list[i].strip()
        seq_letter_list = line
        
        #结构串
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
        #准确率
        (precison, recall) = get_pr(standard_seg_list, my_seg_list)

        #词边界的准确率
        (seg_pos_precision, seg_pos_recall) = get_seg_pos_precision(standard_seg_list, my_seg_list)
        seg_pos_precision_sum += seg_pos_precision
        seg_pos_recall_sum += seg_pos_recall
        print seg_pos_precision
        #print precison, recall
        #覆盖率
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

