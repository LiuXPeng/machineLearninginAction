#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'9.3 machine learning in action'

__author__ = 'lxp'

import regTrees
import numpy as np

myDat = regTrees.loadDataSet('ex00.txt')
myMat = np.mat(myDat)
print (regTrees.createTree(myMat))
