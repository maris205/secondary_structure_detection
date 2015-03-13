#!/bin/sh
#########################################################################
# Author: billczhang
# Created Time: Thu 12 Feb 2015 03:22:27 PM CST
# File Name: build_standard_seg.sh
# Description: build gold standard segmentaiton
#input file is structure file, a record contains 3 lines, one sequence ,one sequence and one space line
#there are two standard segmentation, first, we use the original structure segmentation ,  "*.stu_seg"
#second, we set 9 as the maximal word length of segmentaiton,
#"*.stu_length_limit_seg"
#########################################################################
if [ $# -ne 1 ]
then
    echo "please input structure file name"
    exit
fi
set -x
filename=$1
max_word_length=9 # you can set other value
#step 1, get structure segmentation
./structure_segment.py $filename > $filename.structure_seg

#step 2, get structure segmentaiton, set maximal word length 9
#get structure vocabulary with frequency, maximal word length is 9
sed 's/ /\n/g' $filename.structure_seg | sort| uniq -c|sort -r -n -k1,1 |awk 'length($2)<='''$max_word_length''' && length($2)>0 {print $2"\t"$1}' > $filename.structure_dict_length9

#seg the long structure segmentation into short segments
./structure_segment_limit_length.py $filename.structure_dict_length9 $filename $max_word_length > $filename.structure_limit_length_seg

