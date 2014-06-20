#/bin/sh
#run experiment in paper

set -x
#segment the protein sequence according to its secondary structure, get gold-standard segmentation
./structure_segment.py ss_06.dat > ss_06.dat.stru_seg  

#apply HDP segment method to segment the protein sequence, get the precision, recall,f-score
nohup ./segment ss_06.dat.stru_seg  > ss_06.dat.stru_seg.score &


###################################################################
#run experiment, set maximal word length
#get secondary structure word list
./get_stu_word_dict.py ss_06.dat > ss_06.dat.dict

#segment long secondary structure segmentation into short one, by setting maximal word length
./segment_long_structure_word.py ss_06.dat.dict ss_06.dat 6 > ss_06.dat.seg6
nohup ./segment ss_06.dat.seg6  > ss_06.dat.seg6.score &
