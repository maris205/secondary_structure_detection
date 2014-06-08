#!/bin/sh
if [ $# -ne 1 ]
then
    echo "please input circle num"
    exit
fi
#输入参数为当前运行的轮数，第一次为1轮，需要准备初始数据
#对应的轮次编号就是0
#数值文件名为 dict_轮数_l.norm,dict_轮数_r.norm
set -x

pre_i=$[ $1-1 ] #上一轮数据
l_score=dict_${pre_i}_l.norm #左值
r_score=dict_${pre_i}_r.norm #右值
#step 1, 根据右值计算左值
#上传字典文件
hadoop fs -rm mariswang/dict/word_rank_score
hadoop fs -put ${r_score} mariswang/dict/word_rank_score
#处理数据
./hadoop_run_left.sh
#数据处理
cat part-0* > dict_$1_l
rm -f part-0*
./normalize.py dict_$1_l > dict_$1_l.norm

#step 2,根据左值计算右值
#上传字典文件
hadoop fs -rm mariswang/dict/word_rank_score
hadoop fs -put ${l_score} mariswang/dict/word_rank_score
#处理数据 
./hadoop_run_right.sh
#数据处理
cat part-0* > dict_$1_r
rm -f part-0*
./normalize.py dict_$1_r > dict_$1_r.norm
