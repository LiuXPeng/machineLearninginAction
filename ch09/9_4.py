#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'9.4 machine learning in action'

__author__ = 'lxp'

import regTrees
import numpy as np

myDat2 = regTrees.loadDataSet('ex2.txt')
myMat2 = np.mat(myDat2)
myTree = regTrees.createTree(myMat2, ops = (0, 1))
myDatTest = regTrees.loadDataSet('ex2test.txt')
myMat2Test = np.mat(myDatTest)
print (regTrees.prune(myTree, myMat2Test))
