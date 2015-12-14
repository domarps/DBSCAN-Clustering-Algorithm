#!/usr/bin/python
# Code to implement B-Cubed Evaluation
# Pramod Srinivasan (netid: psrnvsn2)
# Input files : ClusterOutputFile and GroundTruthFile
# Execution:
#	python bcubed.py <clusterOutputFile> <truthFile>
# Example Usage:
# 	python bcubed.py step1.txt truth_normalized.txt

clusterOutputLocation = "../psrnvsn2_assign5_results/"
truthOutputLocation = "../psrnvsn2_assign5_data/"

import time
import itertools
import math
from itertools import combinations
from random import randint
import collections
import inspect
import csv
import sys
import re
from scipy.spatial import distance


numClusters = 4
numPoints = 10005

def getData(clusteringOutputFile):
	clusterOutput = []
	for i in range(numPoints):
		clusterOutput.append([(0.0,0.0),0])
	parameters = []
	t = 0
	clusterCardinality = [0 for i in range(numClusters+1)]
	with open(clusteringOutputFile,'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			#row = re.spl it(r'\t+',row[0])
			if(len(row) == 1):
				parameters.append(float(row[0]))
			else:
				clusterOutput[t][0] = ((float(row[0])),(float(row[1])))
				clusterOutput[t][1] = (int(row[2]))
				clusterId = int(row[2])
				clusterCardinality[clusterId] = clusterCardinality[clusterId] + 1
				t = t + 1
	return {'clusterOutput':clusterOutput, 'cardinality': clusterCardinality, 'parameters':parameters}


def bCubed(clusteringOutputFile,groundTruthFile):
	start = time.time()
	data = getData(clusteringOutputFile)
	resultClusterOutput = data['clusterOutput']
	resultParameters  = data['parameters']
	resultClusterCardinality = data['cardinality']
	data = getData(groundTruthFile)
	truthClusterOutput = data['clusterOutput']
	truthParameters  = data['parameters']
	truthClusterCardinality = data['cardinality']
	precision = 0.0
	recall = 0.0
	N = len(resultClusterOutput)
	# for i in range(len(resultClusterCardinality)):
	# 	print resultClusterCardinality[i]
	for presult,ptruth in zip(resultClusterOutput,truthClusterOutput):
		precisionDenominator = resultClusterCardinality[presult[1]]
		recallDenominator = truthClusterCardinality[ptruth[1]]
		Numerator = 0
		for qresult, qtruth in zip(resultClusterOutput,truthClusterOutput):
			if(presult[1] == qresult[1] and ptruth[1] == qtruth[1]):
				Numerator = Numerator + 1
		if (ptruth[1] == 0 and presult[1] != 0):
			precision = precision + float(1)/(float(precisionDenominator))
			recall = recall + float(1)
		elif (ptruth[1] != 0 and presult[1] == 0):
			precision = precision + float(1)
			recall = recall + (float(1))/(float(recallDenominator))
		else:
			precision = precision + ((Numerator))/(float(precisionDenominator))
			recall = recall + ((Numerator))/(float(recallDenominator))
	end = time.time()
	precision = precision/numPoints
	recall = recall/numPoints
	f1_measure = 2 * (precision) * (recall) /(precision + recall)
	print "precision",precision
	print "recall",recall
	print "f1_measure",f1_measure

if __name__ == '__main__':
	if(len(sys.argv) == 3):
		clusterOutputFile = sys.argv[1]
		groundTruthFile = sys.argv[2]
		clusteringOutputFile = clusterOutputLocation + clusterOutputFile
		groundTruthFile = truthOutputLocation + groundTruthFile 
		result = bCubed(clusteringOutputFile,groundTruthFile)
	else:
		print "python bcubed.py step1.txt truth_normalized.txt"