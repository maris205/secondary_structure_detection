#!/usr/bin/env python
#coding=utf-8
import sys

#chou-fasman的基本参数
CF = {}
CF['Alanine']       = ['A', 142,   83,   66,   0.06,   0.076,  0.035,  0.058]
CF['Arginine']      = ['R',  98,   93,   95,   0.070,  0.106,  0.099,  0.085]
CF['Aspartic Acid'] = ['N', 101,   54,  146,   0.147,  0.110,  0.179,  0.081]
CF['Asparagine']    = ['D',  67,   89,  156,   0.161,  0.083,  0.191,  0.091]
CF['Cysteine']      = ['C',  70,  119,  119,   0.149,  0.050,  0.117,  0.128]
CF['Glutamic Acid'] = ['E', 151,   37,   74,   0.056,  0.060,  0.077,  0.064]
CF['Glutamine']     = ['Q', 111,  110,   98,   0.074,  0.098,  0.037,  0.098]
CF['Glycine']       = ['G',  57,   75,  156,   0.102,  0.085,  0.190,  0.152]
CF['Histidine']     = ['H', 100,   87,   95,   0.140,  0.047,  0.093,  0.054]
CF['Isoleucine']    = ['I', 108,  160,   47,   0.043,  0.034,  0.013,  0.056]
CF['Leucine']       = ['L', 121,  130,   59,   0.061,  0.025,  0.036,  0.070]
CF['Lysine']        = ['K', 114,   74,  101,   0.055,  0.115,  0.072,  0.095]
CF['Methionine']    = ['M', 145,  105,   60,   0.068,  0.082,  0.014,  0.055]
CF['Phenylalanine'] = ['F', 113,  138,   60,   0.059,  0.041,  0.065,  0.065]
CF['Proline']       = ['P',  57,   55,  152,   0.102,  0.301,  0.034,  0.068]
CF['Serine']        = ['S',  77,   75,  143,   0.120,  0.139,  0.125,  0.106]
CF['Threonine']     = ['T',  83,  119,   96,   0.086,  0.108,  0.065,  0.079]
CF['Tryptophan']    = ['W', 108,  137,   96,   0.077,  0.013,  0.064,  0.167]
CF['Tyrosine']      = ['Y',  69,  147,  114,   0.082,  0.065,  0.114,  0.125]
CF['Valine']        = ['V', 106,  170,   50,   0.062,  0.048,  0.028,  0.053]


aa_names = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic Acid',
            'Cysteine', 'Glutamic Acid', 'Glutamine', 'Glycine',
            'Histidine', 'Isoleucine', 'Leucine', 'Lysine',
            'Methionine', 'Phenylalanine', 'Proline', 'Serine',
            'Threonine', 'Tryptophan', 'Tyrosine', 'Valine']

Pa = { }
Pb = { }
Pturn = { }
F0 = { }
F1 = { }
F2 = { }
F3 = { }

#写成单字母的kv形式
# Convert the Chou-Fasman table above to more convenient formats
#    Note that for any amino acid, aa CF[aa][0] gives the abbreviation
#    of the amino acid.
for aa in aa_names:
    Pa[CF[aa][0]] = CF[aa][1]
    Pb[CF[aa][0]] = CF[aa][2]
    Pturn[CF[aa][0]] = CF[aa][3]
    F0[CF[aa][0]] = CF[aa][4]
    F1[CF[aa][0]] = CF[aa][5]
    F2[CF[aa][0]] = CF[aa][6]
    F3[CF[aa][0]] = CF[aa][7]

def combine_zone(zone_list):
    #按照起点排序
    sort_list = sorted(zone_list, key=lambda d:d[0])
    #合并后的区间
    new_zone_list = []
    zone = sort_list[0] #初始化
    for item in sort_list[1:]:
        if item[0] == zone[0]:#如果起点相同
            if item[1] > zone[1]: #新的区间终点大于先有终点，则扩展zone
                zone[1] = item[1] #如果小于则不做任何处理
        else: #如果起点大于zone的起点
            if item[0] <= zone[1]: #如果起点位于zone的内部
                if item[1] > zone[1]: #新的区间终点大于先有终点，则扩展zone
                    zone[1] = item[1] #如果小于则不做任何处理
            else: #如果起点位于zone的外部，则说明有截断的情况，更新
                new_zone_list.append(zone)
                zone = item
    #处理最后一个元素
    if len(new_zone_list)==0 or new_zone_list[-1] != zone:
        new_zone_list.append(zone)
    return new_zone_list

#判断alpha结构，返回 [start,end]对
def find_alpha(seq):
    start = 0
    results = []
    ngram_length = 6 #窗口长度
    for i in range(0,len(seq)-ngram_length+1):
        #处理每一个窗口
        start_pos = i
        end_pos = i+ngram_length
        # 寻找 alpha helix 核
        numgood = 0
        for i in range(start_pos, end_pos):
            if (Pa[seq[i]] > 100):
                numgood = numgood + 1
        if (numgood >= 4): #如果其中4个核大于100，则进行扩展
            #print start_pos, end_pos, seq[start_pos:end_pos] 
            (left_pos, right_pos) = extend_alpha(seq, start_pos, end_pos)
            #print "extend ",left_pos, right_pos, seq[left_pos:right_pos]
            results.append([left_pos, right_pos])
    
    if len(results)==0: #如果没有对应的结果
        return 0
    #print results
    results_combine = combine_zone(results)
    print "alpha",results_combine
    if len(results_combine)==1 and ( results_combine[0][1]-results_combine[0][0] == len(seq) ):
        seg = seq[results_combine[0][0]:results_combine[0][1]]
        #print seg
        pa_sum = sum([ Pa[x] for x in seg])
        pb_sum = sum([ Pb[x] for x in seg ])
        #print pa_sum,pb_sum
        if pa_sum > pb_sum:
            return 1
        else:
            return 0
    else:
        return 0

