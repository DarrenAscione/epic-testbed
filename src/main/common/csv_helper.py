import csv

def csv_reader(filename):
	arr = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		for row in reader:
			arr.append(float(row[0]))
	return arr

def csv_writer(filename, arr, header = None):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		if header != None:
			writer.writerow(header)
		for item in arr:
			writer.writerow(item)

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]	
