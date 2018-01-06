#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'13.3 machine learning in action'

__author__ = 'lxp'

import pca
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dataMat = pca.replaceNanWithMean()
lowDMat, reconMat = pca.pca(dataMat, 3)
meanVals = np.mean(dataMat, axis = 0)
meanRemoved = dataMat - meanVals
covMat = np.cov(meanRemoved, rowvar = 0)
eigVals, eigVects = np.linalg.eig(np.mat(covMat))
print (eigVals)