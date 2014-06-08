#!/bin/sh
for ((i=6;i<13;i++))
do
    echo $i
    ./segment_long_structure_word.py  ss_06.dat.dict ss_06.dat $i > ss_06.dat.seg$i
done
