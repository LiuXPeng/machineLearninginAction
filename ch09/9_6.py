#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'9.6 machine learning in action'

__author__ = 'lxp'

import regTrees
import numpy as np

trainMat = np.mat(regTrees.loaddataSet('bikeSpeedVsIq_train.txt'))
testMat = np.mat(regTrees.loaddataSet('bikeSpeedVsIq_test.txt'))
myTree = regTrees.createTree(trainMat, ops = (1, 20))
yHat = regTrees.createForeCast(myTree, testMat[:, 0])
res = np.corrcoef(yHat, testMat[:, 1], rowvar = 0)[0, 1]
print (res)

ws, X, Y = regTrees.linearSolve(trainMat)
print (ws)

for i in range(np.shape(testMat)[0]):
	yHat[i] = testMat[i, 0] * ws [0, 0]

res = np.corrcoef(yHat, testMat[:, 1], rowvar = 0)[0, 1]
print (res)
