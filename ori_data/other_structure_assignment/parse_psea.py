#!/usr/bin/env python
#coding=utf-8
from Bio.PDB import *
import sys 
import os
reload(sys)
sys.setdefaultencoding('utf-8')
def run_psea(fname):
    """Run PSEA and return output filename.

    Note that this assumes the P-SEA binary is called "psea" and that it is
    on the path.

    Note that P-SEA will write an output file in the current directory using
    the input filename with extension ".sea".

    Note that P-SEA will write output to the terminal while run.
    """
    os.system("psea "+fname + ">temp.dat &2>1")
    last=fname.split("/")[-1]
    base=last.split(".")[0]
    return base+".sea"

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()
    
    psea_file = run_psea(sys.argv[1])
    #print psea_file
    #step 1, parse to psea
    data_file = open(psea_file, "r")
    seg_list = []
    seg = ""
    for line in data_file:
        line = line.strip()
        if len(line)==0 or line[0] == ">" or line[0]=="+":
            if seg!="":
                seg_list.append(seg)
            seg = ""
        else:
            seg = seg + line

    #get chain id
    filename = sys.argv[1]
    p = PDBParser()
    structure = p.get_structure("pdb", filename)
    chain_id_list = []
    for model in structure:
        for chain in model:
            chain_id_list.append(">" + (filename.split("/")[-1][3:7]).upper() + ":" +chain.get_id())
        break
    
    #output
    for i in range(0,len(seg_list)/2):
        print chain_id_list[i]
        print seg_list[i]
        print seg_list[len(seg_list)/2+i]
        print ""

