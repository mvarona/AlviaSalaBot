import unittest
import tweet
import os
from datetime import date

class TestTweet(unittest.TestCase):

	def test_GIVEN_env_secrets_WHEN_running_main_THEN_they_are_loaded(self):
		tweet.main()
		self.assertEqual(os.environ.get('TEST_SECRET'), '1234')

	def test_GIVEN_two_dates_WHEN_calculating_days_between_them_THEN_the_number_of_days_is_returned(self):
		date1 = '2023-01-01'
		date2 = '2023-01-15'
		result = tweet.days_between(date1, date2)
		self.assertEqual(result, 14)

	def test_GIVEN_date_WHEN_building_message_THEN_the_message_for_that_date_is_returned(self):
		d0 = date(2020, 3, 14)
		d1 = date.today()
		days = (d1 - d0).days
		expected_message = "Hace " + str(days) + " días @Renfe quitó el 50% de los Alvia entre Salamanca y Madrid.\nLlevamos 3 años aislados!!\nHartos de ser ciudadanos de 2ª!\nFirma https://www.change.org/p/tren-rápido-salamanca-ya\n@raquelsjimenez @mitmagob @alferma1 @CGCarbayo @A3Noticias @cyltv @elmundoes\n#EspañaVaciada #Renfe #TrenRápidoYa";
		result = tweet.build_message()
		self.assertEqual(result, expected_message)

if __name__ == '__main__':
	unittest.main()