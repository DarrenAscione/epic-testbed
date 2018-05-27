import unittest
import util

class TestUtil(unittest.TestCase):

	def test_mean(self):
		alist = [1,2,3,4,5]
		result = util.mean(alist)
		self.assertEquals(result, 3)

if __name__ == '__main__':
	unittest.main()

