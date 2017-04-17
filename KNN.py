__author__ = 'chelsea'
# -*- coding: utf-8 -*-

import os,sys
import numpy as np
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import datetime
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import datetime

def file2np(file_name):
    xList = []
    yList =[]
    read_file = open(file_name, 'r')
    for line in read_file.read().split('\n'):
        if line != '':
            yList.append(float(line.split(' ')[0]))
            xList.append([float(tk.split(':')[1]) for tk in line.split(' ')[1:]])
    xnp = np.array(xList)
    ynp = np.array(yList)
    return xnp, ynp

def knn_train(x_train, y_train, x_test, y_test, numk):
	h = .01
	time1 = datetime.datetime.now()
	#14 is the best
	clf = neighbors.KNeighborsClassifier(n_neighbors=numk, algorithm='auto')
	clf.fit(x_train, y_train)
	time2 = datetime.datetime.now()
	print time2 
	print time2-time1

	answer = clf.predict(x_test)
	#print(x)
	print("answer: ")
	n=0
	for i in range(len(answer)):
		if answer[i] == y_test[i]:
			n = n + 1
	print("ACC:")
	print float(n)/len(answer)
	#print(np.mean( answer == y_test))
	print time2
	print time2-time1

def incre(x_train, y_train, x_test, y_test, x_incre, y_incre, numk):
	X = np.concatenate((x_train, x_incre))
	y = np.concatenate((y_train, y_incre))
	print "***********incre**********"
	time1 = datetime.datetime.now()
	knn_train(X, y, x_test, y_test, numk)
	time2 = datetime.datetime.now()
	print time2-time1 
	print "**************************"

def training():
	#train_file = 'data/train_data.txt'
	#test_file = 'data/test_data.txt' 
	train_file = sys.argv[1]
	test_file = sys.argv[2] 
	incre_file = sys.argv[3]
	numk = int(sys.argv[4])
	print(train_file)
	print(test_file)

	X_train, y_train = file2np(train_file)
	X_test, y_test = file2np(test_file)
	X_incre, y_incre = file2np(incre_file)
	
	print "***********raw**********"
	time1 = datetime.datetime.now()
	knn_train(X_train, y_train, X_test, y_test, numk)
	time2 = datetime.datetime.now()
	print time2-time1 
	print "************************"

	incre(X_train, y_train, X_test, y_test, X_incre, y_incre, numk)
	print("********************\n\n")

	
	

if __name__ == '__main__':
	training()


