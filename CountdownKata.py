#!/usr/bin/env python

import unittest

def countdownFrom(startPoint):
	result = []
	for index in range (startPoint + 1):
		result += [startPoint - index]
	return result

class CountdownKataTest(unittest.TestCase):
	def test_0_return_an_array_with_0(self):
		self.assertEqual([0], countdownFrom(0))

	def test_1_return_an_array_with_1_and_0(self):
		self.assertEqual([1, 0], countdownFrom(1))

	def test_2_return_an_array_with_2_and_1_and_0(self):
		self.assertEqual([2, 1, 0], countdownFrom(2))

	def test_3_return_an_array_with_3_2_and_1_and_0(self):
		self.assertEqual([3, 2, 1, 0], countdownFrom(3))

if __name__ == "__main__":
	unittest.main()
