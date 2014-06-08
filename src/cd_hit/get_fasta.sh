#!/bin/sh
i=0
ls split_data3/*.fasta|while read line
do
    echo ${line}
    ./filter.sh ${line}
done
