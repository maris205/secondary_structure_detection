#!/bin/sh
file=$1
#./cd-hit -i $file -o  ${file}.uniq -c 0.8 -n 5 -M 20000
./cd-hit -i $file -o  ${file}.uniq -c 0.6 -n 4 -M 20000
#./cd-hit -i $file -o  ${file}.uniq -c 0.4 -n 2 -M 20000
