# list of feature vectors for machine learning algorithm to compute on

from math import pow
import random

def mean(alist):
	return sum(alist)/(len(alist)*1.0)

def std(alist):
	avg = mean(alist)
	diff = [math.pow(num - avg, 2) for num in alist]
	return math.pow((1.0/(len(alist)))*sum(diff), 0.5)

def mad(alist):
	avg = mean(alist)
	diff = [abs(num - avg)*1.0 for num in alist]
	return sum(diff)/len(alist)

def skewness(alist):
	avg = mean(alist)
	stand_dev = std(alist)
	diff = [math.pow((num - avg)/stand_dev,3)*1.0 for num in alist]
	return sum(diff)/len(alist)

def kurtosis(alist):
	avg = mean(alist)
	stand_dev = std(alist)
	diff = [math.pow((num - avg)/stand_dev,4)*1.0 for num in alist]
	return (sum(diff)/len(alist))-3
