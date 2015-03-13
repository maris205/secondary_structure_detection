#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Fri 13 Mar 2015 05:20:56 PM CST
# File Name: run_hdp_experiment.sh
# Description: run hdp segmentation test,get segmentaiton $filename.seg.words
#########################################################################
if [ $# -ne 1 ]
then
    echo "please input protein sequence file name"
    exit
fi

filename=$1
./segment $filename -w0 -o $filename.hdp_seg
