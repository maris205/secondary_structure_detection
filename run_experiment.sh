#!/bin/sh
#########################################################################
# Author: billczhang
# Created Time: Sat 26 Dec 2015 01:51:48 PM CST
# File Name: run_experiment.sh
# Description: protein word  experiment
#########################################################################
set -x
#1 pre process data
cd ori_data
./pre_process.sh
cd -

#2 run protein segmentation experiment 
cd paper_experiment
./run_protein_segment_experiment.sh
cd -

#3 ,segment dna sequence
#You need install Biopython first
# copy the file Translate.py in "paper_experiment/dna_segment" directory to the directory where Biopython install. Normally, it’s “/usr/local/lib/python2.7/site-packages/Bio”
cd paper_experiment/dna_segment
./run_dna_segment_experiment.sh
cd -
