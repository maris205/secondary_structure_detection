#!/usr/bin/env python
import sys
all_sum = {}
one_sum = {}
for line in sys.stdin:
    line = line.strip()
    word = line.split("\t")[0]
    freq = int(line.split("\t")[1])
    length = len(word)
    all_sum.setdefault(length,0)
    all_sum[length] += 1
    if freq == 1:
        one_sum.setdefault(length,0)
        one_sum[length] +=1

for length in range(1,len(all_sum) + 1):
    if one_sum.has_key(length):
        print length,float(one_sum[length])/all_sum[length]
    else:
        print length,0

