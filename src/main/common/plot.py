import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from util import *
from csv_helper import *


filename = 'geid1_l'
arr = csv_reader('../../../data/' + filename + '1.csv')
arr2 = csv_reader('../../../data/' + filename + '2.csv')
arr3 = csv_reader('../../../data/' + filename + '3.csv')


# cleaning
clean_arr1 = arr[600:900]
sample1 = list(chunks(clean_arr1, 100))

clean_arr2 = arr2[600:900]
sample2 = list(chunks(clean_arr2, 100))

clean_arr3 = arr3[600:900]
sample3 = list(chunks(clean_arr3, 100))

mu = []
sigma = []

for item in sample1:
	mu.append(mean(item))
	sigma.append(std(item))

for item in sample2:
	mu.append(mean(item))
	sigma.append(std(item))

for item in sample3:
	mu.append(mean(item))
	sigma.append(std(item))

for i in xrange(len(mu)):
	x = np.linspace(mu[i] - 3*sigma[i], mu[i] + 3*sigma[i], 100)
	plt.plot(x,mlab.normpdf(x, mu[i], sigma[i]))
plt.show()
