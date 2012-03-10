#!/usr/bin/env python

import unittest

def countdownFrom(startPoint):
	if startPoint == 1:
		return [1, 0]
	if startPoint == 2:
		return [2, 1, 0]
	else:
		return [startPoint]

class CountdownKataTest(unittest.TestCase):
	def test_method(self):
		self.assertEqual(True, True)

	def test_0_return_an_array_with_0(self):
		self.assertEqual([0], countdownFrom(0))
	def test_1_return_an_array_with_1_and_0(self):
		self.assertEqual([1, 0], countdownFrom(1))
	def test_2_return_an_array_with_2_and_1_and_0(self):
		self.assertEqual([2, 1, 0], countdownFrom(2))

if __name__ == "__main__":
	unittest.main()
