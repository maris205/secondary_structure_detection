We use the unsupervised word segmentation method to analyze the protein sequence.
We find the segmented protein words sequence is similar to protein secondary structure.

Directory:
ori_data: contain the original data and preprocess code.
paper_experiment: experiment for paper, it contains this sub directory:
	hdp: hdp algorithm segment test
	soft_count: soft-counting segment test
	evaluation: evaluate the segment results
	dna_segment: dna sequence segment test  
src: some other unsupervised segment method codes, not mentioned in our paper (python)
our paper: http://arxiv.org/abs/1404.6866

Protein Structure Data source:
From this page: 
http://www.rcsb.org/pdb/static.do?p=download/http/index.html
We download:
http://www.rcsb.org/pdb/files/ss.txt.gz
We have pre downloaded this data in ori_data directory as   ss.zip  , so you need   unzip   this file first. It’s the DSSP secondary sstructure. 

Preliminary software:
1 cd-hits, we use this tools to delete the similar sequence. It could be found in http://weizhong-lab.ucsd.edu/cd-hit/download.php, after installing it, please copy file   cd-hit   to   ori_data   of this project.(these has been a “cd-hit” in this directory, only test in centos 64 Linux systems)
2 HDP, an unsupervised segment methods, it  s normally regarded as the best unsupervised segment method. It could be found in http://homepages.inf.ed.ac.uk/sgwater/resources.html
. After installing it, please copy its file “segment” to paper_experiment/hdp directory of this project. (These has been a “segment” file in this directory, only test in centos 64 Linux systems)
3 python, 2.7. Our codes are mainly python codes.
4 latest Biopython (1.63 or latter). You can download from http://biopython.org/wiki/Main_Page.


Experiment for paper:
We mainly use the DSSP secondary structure data. To process other forms of structure assignment data, you could refer to this operation.

1 preprocess, mainly filter the similar sequence (in ori_data directory)
#get fasta format file
/get_fasta_file.py ss.txt > ss.fasta   

#delete similar sequence
./cd-hit -i ss.fasta -o  ss.fasta.uniq -c 0.6 -n 4 -M 20000
#get pid
grep '>' ss.fasta.uniq > ss.fasta.uniq.pid 

#get final experimental data
./get_experiment_data.py ss.fasta.uniq.pid ss.txt > ss_06.dat

#get protein sequence
awk 'NR%3==1 {print $0}' > ss_06.dat.pr

Then copy the file   “ss_06.dat”   to directory   “paper_experiment/evaluation”
Copy the file “ss_06.dat.pr” to directory “paper_experiment/hdp” and “paper_experiment/soft_count”

You can run   ./pre_process.sh   to do all the things above.

2 run experiment (in   paper_experiment   directory)

2.1 run hdp segment
In directory “paper_experiment/hdp”:
Run ./segment ss_06.dat.pr -w0 -o ss_06.dat.pr.hdp_seg
It may take several hours to get the results. We can get the segment result “ss_06.dat.pr.hdp_seg.words”. Then copy this file to directory   “paper_experiment/evaluation”

2.2 run soft-counting segment
In directory “paper_experiment/hdp”:
Run ./run_soft_count_experiment.sh ss_06.dat.pr
We can get the segment result “ss_06.dat.pr.soft_count_seg”. Then copy this file to directory   “paper_experiment/evaluation”

2.3 evaluation the segment result
First, we need use the secondary structure to build the gold-standard segmentation
./build_standard_seg.sh ss_06.dat
Then we get these files:
“ss_06.dat.structure_seg”  # structure segmentation
“ss_06.dat.structure_length_limit_seg”  # set the maximal word length limitation for secondary structure, another gold standard segmentation
“ss_06.dat.structure_dict_length9” #structure word vocabulary with frequency

Then we could compare these two standard segmentation with unsupervised word segmentation, for example, evaluate hdp segmentation, run:
./ evaluate_segment.py ss_06.dat.structure_length_limit_seg ss_06.dat.pr.hdp_seg.words

We also need copy the vocabulary file “ss_06.dat.structure_dict_length9” to  directory   “paper_experiment/ dna_segment”
2.4 segment dna sequence
You should copy the file “Translate.py” in this directory to the directory where Biopython install. Normally, it’s “/usr/local/lib/python2.7/site-packages/Bio”. It contain the back translate function, but this function is deleted in new version. 

Then run:
./run_dna_segment_experiment.sh

We also prepare English corpus in “ori_data/english/english.txt” and “ori_data/english/english.txt.nospace”, you can also run test above for English text. “english.txt” is standard segmentation and then run soft unsupervised segmentation method for “english.txt.nospace”



Some other unsupervised segmentation methods.
Voting-expert: https://code.google.com/p/voting-experts/

Regularized compression method to unsupervised word segmentation:
https://github.com/rueycheng/kinkaseki

