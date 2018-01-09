#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'6.4 machine learning in action'

__author__ = 'lxp'

import svmMLiA
import numpy as np

dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
b, alphas = svmMLiA.smoPNew(dataArr, labelArr, 0.6, 0.001, 40)
ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
datMat = np.mat(dataArr)
'''
i = input("要检验的数据编号\n")
print(datMat[0] * np.mat(ws) + b)
print(labelArr[0])
'''
count = 0
m = np.shape(dataArr)[0]
for i in range(m):
	if np.sign(datMat[i] * np.mat(ws) + b) != labelArr[i]:
		count += 1
print(count / m)