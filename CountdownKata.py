#!/usr/bin/env python

import unittest

class TrueTest(unittest.TestCase):
	def test_method(self):
		self.assertEqual(True, True)


if __name__ == "__main__":
	unittest.main()
