#!/bin/sh
ls part-000*|while read line
do
    echo $line
    awk -F "\t" '$2>=10 {print $0}' ${line} > ${line}.len10
done
