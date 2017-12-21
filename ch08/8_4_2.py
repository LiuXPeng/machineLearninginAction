#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'second program 8.4 machine learing in action'

__author__ = 'lxp'

import regression
import numpy as np
import matplotlib.pyplot as plt

xArr, yArr = regression.loadDataSet('abalone.txt')
weights = regression.stageWise(xArr, yArr, 0.001, 5000)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(weights)
plt.show()
