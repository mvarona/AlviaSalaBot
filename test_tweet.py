import unittest
import tweet
import os

class TestTweet(unittest.TestCase):

	def test_GIVEN_env_secrets_WHEN_running_main_THEN_they_are_loaded(self):
		tweet.main()
		self.assertEqual(os.environ.get('TEST_SECRET'), '1234')

	def test_GIVEN_two_dates_WHEN_calculating_days_between_them_THEN_the_number_of_days_is_returned(self):
		date1 = '2023-01-01'
		date2 = '2023-01-15'
		result = tweet.days_between(date1, date2)
		self.assertEqual(result, 14)

if __name__ == '__main__':
	unittest.main()