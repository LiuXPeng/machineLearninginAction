#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ch08 machine learning in action'

__author__ = 'lxp'

import numpy as np

def loadDataSet(fileName):
	dataMat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = list(map(float, curLine))
		dataMat.append(fltLine)
	return dataMat

def binSplitDataSet(dataSet, feature, value):
	mat0 = dataSet[np.nonzero(dataSet[:, feature] > value)[0], :]
	mat1 = dataSet[np.nonzero(dataSet[:, feature] <= value)[0], :]
	return mat0, mat1

def regLeaf(dataSet):
	return np.mean(dataSet[:, -1])

def regErr(dataSet):
	return np.var(dataSet[:, -1]) * np.shape(dataSet)[0]

def createTree(dataSet, leafType = regLeaf, errType = regErr, ops = (1, 4)):
	feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
	if feat == None: 
		return val
	retTree = {}
	retTree['spInd'] = feat
	retTree['spVal'] = val
	lSet, rSet = binSplitDataSet(dataSet, feat, val)
	retTree['left'] = createTree(lSet, leafType, errType, ops)
	retTree['right'] = createTree(rSet, leafType, errType, ops)
	return retTree

def chooseBestSplit(dataSet, leafType = regLeaf, errType = regErr, ops = (1, 4)):
	tolS = ops[0]
	tolN = ops[1]
	if len(set(dataSet[:, -1].T.tolist()[0])) == 1:
		return None, leafType(dataSet)
	m, n = np.shape(dataSet)
	S = errType(dataSet)
	bestS = np.inf
	bestIndex = 0
	bestValue = 0
	for featIndex in range(n - 1):
		for splitVal in set((dataSet[:, featIndex].T.A.tolist())[0]):
			mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
			if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
				continue
			newS = errType(mat0) + errType(mat1)
			if newS < bestS:
				bestIndex = featIndex
				bestValue = splitVal
				bestS = newS
	if (S - bestS) < tols:
		return None, leafType(dataSet)
	mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
	if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
		return None, leafType(dataSet)
	return bestIndex, bestValue
