#!/usr/bin/env python
#coding=utf-8
#############################################################
#function: viterbi/(max probility) segment
#          a dynamic programming method
#
#input: dict file
#output: segmented words, divide by delimiter " "
#author: wangliang.f@gmail.com
##############################################################
import sys
import math

#global parameter
DELIMITER = " " #分词之后的分隔符

class ViterbiSegment:
    def __init__(self):
        self.word_dict = {} #记录概率
        self.word_dict_count = {} #记录词频
        self.gmax_word_length = 0
        self.all_freq = 0 #所有词的词频总和

    #估算未出现的词的概率,根据beautiful data里面的方法估算
    def get_unkonw_word_prob(self, word):
        one_freq_prob = float(1)/1000000000 #最小的概率
        return math.log(10./(one_freq_prob*10**len(word)))

    #寻找node的最佳前驱节点
    #方法为寻找所有可能的前驱片段
    def get_best_pre_node(self, sequence, node, node_state_list):
        #如果node比最大词长小，取的片段长度以node的长度为限
        max_seg_length = min([node, self.gmax_word_length])
        pre_node_list = [] #前驱节点列表

        #获得所有的前驱片段，并记录累加概率
        for segment_length in range(1,max_seg_length+1):
            segment_start_node = node-segment_length
            segment = sequence[segment_start_node:node] #获取片段

            pre_node = segment_start_node  #若取该片段，则记录对应的前驱节点
            pre_node_prob_sum = node_state_list[pre_node]["prob_sum"] #前驱节点的概率累加值

            #获得片段的概率
            if (self.word_dict.has_key(segment)): #如果字典包含这个词
                segment_prob = self.word_dict[segment]
            else: #如果没有这个词，则取一个很小的概率
                #segment_prob = self.get_unkonw_word_prob(segment)
                continue

            #当前node一个候选前驱节点到当前node的累加概率值
            candidate_prob_sum = pre_node_prob_sum + segment_prob 
    
            pre_node_list.append((pre_node, candidate_prob_sum))

        #找到最大的候选概率值
        (best_pre_node, best_prob_sum) = max(pre_node_list,key=lambda d:d[1])
        return (best_pre_node, best_prob_sum) 
    
    #最大概率分词,返回分词结果和概率
    def mp_seg_prob(self, sequence):
        sequence = sequence.strip()

        #初始化
        node_state_list = [] #记录节点的状态，该数组下标对应节点位置
        #初始节点，也就是0节点信息
        ini_state = {}
        ini_state["pre_node"] = -1 #前一个节点
        ini_state["prob_sum"] = 0 #当前的概率总和
        node_state_list.append( ini_state )

        #逐个节点寻找最佳前驱节点
        #字符串概率为1元概率,#P(ab c) = P(ab)P(c)
        for node in range(1,len(sequence) + 1):
            #寻找最佳前驱节点，并记录当前最大的概率累加值
            (best_pre_node, best_prob_sum) = \
                    self.get_best_pre_node(sequence,node,node_state_list)

            #记录当前节点信息
            cur_node = {}
            cur_node["pre_node"] = best_pre_node
            cur_node["prob_sum"] = best_prob_sum
            node_state_list.append(cur_node)

        # step 2, 获得最优路径,从后到前
        best_path = []
        node = len(sequence) #最后一个点
        best_path.append(node)
        while True:
            pre_node = node_state_list[node]["pre_node"]
            if pre_node == -1:
                break
            node = pre_node
            best_path.append(node)
        best_path.reverse()

        # step 3, 构建切分
        word_list = []
        for i in range(len(best_path)-1):
            left = best_path[i]
            right = best_path[i + 1]
            word = sequence[left:right]
            word_list.append(word)

        seg_sequence = DELIMITER.join(word_list)
        return seg_sequence,node_state_list[-1]["prob_sum"]

    #最大概率分词
    def mp_seg(self, sequence):
        sequence = sequence.strip()

        #初始化
        node_state_list = [] #记录节点的状态，该数组下标对应节点位置
        #初始节点，也就是0节点信息
        ini_state = {}
        ini_state["pre_node"] = -1 #前一个节点
        ini_state["prob_sum"] = 0 #当前的概率总和
        node_state_list.append( ini_state )
        
        #逐个节点寻找最佳前驱节点
        #字符串概率为1元概率,#P(ab c) = P(ab)P(c)
        for node in range(1,len(sequence) + 1):
            #寻找最佳前驱节点，并记录当前最大的概率累加值
            (best_pre_node, best_prob_sum) = \
                    self.get_best_pre_node(sequence,node,node_state_list)
            
            #记录当前节点信息
            cur_node = {}
            cur_node["pre_node"] = best_pre_node
            cur_node["prob_sum"] = best_prob_sum
            node_state_list.append(cur_node)

        # step 2, 获得最优路径,从后到前
        best_path = []
        node = len(sequence) #最后一个点
        best_path.append(node)
        while True:
            pre_node = node_state_list[node]["pre_node"]
            if pre_node == -1:
                break
            node = pre_node
            best_path.append(node)
        best_path.reverse()

        # step 3, 构建切分
        word_list = []
        for i in range(len(best_path)-1):
            left = best_path[i]
            right = best_path[i + 1]
            word = sequence[left:right]
            word_list.append(word)

        seg_sequence = DELIMITER.join(word_list)
        return seg_sequence
    
    #加载词典，为词\t词频的格式
    def initial_dict(self,filename, max_word_length=10000):
        dict_file = open(filename, "r")
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            if len(key)<=max_word_length: #如果设置了最大长度值
                self.word_dict_count[key] = value

        #计算频率
        self.all_freq = sum(self.word_dict_count.itervalues()) #所有词的词频
        self.gmax_word_length = \
            max(len(key) for key in self.word_dict_count.iterkeys()) #所有词的词频
        
        #计算每个词的概率，用log形式
        for key in self.word_dict_count:
            value = self.word_dict_count[key]
            if value!=0 and len(key)<=self.gmax_word_length:
                self.word_dict[key] = math.log(value/self.all_freq)  #取自然对数

#test
if __name__=='__main__':
    if len(sys.argv) != 3: 
        print "please input dict and sequence file name"
        sys.exit(0)

    myseg = ViterbiSegment()
    myseg.initial_dict(sys.argv[1])
    data_file=open(sys.argv[2], "r")
    for line in data_file:
        line = line.strip()
        try:
            print myseg.mp_seg(line)
        except:
        #if error, please check "error" word in output
            print "error line ", line
            continue 
