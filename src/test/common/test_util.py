import unittest
import util

class TestUtil(unittest.TestCase):

	global alist
	alist = [1,2,3,4,5]

	def test_mean(self):
		result = util.mean(alist)
		self.assertEquals(result, 3.0)

	def test_std(self):
		result = round(util.std(alist),2)
		self.assertEquals(result, 1.41)

	def test_mad(self):
		result = util.mad(alist)
		self.assertEquals(result, 1.2)

	def test_skewness(self):
		result = util.skewness(alist)
		self.assertEquals(result, 0.0)

	def test_kurtosis(self):
		result = round(util.kurtosis(alist),2)
		self.assertEquals(result, -1.3)




if __name__ == '__main__':
	unittest.main()

