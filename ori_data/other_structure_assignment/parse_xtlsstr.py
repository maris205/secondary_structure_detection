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
    os.system("./xtlsstr "+fname + " > temp.txt")
    return base+".ln"

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()
    
    psea_file = run_stride(sys.argv[1])
    #print psea_file
    #step 1, parse to psea
    data_file = open(psea_file, "r")
    st_list = {}
    start = 0
    for line in data_file:
        line = line.strip()
        if start==0 and line[0:4]=="isub":
            start = 1  
            continue
        
        if start == 1:
            item = re.split("\s+", line)
            if len(item)<9:
                continue
            residue = item[2]
            chain = item[0]
            st = item[4].upper()
            if len(st)!=1:
                continue
            st_list.setdefault(chain,{})
            st_list[chain].setdefault("re", [])
            st_list[chain].setdefault("st", [])
            st_list[chain]["re"].append( residue )
            st_list[chain]["st"].append(st)
    #print st_list
    #get chain id
    filename = sys.argv[1]
    p = PDBParser()
    structure = p.get_structure("pdb", filename)
    for model in structure:
        i = 1
        for chain in model:
            if st_list.has_key(str(i)) and len(st_list[str(i)]["re"])>40:
                print ">" + (filename.split("/")[-1][3:7]).upper() + ":" +chain.get_id()
                print "".join(st_list[str(i)]["re"])
                print "".join(st_list[str(i)]["st"])
                print ""
            i = i + 1 

        break