#alpha helix扩展
def extend_alpha(seq, start, end):
    ngram_length = 4
    #向右边扩展
    right_pos = end
    for i in range(end-3,len(seq)-ngram_length+1):
        start_pos = i
        end_pos = i + ngram_length
        avg = float( sum([Pa[x] for x in seq[start_pos:end_pos]]) )/4
        #print start_pos, end_pos, seq[start_pos:end_pos],avg
        if avg>=100:
            right_pos = end_pos
        else:
            break
    #print "right pos ", right_pos
    left_pos = start
    #向左边扩展,这里i是结束位置
    for i in range(start+3, ngram_length-1, -1):
        end_pos = i
        start_pos = i-ngram_length
        avg = float( sum([Pa[x] for x in seq[start_pos:end_pos]]) )/4
        #print start_pos, end_pos, seq[start_pos:end_pos],avg
        if avg>=100:
            left_pos = start_pos;
        else:
            break
    #print "left pos", left_pos
    return (left_pos, right_pos)



###########################################
#find beta
def find_beta(seq):
    start = 0
    results = []
    ngram_length = 5 #窗口长度
    for i in range(0,len(seq)-ngram_length+1):
        #处理每一个窗口
        start_pos = i
        end_pos = i+ngram_length
        # 寻找 alpha helix 核
        numgood = 0
        for i in range(start_pos, end_pos):
            if (Pa[seq[i]] > 100):
                numgood = numgood + 1
        if (numgood >= 3): #如果其中3个核大于100，则进行扩展
            #print start_pos, end_pos, seq[start_pos:end_pos] 
            (left_pos, right_pos) = extend_beta(seq, start_pos, end_pos)
            #print "extend ",left_pos, right_pos, seq[left_pos:right_pos]
            results.append([left_pos, right_pos])
    
    if len(results)==0: #如果没有对应的结果
        return 0
    #print results
    results_combine = combine_zone(results)
    print "beta",results_combine
    if len(results_combine)==1 and ( results_combine[0][1]-results_combine[0][0] == len(seq) ):
        seg = seq[results_combine[0][0]:results_combine[0][1]]
        #print seg
        pa_sum = sum([ Pa[x] for x in seg])
        pb_sum = sum([ Pb[x] for x in seg ])
        #print pa_sum,pb_sum
        if pa_sum < pb_sum:
            return 1
        else:
            return 0
    else:
        return 0

#beta band扩展
def extend_beta(seq, start, end):
    ngram_length = 4
    #向右边扩展
    right_pos = end
    for i in range(end-3,len(seq)-ngram_length+1):
        start_pos = i
        end_pos = i + ngram_length
        avg = float( sum([Pb[x] for x in seq[start_pos:end_pos]]) )/4
        #print start_pos, end_pos, seq[start_pos:end_pos],avg
        if avg>=100:
            right_pos = end_pos
        else:
            break
    #print "right pos ", right_pos
    left_pos = start
    #向左边扩展,这里i是结束位置
    for i in range(start+3, ngram_length-1, -1):
        end_pos = i
        start_pos = i-ngram_length
        avg = float( sum([Pb[x] for x in seq[start_pos:end_pos]]) )/4
        #print start_pos, end_pos, seq[start_pos:end_pos],avg
        if avg>=100:
            left_pos = start_pos;
        else:
            break
    #print "left pos", left_pos
    return (left_pos, right_pos)

###################################################
#turn 规则
def find_turns(seq):
    results = []
    ngram_length = 4
    for i in range(len(seq)-ngram_length+1):
    # CONDITION 1
        c1 = F0[seq[i]]*F1[seq[i+1]]*F2[seq[i+2]]*F3[seq[i+3]] > 0.000075
    # CONDITION 2
        c2 = ( float(sum([Pturn[x] for x in seq[i:i+4]])) / float(4) ) > 100 
    # CONDITION 3
        c3 = sum([Pturn[x] for x in seq[i:i+4]]) > max(sum([Pa[x] for x in seq[i:i+4]]),sum([Pb[x] for x in seq[i:i+4]]))
        if c1 and c2 and c3: 
            results.append([i,i+4])

    if len(results)==0: #如果没有对应的结果
        return 0
    results_combine = combine_zone(results)
    #print results
    print "turn",results_combine
    if len(results_combine)==1 and (results_combine[0][1]-results_combine[0][0]==len(seq) ):
        return 1
    else:
        return 0

def judge_if_word(seq):
    if find_alpha(seq) or find_beta(seq) or find_turns(seq):
        return 1
    else:
        return 0

if __name__=="__main__":
    seq = "MKIDAIVGRNSAKDI"
    #print find_alpha(seq)
    #print find_beta(seq)
    #print find_turns(seq)
    for line in sys.stdin:
        seq = line.strip()
        print "len seq",len(seq)
        try:
            print judge_if_word(seq)
        except:
            continue
