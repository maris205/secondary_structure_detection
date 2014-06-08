#!/bin/sh
for ((i=0;i<9;i++))
do
    dict_file=dict_${i}
    echo "process dict file "${dict_file} 
    #step 1,覆盖hadoop上的dict文件
    hadoop fs -rm mariswang/dict/dict_soft
    hadoop fs -put ${dict_file} mariswang/dict/dict_soft
    #step 2,运行hadoop
    ./hadoop_run.sh
    #复制文件为下一个词典,为下一轮处理做准备
    new_dict=$[ $i+1 ]
    new_dict=dict_${new_dict}
    cat part-* > part_temp
    ./convert_dict.py part_temp > ${new_dict}
    rm -f part*
done
