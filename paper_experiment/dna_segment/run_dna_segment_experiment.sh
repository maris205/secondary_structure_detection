#!/bin/sh
#########################################################################
# Author: wangliang.f@gmail.com
# Created Time: Fri 13 Mar 2015 07:51:22 PM CST
# File Name: run_dna_segment_experiment.sh
# Description: segment dna sequence by protein word vocabulary
#########################################################################

#step 1, get DNA vocabulary from protein vocabulary
#please check file "ss_06.dat.structure_dict_length9" exist
./build_dna_dict.py ss_06.dat.structure_dict_length9 > dna.dict

#step 2, segment the DNA sequence test file, it's part of human genome
./viterbi_segment.py dna.dict test.dna > test.dna.seg

#step 3, caculate the protein word coverage rate of each dna sequence
./get_protein_coverge_rage.py test.dna.seg > test.dna.seg.coverage
