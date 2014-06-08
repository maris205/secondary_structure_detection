#!/bin/sh
if [ $# -ne 1 ]
then
    echo "please input word file name"
    exit
fi


set -x

file=$1
base="ss_06_f2"
#freq,1
./get_svm_data.py ${base}.freq_feature $file 1 > svm.1
#prob,2
./get_svm_data.py ${base}.prob_feature svm.1 2 > svm.2
#ngram bf, 3
./get_svm_data.py ${base}.bf_feature svm.2 3 > svm.3
#mi,4
./get_svm_data.py ${base}.mi_feature svm.3 4 > svm.4
#bf,5
./get_svm_data.py ${base}.wbf_feature svm.4 5 > svm.5
#word rank,6
#./get_svm_data.py ${base}.wrk_feature svm.5 6 > svm.6
#word length
./get_svm_data.py ${base}.len_feature svm.5 6 > svm.6

#convert
awk -F "\t" '{print $2}' svm.6 > ${file}.svm
