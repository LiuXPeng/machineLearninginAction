#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'7_7 ROC'

__author__ = 'lxp'

import adaboost

datArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray, aggClassEst = adaboost.adaBoostTrainDSNew(datArr, labelArr, 10)
adaboost.plotROC(aggClassEst.T, labelArr)
