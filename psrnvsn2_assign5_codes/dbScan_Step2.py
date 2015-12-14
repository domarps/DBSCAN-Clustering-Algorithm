#!/usr/bin/python
# Code to implement the dBscan Algorithm
# Pramod Srinivasan (netid: psrnvsn2)
# Input files : Dataset File, Output File, minPts and eps
# Output file is generated in the "../psrnvsn2_assign3_results/"
# Execution:
#	python dbscan_Step2.py
import time
import itertools
import math
from itertools import combinations
from random import randint
import collections
import inspect
import csv
import re
from scipy.spatial import distance
#import sys
#import os
#import math

def getData(dfile):
	Data = []
	with open(dfile,'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			#row = re.spl it(r'\t+',row[0])
			if(len(row) == 1):
				nDataPoints = int(row[0])
			else:
				Data.append([float(row[0]),float(row[1])])
	return {'nDataPoints':nDataPoints, 'Points':Data}

def calculateDistance(point1,point2):
	a = (point1[0] - point2[0])
	b = (point1[1] - point2[1])
	return a ** 2 + b ** 2

def getEpsNeighbours(points,eps):
	neighBourList = []
	N = len(points)
	for i in range(N):
		neighBourList.append([])
	for i,p in enumerate(points):
		# if i%100 == 0:
		# 	print 'index',i
		for j,q in enumerate(points):
			if(calculateDistance(p,q) <= eps ** 2):
				neighBourList[i].append(j)
	return {'neighBourList' : neighBourList}



def dBScan(dfile,resultFile,eps,minPoints):
	start = time.time()
	data = getData(dfile)
	#nDataPoints <- data['nDataPoints'] , Points <- data['Points']
	nDataPoints = data['nDataPoints']
	points = data['Points']
	N = len(points)
	nList = getEpsNeighbours(points,eps)
	print 'Generated the epsilon-neighborhood of points'
	neighBourList = nList['neighBourList']
	# print len(neighBourList)
	# for i in range(N):
	# 	print len(neighBourList[i])
	# NeighbourList is a list of lists, where each list[i] is the number of neighbours corresponding to i^th datapoint
	unvisited = []
	cluster = []
	visited = []
	for i in range(N):
		unvisited.append(i)
		cluster.append(-1)
		visited.append(False)
	clusterID = 0
	# print 'unvisited',unvisited
	# print 'cluster',cluster
	# print 'visited',visited
	while(len(unvisited) != 0):
		# print 'remaining',len(unvisited)
		pIndex = randint(0,len(unvisited)-1)
		# print 'unvisited object', pIndex
		node = unvisited[pIndex]
		# print 'node', node
		visited[node] = True
		# print visited
		unvisited.remove(node)
		# print 'unvisited',unvisited
		# print '----------------------------'
		# print 'number of neighbours', len(neighBourList[node])
		if len(neighBourList[node]) >= minPoints:
			clusterID = clusterID + 1
			cluster[node] = clusterID
			nodeNeighbours = []
			#nodeNeighbours is the neighbours of pIndex'th datapoint
			for i,p in enumerate(neighBourList[node]):
				nodeNeighbours.append(p)
			while(len(nodeNeighbours) != 0):
				if(visited[nodeNeighbours[0]] == False):
					# print nodeNeighbours[0]
					visited[nodeNeighbours[0]] = True
					unvisited.remove(nodeNeighbours[0])
					if(len(neighBourList[nodeNeighbours[0]]) >= minPoints):
						for j,q in enumerate(neighBourList[nodeNeighbours[0]]):
							nodeNeighbours.append(q)
				if(cluster[nodeNeighbours[0]] == -1):
					cluster[nodeNeighbours[0]] = clusterID
				nodeNeighbours.remove(nodeNeighbours[0])
		else:
			cluster[node] = 0 #mark the node as noise
	f = open(resultFile, 'w')
	f.write(str(minPoints) + '\n')
	f.write(str(eps) + '\n')
	f.write(str(clusterID) + '\n')
	for i in range(nDataPoints):
		line = str(points[i][0]) + ',' + str(points[i][1]) + ',' + str(cluster[i]) + '\n'
		f.write(line)
	end = time.time()
	print 'Time taken to run DBSCAN is :', end - start ,'seconds'

resultFile1 = '../psrnvsn2_assign5_results/step2a.txt'
resultFile2 = '../psrnvsn2_assign5_results/step2b.txt'
dfile  = '../psrnvsn2_assign5_data/data_normalized.txt'
eps1 = 0.075
eps2 = 0.05
minPoints = 25
result =  dBScan(dfile,resultFile1,eps1,minPoints)
result =  dBScan(dfile,resultFile2,eps2,minPoints)

