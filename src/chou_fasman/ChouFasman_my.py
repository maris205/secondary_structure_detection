#!/usr/bin/env python
# File:
#   ChouFasman.py
# Summary:
#   An implementation of the Chou-Fasman algorithm
# Authors:
#   Samuel A. Rebelsky
#   YOUR NAME HERE

import string

# The Chou-Fasman table, with rows of the table indexed by amino acid name.
#   Data copied, pasted, and reformatted from 
#     http://prowl.rockefeller.edu/aainfo/chou.htm
# Columns are          SYM,P(a), P(b),P(turn), f(i),   f(i+1), f(i+2), f(i+3)

CF = {}
CF['Alanine']       = ['A', 142,   83,   66,   0.06,   0.076,  0.035,  0.058]
CF['Arginine']      = ['R',  98,   93,   95,   0.070,  0.106,  0.099,  0.085]
CF['Aspartic Acid'] = ['N', 101,   54,  146,   0.147,  0.110,  0.179,  0.081]
CF['Asparagine']    = ['D',  67,   89,  156,   0.161,  0.083,  0.191,  0.091]
CF['Cysteine']      = ['C',  70,  119,  119,   0.149,  0.050,  0.117,  0.128]
CF['Glutamic Acid'] = ['E', 151,   37,   74,   0.056,  0.060,  0.077,  0.064]
CF['Glutamine']     = ['Q', 111,  110,   98,   0.074,  0.098,  0.037,  0.098]
CF['Glycine']       = ['G',  57,   75,  156,   0.102,  0.085,  0.190,  0.152]
CF['Histidine']     = ['H', 100,   87,   95,   0.140,  0.047,  0.093,  0.054]
CF['Isoleucine']    = ['I', 108,  160,   47,   0.043,  0.034,  0.013,  0.056]
CF['Leucine']       = ['L', 121,  130,   59,   0.061,  0.025,  0.036,  0.070]
CF['Lysine']        = ['K', 114,   74,  101,   0.055,  0.115,  0.072,  0.095]
CF['Methionine']    = ['M', 145,  105,   60,   0.068,  0.082,  0.014,  0.055]
CF['Phenylalanine'] = ['F', 113,  138,   60,   0.059,  0.041,  0.065,  0.065]
CF['Proline']       = ['P',  57,   55,  152,   0.102,  0.301,  0.034,  0.068]
CF['Serine']        = ['S',  77,   75,  143,   0.120,  0.139,  0.125,  0.106]
CF['Threonine']     = ['T',  83,  119,   96,   0.086,  0.108,  0.065,  0.079]
CF['Tryptophan']    = ['W', 108,  137,   96,   0.077,  0.013,  0.064,  0.167]
CF['Tyrosine']      = ['Y',  69,  147,  114,   0.082,  0.065,  0.114,  0.125]
CF['Valine']        = ['V', 106,  170,   50,   0.062,  0.048,  0.028,  0.053]

aa_names = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic Acid',
            'Cysteine', 'Glutamic Acid', 'Glutamine', 'Glycine',
            'Histidine', 'Isoleucine', 'Leucine', 'Lysine',
            'Methionine', 'Phenylalanine', 'Proline', 'Serine',
            'Threonine', 'Tryptophan', 'Tyrosine', 'Valine']

Pa = { }
Pb = { }
Pturn = { }
F0 = { }
F1 = { }
F2 = { }
F3 = { }

# Convert the Chou-Fasman table above to more convenient formats
#    Note that for any amino acid, aa CF[aa][0] gives the abbreviation
#    of the amino acid.,给出各个缩写的几个值
for aa in aa_names:
    Pa[CF[aa][0]] = CF[aa][1]
    Pb[CF[aa][0]] = CF[aa][2]
    Pturn[CF[aa][0]] = CF[aa][3]
    F0[CF[aa][0]] = CF[aa][4]
    F1[CF[aa][0]] = CF[aa][5]
    F2[CF[aa][0]] = CF[aa][6]
    F3[CF[aa][0]] = CF[aa][7]

