#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'12.5 machine learning in action'

__author__ = 'lxp'

import fpGrowth

parsedDat = [line.split() for line in open('kosarak.dat').readlines()]
initSet = fpGrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 100000)
freqItems = []
fpGrowth.mineTree(myFPtree, myHeaderTab, 100000, set([]), freqItems)
print (len(freqItems))
print (freqItems)