from csv_helper import *
from util import *
import sys

def statistic_cal(filename, chunk_size):

	arr = csv_reader('../../../data/' + filename + '.csv')
	# cleaning
	clean_arr = arr
	# chunking
	sample = list(chunks(clean_arr, chunk_size))
	a = feature_extract(sample)
	csv_writer('../../../data/' + filename + str(chunk_size) + '.csv' , a)

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

if __name__ == "__main__":
	statistic_cal(sys.argv[1], int(sys.argv[2]))
