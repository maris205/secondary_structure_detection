#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Sat 26 Dec 2015 01:22:10 PM CST
# File Name: run_protein_segment_experiment.sh
#Description:  soft-counting segment and evaluation
#########################################################################
set -x
#1 run soft-counting segment
cd soft_counting
./run_soft_count_experiment.sh ss_06.dat.pr
cp ss_06.dat.pr.soft_count_seg ../evaluation
cd -


#you could also run hdp segment,but may spend 10+ or more hours
#cd hdp
#./run_hdp_experiment.sh
#cp ss_06.dat.pr.hdp_seg.words ../evaluation
#cd -

#2 evaluation the segment result
cd evaluation
#build the gold-standard segmentation
./build_standard_seg.sh ss_06.dat
cp ss_06.dat.structure_dict_length9 ../dna_segment
#evaluation
./evaluate_segment.py ss_06.dat.structure_limit_length_seg ss_06.dat.pr.soft_count_seg
#description length
./get_description_length.py ss_06.dat.structure_seg
./get_description_length.py ss_06.dat.pr.soft_count_seg
