#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'11.4 machine learning in action'

__author__ = 'lxp'

import apriori

dataSet = apriori.loadDataSet()
L, supportData = apriori.apriori(dataSet, 0.5)
rules = apriori.generateRules(L, supportData, 0.7)
print (rules)
