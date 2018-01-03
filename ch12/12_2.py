#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'12.2 machine learning in action'

__author__ = 'lxp'

import fpGrowth

simpDat = fpGrowth.loadSimpDat()
#print (simpDat)
initSet = fpGrowth.createInitSet(simpDat)
#print (initSet)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
myFPtree.disp()