#!/bin/sh
test_data=swiss.pr
mapper=./word_rank_mapper.py
reducer=./word_rank_reducer.py

cat ${test_data}|${mapper}|sort -k1,1|${reducer}

