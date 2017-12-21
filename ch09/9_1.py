#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ch09 machine learning in action'

__author__ = 'lxp'

import regTrees
import numpy as np

testMat = np.mat(eye(4))
mat0, mat1 = regTrees.binSplitDataSet(testMat, 1, 0.5)
print (mat0)
print (mat1)
