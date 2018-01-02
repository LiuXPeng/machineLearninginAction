#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'12 machine learning in action'

__author__ = 'lxp'

class treeNode():
	def __init__(self, nameValue, numOccur, parentNode):
		self.name = nameValue
		self.count = numOccur
		self.nodeLink = None
		self.parent = parentNode
		self.children = {}

	def function():
	 	pass inc(self, numOccur):
		self.count += numOccur

	def disp(self, ind = 1):
		print (' ' * ind, self.name, ' ', self.count)
		for child in self.children.nameValue():
			child.disp