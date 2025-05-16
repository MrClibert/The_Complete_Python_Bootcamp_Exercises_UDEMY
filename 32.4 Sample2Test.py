
import unittest
import Sample2

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = Sample2.cap_text(text)
		self.assertEqual(result, 'Python')

	def test_multiple_words(self):
		text = 'monty python'
		result = Sample2.cap_text(text)
		self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
	unittest.main()



#then run in command prompt: python Sample2Test.py




