#!/bin/sh
#计算left的值，用right的值
hadoop fs -rmr mariswang/output_word_rank_score
hadoop org.apache.hadoop.streaming.HadoopStreaming \
    -input mariswang/data/dict_0.sort.300wan.l_to_r \
    -output mariswang/output_word_rank_score \
    -mapper "word_rank_score_mapper.py" \
    -reducer "word_rank_score_reducer.py" \
    -file word_rank_score_mapper.py \
    -file word_rank_score_reducer.py \
    -cacheFile  mariswang/dict/word_rank_score#word_rank_score \
    -jobconf mapred.reduce.tasks=5 \
    -jobconf mapred.job.name="mariswang_word_rank_score"
#get data
hadoop fs -get mariswang/output_word_rank_score/part-0* ./
