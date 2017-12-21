#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'program of chapt 3'

__author__ = 'lxp'

import trees

myDat, labels = trees.createDataSet()
print(myDat)
print(trees.splitDataSet(myDat, 0, 1))

