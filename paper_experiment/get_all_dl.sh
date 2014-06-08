#!/bin/sh
for ((i=6;i<13;i++))
do
    echo $i
    ./mdl.py ss_06.dat.seg$i
done
