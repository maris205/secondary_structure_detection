#!/bin/sh
if [ $# -ne 1 ]
then
    echo "please input file name"
    exit
fi
filename=$1
sed 's/ /\n/g' $filename|sort|uniq -c|sort -n -k1,1 -r|awk '{print $2"\t"$1}'