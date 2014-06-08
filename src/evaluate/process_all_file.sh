#!/bin/sh
ls *_feature|while read line
do
    echo $line
    awk -F "\t" 'length($1)==6 {print $0}' $line > $line.len6
    awk -F "\t" '$3==1 {print $0}' $line.len6 > $line.len6.word
    awk -F "\t" '$3==0 {print $0}' $line.len6 > $line.len6.noword
done