#遍历窗口，看是否有候选的螺旋结构
#1 相邻的6个残基中如果有至少4个残基倾向于形成α螺旋
# 即有4个残基对应的Pa>100 or 103
#2 然后进行扩展
#3 最后判断扩展后的片段是否是螺旋
def CF_find_alpha(seq):
    """Find all likely alpha helices in sequence.  Returns a list
       of [start,end] pairs for the alpha helices."""
    start = 0
    results = []
    # Try each window
    while (start + 6 < len(seq)):
        # Count the number of "good" amino acids (those likely to be
        # in an alpha helix).
        numgood = 0
        for i in range(start, start+6):
            if (Pa[seq[i]] > 100):
                numgood = numgood + 1
        if (numgood >= 4): #至少有4个倾向于a螺旋
            [estart,end] = CF_extend_alpha(seq, start, start+6)
            #print "Exploring potential alpha " + str(estart) + ":" + str(end)
            #判断是否是好的片段
            if (CF_good_alpha(seq[estart:end])):
                results.append([estart,end])
        # Go on to the next frame
        start = start + 1
    # That's it, we're done
    return results

#螺旋结构扩展
#向左或者向右扩展，直至四肽a片段Pα的平均值小于100为止
#也就是连续扩展的窗口值
def CF_extend_alpha(seq, start, end):
    """Extend a potential alpha helix sequence.  Return the endpoints
       of the extended sequence.
    """
    #向左边扩展,终止条件为start=0，或者 连续4个小于100
    #包含自身的6个残基
    while ( start>=0 and float(sum(Pa[x] for x in seq[start,start+4]))/4>100 ):
        start -= 1
    #向右边扩展，终止条件为end=len(seq) ,或者 连续4个小于100
    while ( end+1<=len(seq) and float(sum(Pa[x] for x in seq[end-3,end+1]))/4>100 ):
        start += 1
    # To be written
    return [start,end]

#找到的片段长度大于5，并且Pα的平均值大于Pβ的平均值，
#那么这个片段的二级结构就被预测为α螺旋
def CF_good_alpha(subseq):
    """Determine if a subsequence appears to be an alpha helix."""
    sum_Pa = 0
    for aa in subseq:
        sum_Pa = sum_Pa + Pa[aa]
    ave_Pa = sum_Pa/len(subseq)
    # Criteria need to be extended
    return (ave_Pa > 100)

def CF_find_beta(seq):
    """Find all likely beta strands in seq.  Returns a list
       of [start,end] pairs for the beta strands."""
    # To be written
    return []

def CF_find_turns(seq):
    """Find all likely beta turns in seq.  Returns a list of positions
       which are likely to be turns."""
    # To be written
    return []

def region_overlap(region_a, region_b):
    """Given two regions, represented as two-element lists, determine
       if the two regions overlap.
    """
    return (region_a[0] <= region_b[0] <= region_a[1]) or \
           (region_b[0] <= region_a[0] <= region_b[1])
          
def region_merge(region_a, region_b):
    """Given two regions, represented as two-element lists, return
       the minimum region that contains both regions.
    """
    return [min(region_a[0], region_b[0]), max(region_a[1], region_b[1])]

def region_intersect(region_a, region_b):
    """Given two regions, represented as two-element lists, return
       the intersection of the two regions.
    """
    return [max(region_a[0], region_b[0]), min(region_a[1], region_b[1])]

def ChouFasman(seq):
    """Analyze seq using the Chou-Fasman algorithm and display
       the results.  H represents 'alpha helix'.  E represents 
       'beta strand'.  T represents "turn".  Space represents
       'none of the above'.  
    """

    # Find probable locations of alpha helices, beta strands,
    # and beta turns.
    alphas = CF_find_alpha(seq)
    # print "Alphas = " + str(alphas)
    betas = CF_find_beta(seq)
    # print "Betas = " + str(betas)
    turns = CF_find_turns(seq)
    # print "Turns = " + str(turns)

    # Handle overlapping regions
    # To be written

    # Build a sequence of spaces of the same length as seq. 
    analysis = [' ' for i in xrange(len(seq))]

    # Fill in the predicted alpha helices
    for alpha in alphas:
        for i in xrange(alpha[0], alpha[1]):
            analysis[i] = 'H'
    # Fill in the predicted beta strands 
    for beta in betas:
        for i in xrange(beta[0], beta[1]):
            analysis[i] = 'E'
    # Fill in the predicted beta turns
    for turn in turns:
        analysis[turn] = 'T'

    # Turn the analysis and the sequence into strings for ease
    # of printing
    astr = string.join(analysis, '')
    sstr = string.join(seq, '')

    # Print out 60 characters lines
    start = 0
    end = 60
    while (start < len(seq)):
        print astr[start:end]
        print sstr[start:end]
        print str(start + 10).rjust(10) + \
              str(start + 20).rjust(10) + \
              str(start + 30).rjust(10) + \
              str(start + 40).rjust(10) + \
              str(start + 50).rjust(10) + \
              str(start + 60).rjust(10) 
        print ""
        start = start + 60
        end = end + 60
