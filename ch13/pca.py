#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ch13 machine learning in action'

__author__ = 'lxp'

import numpy as np

def loadDataSet(fileName, delim = '\t'):
	fr = open(fileName)
	stringArr = [line.strip().split(delim) for line in fr.readlines()]
	datArr = [list(map(float, line)) for line in stringArr]
	return np.mat(datArr)

def pca(dataMat, topNfeat = 9999999):
	meanVals = np.mean(dataMat, axis = 0)
	meanRemoved = dataMat - meanVals
	covMat = np.cov(meanRemoved, rowvar = 0)
	eigVals, eigVects = np.linalg.eig(np.mat(covMat))
	eigValInd = np.argsort(eigVals)
	eigValInd = eigValInd[: -(topNfeat) : -1]
	redEigVects = eigVects[:, eigValInd]
	lowDDataMat = meanRemoved * redEigVects
	reconMat = (lowDDataMat * redEigVects.T) + meanVals
	return lowDDataMat, reconMat