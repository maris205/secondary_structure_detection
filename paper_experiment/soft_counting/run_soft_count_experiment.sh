#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Thu 12 Feb 2015 03:22:27 PM CST
# File Name: run_soft_count_experiment.sh
# Description: run soft-counting experiment, input file is protein files, 
# its format, one line one protein sequence
#########################################################################
if [ $# -ne 1 ]
then
    echo "please input protein file name"
    exit
fi
set -x
filename=$1
#set max word length as 9, you can set other length
max_word_length=9

#step 1, get all possible sub-string/words by ngram segmentation methods
./local_run_ngram_count.sh $filename

#step 2, run soft counting algorithms，get vocabulary with probability
./local_run_soft_count.sh  $filename $filename.ngram

#step 3, run border information filter, get final vocabulary $filename.ngram.em
./local_run_border_info.sh $filename $filename.ngram

#step 4, segment the test data
cp $filename.ngram.em $filename.dict
./viterbi_segment.py $filename.dict $filename > $filename.soft_count_seg 

