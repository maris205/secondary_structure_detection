#!/bin/sh
for ((i=6;i<13;i++))
do
    echo $i
    ./segment ss_06.dat.seg$i > ss_06.dat.seg$i.pr
done
