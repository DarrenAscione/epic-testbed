from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from util import *
from csv_helper import *

filename = 'tied4_v'
lines = 2
collector = []
size = 12

for i in xrange(1,lines+1):
	arr = csv_reader('../../../data/' + filename + str(i+1) +'.csv')
	collector.append(list(chunks(arr, size)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.title.set_text('TIED4 Current Analysis')

color = ["#f1c40f", "#27ae60", "#2c3e50"]
#color = []

for i in xrange(lines):
	mu = []
	sigma = []
	skw = []

	for item in collector[i]:
		mu.append(mean(item))
		sigma.append(std(item))
		skw.append(skewness(item))

	ax.scatter(sigma, mu, skw, c=color[i], marker='o', label=filename+str(i+1))

ax.set_xlabel('Standard Deviation')
ax.set_ylabel('Mean')
ax.set_zlabel('Skewness')
ax.legend()

plt.show()