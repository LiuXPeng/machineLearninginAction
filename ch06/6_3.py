#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'6.3 machine learning in action'

__author__ = 'lxp'

import svmMLiA

dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
#print (labelArr)
b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print (b)
print (alphas[alphas > 0])