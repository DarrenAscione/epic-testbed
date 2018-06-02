import unittest
import pcaptxt
import os

class TestPcapTxt(unittest.TestCase):

	def test_covert(self):
		result = pcaptxt.convert("cipKiller40-50.pcap", "test.txt")
		self.assertTrue(os.path.isfile("../../../data/test.txt"))
		os.remove("../../../data/test.txt")


if __name__ == '__main__':
	unittest.main()
		
