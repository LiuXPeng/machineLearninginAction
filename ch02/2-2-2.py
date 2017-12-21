import kNN
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 20, 15.0*(array(datingLabels)+20))
#ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
