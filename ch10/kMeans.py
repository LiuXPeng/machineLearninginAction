#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ch10 machine learning in action'

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

def distEclud(vecA, vecB):
	return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet, k):
	n = np.shape(dataSet)[1]
	centroids = np.mat(np.zeros((k, n)))
	for j in range(n):
		minJ = np.min(dataSet[:, j])
		rangeJ = float(np.max(dataSet[:, j]) - minJ)
		centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)
	return centroids

def kMeans(dataSet, k, distMeas = distEclud, createCent = randCent):
	m = np.shape(dataSet)[0]
	clusterAssment = np.mat(np.zeros((m, 2)))
	centroids = createCent(dataSet, k)
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(m):
			minDist = np.inf
			minIndex = -1
			for j in range(k):
				distJI = distMeas(centroids[j, :], dataSet[i, :])
				if distJI < minDist:
					minDist = distJI
					minIndex = j
			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist ** 2
		print (centroids)
		for cent in range(k):
			ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]
			centroids[cent, :] = np.mean(ptsInClust, axis = 0)
	return centroids, clusterAssment



  						
