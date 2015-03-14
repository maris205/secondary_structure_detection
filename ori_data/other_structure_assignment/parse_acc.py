#!/usr/bin/env python
#coding=utf-8
from Bio.PDB import *
import math
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()

    filename = sys.argv[1]
    p = PDBParser()
    structure = p.get_structure("pdb", filename)
    for model in structure:
        dssp = DSSP(model, filename)
        for chain in model:
            chain_id = chain.get_id()
            acc = []
            seq = []
            for residue in chain:
                residue_id = residue.get_id()
                try:
                    relative_acc = dssp[(chain_id, residue_id)][3]
                    if "NA" != relative_acc :
                        acc.append(str( round(relative_acc,2) ))
                    else:
                        acc.append("-1")
                    seq.append(Polypeptide.three_to_one( residue.get_resname() ))
                except:
                    #print residue
                    break
            print ">" + (filename.split("/")[-1][3:7]).upper() + ":" +chain.get_id()
            print " ".join(seq)
            print " ".join(acc)
            print ""
        break # onlyget one model
    
    
    #model = structure[0]
    #print vars(model)
    
    """
    #获得序列
    ppb=PPBuilder()
    seq = ""
    for chain in ppb.build_peptides(model):
        seq = seq + chain.get_sequence()
    
    print " ".join(seq)
    #print len(seq) 
    """
    """
    #get relative solvent accessibility
    dssp = DSSP(model, filename)
    acc = []
    seq = []
    for item in list(dssp):
        if "NA" != item[3] :
            acc.append( str( round(item[3],2) ) )
        else:
            acc.append( "-1" )
        seq.append( Polypeptide.three_to_one(item[0].get_resname()) )
    print ">" + filename[3:7]
    print " ".join(seq)
    print " ".join(acc)
    #print len(seq)
    #print len(acc)
    print ""
    """
