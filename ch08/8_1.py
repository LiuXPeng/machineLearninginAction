#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'8.1'

__author__ = 'lxp'

import regression
import numpy as np
import matplotlib.pyplot as plt

xArr, yArr = regression.loadDataSet('ex0.txt')
print("xArr: ", xArr)
ws = regression.standRegres(xArr, yArr)
print("ws: ", ws)
xMat = np.mat(xArr)
yMat = np.mat(yArr)
yHat = xMat * ws
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:, 1].flatter().A[0], yMat.T[:, 0].flatten().A[0])
