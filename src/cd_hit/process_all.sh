#!/bin/sh
ls split_data/x* | while read line
do
    echo $line
    ./filter.sh $line
done
