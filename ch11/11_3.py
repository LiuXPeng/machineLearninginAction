#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'11.3 machine learning in action'

__author__ = 'lxp'

import apriori

dataSet = apriori.loadDataSet()
L, supportData = apriori.apriori(dataSet)
print (L)
