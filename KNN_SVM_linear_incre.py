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
	print('begin')
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

def nnsvm_train(x_train, y_train, x_test, y_test, numk, rfile):
	h = .01
	#14 is the best
	neigh = neighbors.NearestNeighbors(n_neighbors=numk)
	neigh.fit(x_train) 
	#print(x)
	all_label = []
	index = 0
	right=0
	test_result = open(rfile, 'w')
	for one_test in x_test:
		
		result = neigh.kneighbors(one_test)
		label_index = result[1]
		label = []
		train = []
		#array_label = label_index.copy()
		for i in label_index:
			c = 0
			for j in i:
				one_label = y_train[j]
				one_train = x_train[j]
				label.append(one_label)
				train.append(one_train)
				#array_label[0][c]=one_label
				c=c+1
		if len(set(label))==1:
			test_result.write(str(label[0])+'\n')
			if label[0]==y_test[index]:
				right=right+1
		
		else:
			np_label = np.array(label)
			np_train = np.array(train)

			clf = LinearSVC()
			#clf.decision_function_shape='ovr'
			#print (np_train.shape, np_label.shape)
			#print (result[0], array_label)
			clf.fit(np_train, np_label)
			test_result.write(str(clf.predict(one_test)[0])+'\n')
			if y_test[index] == clf.predict(one_test)[0]:
				right = right+1
				
		index = index + 1
		#print right
	print float(right)/float(len(y_test))

	#print result

def incre(x_train, y_train, x_test, y_test, x_incre, y_incre, numk, rfile):
	X = np.concatenate((x_train, x_incre))
	y = np.concatenate((y_train, y_incre))
	print "***********incre**********"
	time1 = datetime.datetime.now()
	nnsvm_train(X, y, x_test, y_test, numk, rfile)
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
	'''
	print "***********raw**********"
	time1 = datetime.datetime.now()
	rfile='result/'+str(numk)+'_'+train_file+"_result"
	nnsvm_train(X_train, y_train, X_test, y_test, numk, rfile)
	time2 = datetime.datetime.now()
	print time2-time1 
	print "************************"
	'''
	rfile='result/'+str(numk)+'_'+incre_file+"_result"
	incre(X_train, y_train, X_test, y_test, X_incre, y_incre, numk, rfile)
	print("********************\n\n")

	
	

if __name__ == '__main__':
	training()


