We use the unsupervised word segmentation method to analyze the protein sequence.
We find the segmented protein words sequence is similar to protein secondary structure.

Directory:
ori_data: contain the original data and preprocess code.
paper_experiment: experiment for paper 
src: some unsupervised segment method code (python)
our paper: http://arxiv.org/abs/1404.6866

Data source:
From this page: 
http://www.rcsb.org/pdb/static.do?p=download/http/index.html
We download:
http://www.rcsb.org/pdb/files/ss.txt.gz
We have downloaded this data in  ��ori_data�� directory as ��ss.zip��, so you need ��unzip�� this file first.

Preliminary software:
1 cd-hits, we use this tools to delete the similar sequence. It could be found in http://weizhong-lab.ucsd.edu/cd-hit/download.php, after installing it, please copy file ��cd-hit�� to ��ori_data�� of this project.(these has been a cd-hit in this directory, but may not run in different Linux systems)
2 HDP, an unsupervised segment methods, it��s normally regarded as the best unsupervised segment method. It could be found in http://homepages.inf.ed.ac.uk/sgwater/resources.html
. After installing it, please copy its file ��segment�� to ��paper_experiment�� directory of this project.
3 python, 2.6 or 2.7

Experiment for paper

1 preprocess, mainly filter the similar sequence (in ��ori_data�� directory)
./get_fasta_file.py ss.txt > ss.fasta   #get fasta format file
./cd-hit -i ss.fasta -o  ss.fasta.uniq -c 0.6 -n 4 -M 20000 #delete similar sequence
grep '>' ss.fasta.uniq > ss.fasta.uniq.pid #get pid
./get_experiment_data.py ss.fasta.uniq.pid ss.txt > ss_06.dat #get final experimental data
The copy the file ��ss_06.dat�� to directory ��paper_experiment��

You can run ��./pre_process.sh�� to do all the things above.

2 run experiment (in ��paper_experiment�� directory)
#segment the protein sequence according to its secondary structure, get gold-standard segmentation
./structure_segment.py ss_06.dat > ss_06.dat.stru_seg  

#apply HDP segment method to segment the protein sequence, get the precision, recall,f-score
./segment ss_06.dat.stru_seg  > ss_06.dat.stru_seg.score
Its score is about: BP 28.24 BR 55.48 BF 37.43

It may take several hours to get the results. The input of HDP program is the gold-standard segmentation. It first deletes the space between words and run the unsupervised segmenting. Then it compares the segmentation results with the gold-standard segmentation, get the precision, recall, f-score.

#run experiment, set maximal word length
#get secondary structure word list
./get_stu_word_dict.py ss_06.dat > ss_06.dat.dict

#segment long secondary structure segmentation into short one, by setting maximal word length
./segment_long_structure_word.py ss_06.dat.dict ss_06.dat 6 > ss_06.dat.seg6
Here input parameter 6 is the maximal word length, you could set other value.

Then we can run the unsupervised segmentation again:
./segment ss_06.dat.seg6  > ss_06.dat.seg6.score
Its score is about: BP 42.15 BR 55.88 BF 48.06

Some other unsupervised segmentation methods.
Voting-expert: https://code.google.com/p/voting-experts/

Regularized compression method to unsupervised word segmentation:
https://github.com/rueycheng/kinkaseki

