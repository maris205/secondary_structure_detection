#!/bin/sh
hadoop fs -rmr mariswang/output_ngram_dssp
hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -input mariswang/data/mo.17s.pr.uniq \
    -output mariswang/output_ngram_dssp \
    -mapper "ngram_count_mapper.py" \
    -reducer "ngram_count_reducer.py" \
    -file ngram_count_mapper.py \
    -file ngram_count_reducer.py \
    -jobconf  mapred.reduce.tasks=10 \
    -jobconf  mapred.job.name="mariswang_ngram_dssp" 
#get data
hadoop fs -get mariswang/output_ngram_dssp/part-0* ./
