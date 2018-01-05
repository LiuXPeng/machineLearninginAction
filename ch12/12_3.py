#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'12.3 machine learning in action'

__author__ = 'lxp'

import fpGrowth

simpDat = fpGrowth.loadSimpDat()
#print (simpDat)
initSet = fpGrowth.createInitSet(simpDat)
#print (initSet)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)

#print (fpGrowth.findPrefixPath('x', myHeaderTab['x'][1]))
freqItems = []
fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
