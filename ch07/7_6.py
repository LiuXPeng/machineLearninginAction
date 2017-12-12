#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'7.6'

__author__ = 'lxp'

import adaboost
import numpy as np

datArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray = adaboost.adaBoostTrainDS(datArr, labelArr, 10)
testArr, testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
prediction10 = adaboost.adaClassify(testArr, classifierArray)
errArr = np.mat(np.ones((67, 1)))
print(errArr[prediction10 != np.mat(testLabelArr).T].sum())
