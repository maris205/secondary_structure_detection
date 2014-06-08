#!/bin/sh
hadoop fs -rmr mariswang/output_word_rank
hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -input mariswang/data/ss.pr.uniq \
    -output mariswang/output_word_rank \
    -mapper "word_rank_mapper.py" \
    -reducer "word_rank_reducer.py" \
    -file word_rank_mapper.py \
    -file word_rank_reducer.py \
    -cacheFile  mariswang/dict/dict_0.sort.300wan#dict_0.sort.300wan \
    -jobconf mapred.reduce.tasks=5\
    -jobconf mapred.job.name="mariswang_word_rank"
#get data
hadoop fs -get mariswang/output_word_rank/part-0* ./
