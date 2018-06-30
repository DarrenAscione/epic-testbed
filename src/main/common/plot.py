from csv_helper import *
from util import *
import matplotlib.pyplot as plt

arr = csv_reader('../../../data/geid1_l1.csv')

# cleaning
clean_arr = arr[600:900]

print len(clean_arr)

# chunking
sample = list(chunks(clean_arr, 100))

# feature extraction
def feature_extract(sample):
	vector_list = []
	for item in sample:
		vector = []
		vector.append(mean(item))
		vector.append(std(item))
		vector.append(mad(item))
		vector.append(skewness(item))
		vector.append(kurtosis(item))
		vector_list.append(vector)
	return vector_list


a = feature_extract(sample)
# plt.plot()
# plt.show()

csv_writer('../../../data/test.csv', a)
	
