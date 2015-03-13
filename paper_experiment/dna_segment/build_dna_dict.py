#!/usr/bin/env python
#coding=utf-8
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import Translate
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def protein_to_dna(seq):
    standard_translator = Translate.unambiguous_dna_by_id[1]    
    my_protein = Seq(seq, IUPAC.protein)
    dna = standard_translator.back_translate(my_protein)
    return str(dna)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print "please input data filename"
        sys.exit()

    filename = sys.argv[1]
    data_file = open(filename,'r')
    for line in data_file:
        line = line.strip()
        protein_seq = line.split("\t")[0]
        value = line.split("\t")[1]
        try:
            dna_seq = protein_to_dna(protein_seq)
            print dna_seq + "\t" + value
        except:
            continue

    #print 4 dna letter
    print "A\t1"
    print "T\t1"
    print "C\t1"
    print "G\t1"

