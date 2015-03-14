#!/usr/bin/env python
#coding=utf-8
import sys 
import os
import re
import xml.dom.minidom
reload(sys)
sys.setdefaultencoding('utf-8')
def run_kaksi(fname):
    last=fname.split("/")[-1]
    base=last.split(".")[0]
    os.system("./kaksi -pf "+fname + "> " + base + ".kaksi")
    return base+".kaksi"

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "please input file name"
        sys.exit()
    
    kaksi_file = run_kaksi(sys.argv[1])
    #step 1, parse kaksi
    data_file = open(kaksi_file, "r")
    xml_data = data_file.read()
    result = xml.dom.minidom.parseString(xml_data)
    for chain in result.getElementsByTagName("chain"):
        chain_id = chain.getElementsByTagName("name")[0].firstChild.nodeValue
        st_list = []
        res_list = []
        for res in chain.getElementsByTagName("sequence")[0].getElementsByTagName("res"):
            try:
                st_list.append(res.getElementsByTagName("kaksi_sse")[0].firstChild.nodeValue)
                res_list.append(res.getElementsByTagName("aa1")[0].firstChild.nodeValue)
            except:
                continue
        print ">" + (sys.argv[1].split("/")[-1][3:7]).upper() + ":" +chain_id
        print "".join(res_list)
        print "".join(st_list)
        print ""
