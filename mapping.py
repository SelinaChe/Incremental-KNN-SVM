import os, sys

def file2np(file_name,):
    xList = []
    yList =[]
    read_file = open(file_name, 'r')
    for line in read_file.read().split('\n'):
        if line != '':
            yList.append(float(line.split(' ')[0]))
    return yList

test_file = 'test_data.txt'
test_yfile = 'test_data_ylist.txt'
ylist = file2np(test_file)

test_y = open(test_yfile, 'w')
for y in ylist:
	test_y.write(str(y)+'\n')



