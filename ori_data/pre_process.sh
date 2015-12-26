#!/bin/sh
#preprocess data
set -x
unzip ss.zip

#get fasta format file
./get_fasta_file.py ss.txt > ss.fasta

#delete similar sequence
./cd-hit -i ss.fasta -o  ss.fasta.uniq -c 0.6 -n 4 -M 20000
#get pid
grep '>' ss.fasta.uniq > ss.fasta.uniq.pid #get pid

#get final experimental data
./get_experiment_data.py ss.fasta.uniq.pid ss.txt > ss_06.dat

#get protein sequence
awk 'NR%3==1 {print $0}' ss_06.dat> ss_06.dat.pr

#copy data
cp ss_06.dat  ../paper_experiment/evaluation/
cp ss_06.dat.pr  ../paper_experiment/soft_counting
cp ss_06.dat.pr  ../paper_experiment/hdp
