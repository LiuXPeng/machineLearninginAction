#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'13.2 machine learning in action'

__author__ = 'lxp'

import pca
import matplotlib
import matplotlib.pyplot as plt

dataMat = pca.loadDataSet('testSet.txt')
lowDMat, reconMat = pca.pca(dataMat, 3)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker = '^', s = 90, c = 'blue')
ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker = 'o', s = 50, c = 'red')
plt.show()