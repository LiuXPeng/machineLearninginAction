#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'8.3 mechinelearing in action'

__author__ = 'lxp'

import regression
import numpy as np

abX, abY = regression.loadDataSet('abalone.txt')
yHat01 = regression.lwlrTest(abX[0 : 99], abX[0 : 99], abY[0 : 99], 0.1)
yHat1 = regression.lwlrTest(abX[0 : 99], abX[0 : 99], abY[0 : 99], 1)
yHat10 = regression.lwlrTest(abX[0 : 99], abX[0 : 99], abY[0 : 99], 10)
print (regression.rssError(abY[0 : 99], yHat01.T))
print (regression.rssError(abY[0 : 99], yHat1.T))
print (regression.rssError(abY[0 : 99], yHat10.T))

yHat01 = regression.lwlrTest(abX[100 : 199], abX[0 : 99], abY[0 : 99], 0.1)
yHat1 = regression.lwlrTest(abX[100 : 199], abX[0 : 99], abY[0 : 99], 1)
yHat10 = regression.lwlrTest(abX[100 : 199], abX[0 : 99], abY[0 : 99], 10)
print (regression.rssError(abY[100 : 199], yHat01.T))
print (regression.rssError(abY[100 : 199], yHat1.T))
print (regression.rssError(abY[100 : 199], yHat10.T))

ws = regression.standRegres(abX[0 : 99], abY[0 : 99])
yHat = np.mat(abX[100 :199]) * ws
print (regression.rssError(abY[100 : 199], yHat.T.A))
