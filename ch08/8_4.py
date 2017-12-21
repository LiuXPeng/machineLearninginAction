#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'8.4 machine learning in action'

__author__ = 'lxp'

import regression
import numpy as np
import matplotlib.pyplot as plt

abX, abY = regression.loadDataSet('abalone.txt')
#print (abX)
ridgeWeights = regression.ridgeTest(abX, abY)
#print (ridgeWeights)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()
