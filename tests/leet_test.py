from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import unittest
from leetcode import remove_duplicates

class test_leet(unittest.TestCase):

	def setUp(self):
		print "Hello World!!"

	def test_remove_duplicates(self):
		sol = remove_duplicates.Solution()
		self.assertEqual(sol.removeDuplicates([1, 1, 2]), 2)

if __name__ == "__main__":
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(test_leet)
	unittest.TextTestRunner(verbosity=2).run(suite)