#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Thu 12 Feb 2015 03:22:27 PM CST
# File Name: local_run_ngram_count.sh
# Description: run ngram count
# input file:  protein files, its format, one line one protein sequence
# output file: $filename.ngram, all possible sub-string of sequence with frequency
#########################################################################
if [ $# -ne 1 ]
then
    echo "please input protein file name"
    exit
fi
filename=$1
mapper=./ngram_count_mapper.py
reducer=./ngram_count_reducer.py

#step 1, ngram count. the default max word length is 9, this value could
# revised in ngram_count_mapper.py
cat ${filename}|${mapper}|sort -k1,1|${reducer} > $filename.ngram9

#step 2, filter vocabulary by frequency, here we set 3 as the lowest frequency
awk '$2>2 {print $0}' $filename.ngram9 > $filename.ngram9.freq6

#step 3, filter sub string of long string if they have same frequency
./sub_seq_filter.py $filename.ngram9.freq6 > $filename.ngram9.freq6.sub

#step 4, description length gain filter 
./description_length_gain_filter.py $filename $filename.ngram9.freq6.sub > $filename.ngram
