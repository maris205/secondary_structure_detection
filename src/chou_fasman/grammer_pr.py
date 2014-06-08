#!/usr/bin/env python
#coding=utf-8
import sys
import ChouFasman
#根据语法判断一个序列是否是一个词

if __name__=="__main__":
    for line in sys.stdin:
        line = line.strip()
        print ChouFasman.ChouFasman(line)
