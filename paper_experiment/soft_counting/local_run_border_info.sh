#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Fri 06 Mar 2015 05:23:29 PM CST
# File Name: local_run_border_info.sh
# Description: 
#########################################################################
if [ $# -ne 2 ]
then
    echo "please input corpus and dict file name"
    exit
fi

corpus=$1
dict=$2

cp $dict data.dict

#get left border info
cat $corpus | ./get_left_ngram_border_info_mapper.py | sort -k1,1|./get_ngram_border_info_reducer.py > $dict.lbf

#get right border info
cat $corpus | ./get_right_ngram_border_info_mapper.py | sort -k1,1|./get_ngram_border_info_reducer.py > $dict.rbf

#combine border info
./combine_border_info.py $dict.lbf  $dict.rbf >  $dict.bf

#filter vocabuary according to border info 
./filter_vocabulary_by_border_info.py $dict $dict.bf > $dict.wbf 
