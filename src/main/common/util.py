# list of feature vectors for machine learning algorithm to compute on

from math import pow
import random

def mean(alist):
	return sum(alist)/(len(alist)*1.0)

def std(alist):
	avg = mean(alist)
	diff = [pow(num - avg, 2) for num in alist]
	return pow((1.0/(len(alist)))*sum(diff), 0.5)

def mad(alist):
	avg = mean(alist)
	diff = [abs(num - avg)*1.0 for num in alist]
	return sum(diff)/len(alist)

def skewness(alist):
	try:
		return 3*(mean(alist)-median(alist))/std(alist)
	except ZeroDivisionError:
		return 0


def kurtosis(alist):
	avg = mean(alist)
	stand_dev = std(alist)
	diff = [pow((num - avg)/stand_dev,4)*1.0 for num in alist]
	return (sum(diff)/len(alist))-3

def power(current, voltage):
	return current * voltage

def median(alist):
	alist.sort()
	return alist[len(alist)/2+1] if len(alist) % 2 != 0 else (alist[len(alist)/2]+alist[len(alist)/2+1])/2.0 

