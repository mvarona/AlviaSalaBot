import unittest
import tweet
import os

class TestTweet(unittest.TestCase):

	def test_GIVEN_env_secrets_WHEN_running_main_THEN_they_are_loaded(self):
		tweet.main()
		self.assertEqual(os.environ.get('TEST_SECRET'), '1234')

if __name__ == '__main__':
	unittest.main()