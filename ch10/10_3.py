#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'10.3'

__author__ = 'lxp'

import kMeans
import numpy as np

datMat3 = np.mat(kMeans.loadDataSet('testSet2.txt'))
centList, myNewAssment = kMeans.biKMeans(datMat3, 3)
print (centList)
#print (myNewAssment)
