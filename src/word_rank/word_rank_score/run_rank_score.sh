#!/bin/sh
if [ $# -ne 1 ]
then
    echo "please input circle num"
    exit
fi
#�������Ϊ��ǰ���е���������һ��Ϊ1�֣���Ҫ׼����ʼ����
#��Ӧ���ִα�ž���0
#��ֵ�ļ���Ϊ dict_����_l.norm,dict_����_r.norm
set -x

pre_i=$[ $1-1 ] #��һ������
l_score=dict_${pre_i}_l.norm #��ֵ
r_score=dict_${pre_i}_r.norm #��ֵ
#step 1, ������ֵ������ֵ
#�ϴ��ֵ��ļ�
hadoop fs -rm mariswang/dict/word_rank_score
hadoop fs -put ${r_score} mariswang/dict/word_rank_score
#��������
./hadoop_run_left.sh
#���ݴ���
cat part-0* > dict_$1_l
rm -f part-0*
./normalize.py dict_$1_l > dict_$1_l.norm

#step 2,������ֵ������ֵ
#�ϴ��ֵ��ļ�
hadoop fs -rm mariswang/dict/word_rank_score
hadoop fs -put ${l_score} mariswang/dict/word_rank_score
#�������� 
./hadoop_run_right.sh
#���ݴ���
cat part-0* > dict_$1_r
rm -f part-0*
./normalize.py dict_$1_r > dict_$1_r.norm
