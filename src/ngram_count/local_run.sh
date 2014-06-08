#!/bin/sh
test_data=test.dat
mapper=./ngram_count_mapper.py
reducer=./ngram_count_reducer.py

cat ${test_data}|${mapper}|sort -k1,1|${reducer}

