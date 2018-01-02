#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'11.6 machine learning in action'

__author__ = 'lxp'

import apriori

mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
L, suppData = apriori.apriori(mushDatSet, 0.3)
for i in range(len(L)):
	for item in L[i]:
		if item.intersection('2'):
			print (item)