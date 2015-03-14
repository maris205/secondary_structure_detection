#!/usr/bin/env python
#coding=utf-8
from Bio.PDB import *
import sys 
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')
def run_stride(fname):
    last=fname.split("/")[-1]
    base=last.split(".")[0]
    os.system("./stride "+fname + "> " + base + ".stride")
    return base+".stride"

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()
    
    psea_file = run_stride(sys.argv[1])
    #print psea_file
    #step 1, parse to psea
    data_file = open(psea_file, "r")
    st_list = {}
    for line in data_file:
        line = line.strip()
        if line[0:3]=="ASG":
            item = re.split("\s+", line)
            residue = item[1]
            chain = item[2]
            st = item[5]
            st_list.setdefault(chain,{})
            st_list[chain].setdefault("re", [])
            st_list[chain].setdefault("st", [])
            st_list[chain]["re"].append( Polypeptide.three_to_one(residue) )
            st_list[chain]["st"].append(st)
    #get chain id
    filename = sys.argv[1]
    p = PDBParser()
    structure = p.get_structure("pdb", filename)
    for model in structure:
        for chain in model:
            if len(st_list[chain.get_id()]["re"])>0:
                print ">" + (filename.split("/")[-1][3:7]).upper() + ":" +chain.get_id()
                print "".join(st_list[chain.get_id()]["re"])
                print "".join(st_list[chain.get_id()]["st"])
                print ""
        break
            
