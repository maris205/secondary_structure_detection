#!/bin/sh
if [ $# -ne 2 ]
then
    echo "please input corpus and dict file name"
    exit
fi
set -x
#here corpus data is protein sequence. one line one sequence 
#dict is initial vocabulary
corpus=$1
dict=$2

cp $dict dict_0

#in most condition, the word probability will converge in 5 circles run
mapper=./soft_count_mapper.py
reducer=./soft_count_reducer.py

for ((i=0;i<5;i++))
do
    dict_file=dict_${i}
    cp ${dict_file} "dict_soft"
    echo "process dict file "${dict_file} 
    #run soft count
    cat $corpus |${mapper}|sort -k1,1|${reducer} > "temp.dict"
    #cp new dict as the input of next circle 
    new_dict=$[ $i+1 ]
    new_dict=dict_${new_dict}
    #normalize the vocabulary
    ./normalize_dict.py  temp.dict > ${new_dict}
done
cp dict_5 $dict.em
