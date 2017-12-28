#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'9.5 machine learning in action'

__author__ = 'lxp'

import regTrees
import numpy as np

myMat2 = np.mat(regTrees.loadDataSet('exp2.txt'))
print (regTrees.createTree(myMat2, regTrees.modelLeaf, regTrees.modelErr, (1, 10)))
