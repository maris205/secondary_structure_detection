#!/bin/sh
test_data=test1.dat
mapper=./em_mapper.py
reducer=./em_reducer.py

cat ${test_data}|${mapper}|sort -k1,1|${reducer}

