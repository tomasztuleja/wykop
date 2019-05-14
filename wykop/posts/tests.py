from django.test import TestCase

# Create your tests here.

class ReactionTest(TestCase):
	def test_true(self):
		self.assertTrue(True)
		self.assertFalse(False)

	def tesst_fail(self):
		self.assertTrue(False)
