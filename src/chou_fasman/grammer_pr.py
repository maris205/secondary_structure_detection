#!/usr/bin/env python
#coding=utf-8
import sys
import ChouFasman
#�����﷨�ж�һ�������Ƿ���һ����

if __name__=="__main__":
    for line in sys.stdin:
        line = line.strip()
        print ChouFasman.ChouFasman(line)
