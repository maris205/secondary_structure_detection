#!/bin/sh
hadoop fs -rmr mariswang/output_soft
hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -input mariswang/data/ss_06.pr \
    -output mariswang/output_soft \
    -mapper "em_mapper.py" \
    -reducer "em_reducer.py" \
    -file em_mapper.py \
    -file em_reducer.py \
    -cacheFile  mariswang/dict/dict_soft#dict_soft \
    -jobconf mapred.reduce.tasks=10 \
    -jobconf mapred.job.name="mariswang_soft" \
#get data
hadoop fs -get mariswang/output_soft/part-* ./
