#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'8.2'

__author__ = 'lxp'

import regression
import numpy as np
import matplotlib.pyplot as plt

xArr, yArr = regression.loadDataSet('ex0.txt')
print (regression.lwlr(xArr[0], xArr, yArr, 1))
print (regression.lwlr(xArr[0], xArr, yArr, 0.001))
yHat = regression.lwlrTest(xArr, xArr, yArr, 0.003)
xMat = np.mat(xArr)
srtInd = xMat[:, 1].argsort(0)
xSort = xMat[srtInd][:, 0, :]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:, 1], yHat[srtInd])
ax.scatter(xMat[:, 1].flatten().A[0], np.mat(yArr).T.flatten().A[0], s = 2, c = 'red')
plt.show()


