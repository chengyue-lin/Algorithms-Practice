import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest

class test_leet(unittest.TestCase):

	def setUp(self):
		print "Hello World!!"


if __name__ == "__main__":
	unittest.main()