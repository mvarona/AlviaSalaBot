import unittest
import tweet
import os
from datetime import date
from unittest import TestCase
import mock
from unittest.mock import patch
import requests
from requests_oauthlib import OAuth1

class TestTweet(unittest.TestCase):

	def test_GIVEN_env_secrets_WHEN_running_main_THEN_they_are_loaded(self):
		f = tweet.make_request
		tweet.make_request = mock.Mock(return_value="")
		tweet.main()
		self.assertEqual(os.environ.get("TEST_SECRET"), "1234")
		tweet.make_request = f

	def test_GIVEN_two_dates_WHEN_calculating_days_between_them_THEN_the_number_of_days_is_returned(self):
		date1 = "2023-01-01"
		date2 = "2023-01-15"
		result = tweet.days_between(date1, date2)
		self.assertEqual(result, 14)

	def test_GIVEN_date_WHEN_building_message_THEN_the_message_for_that_date_is_returned(self):
		d0 = date(2020, 3, 14)
		d1 = date.today()
		days = (d1 - d0).days
		expected_message = "Hace " + str(days) + " días @Renfe quitó el 50% de los Alvia entre Salamanca y Madrid.\nLlevamos 3 años aislados!!\nHartos de ser ciudadanos de 2ª!\nFirma https://www.change.org/p/tren-rápido-salamanca-ya\n@raquelsjimenez @mitmagob @alferma1 @CGCarbayo @A3Noticias @cyltv @elmundoes\n#EspañaVaciada #Renfe #TrenRápidoYa";
		result = tweet.build_message()
		self.assertEqual(result, expected_message)

	@mock.patch('tweet.requests.post')
	def test_GIVEN_message_WHEN_building_request_AND_correct_response_THEN_the_request_succeeds(self, mock_post):
		mock_post.return_value.status_code = 201
		mock_post.return_value.json.return_value = {"response": "OK"}
		result = tweet.make_request()
		self.assertEqual(result, True)
		self.assertEqual(mock_post.call_args[1]["json"], {'text': tweet.build_message()})
		self.assertEqual(mock_post.call_args[1]["headers"], {'Content-Type': 'application/json'})
		self.assertEqual(str(type(mock_post.call_args[1]["auth"])), "<class 'requests_oauthlib.oauth1_auth.OAuth1'>")

def set_global_mocks():
	tweet.get_url = mock.Mock(return_value="http://bmsalamanca.com/others/AlviaSalamancaBot/request.txt")
	os.environ["CONSUMER_KEY"] = "CONSUMER_KEY"
	os.environ["CONSUMER_SECRET"] = "CONSUMER_SECRET"
	os.environ["ACCESS_TOKEN"] = "ACCESS_TOKEN"
	os.environ["ACCESS_TOKEN_SECRET"] = "ACCESS_TOKEN_SECRET"

if __name__ == "__main__":
	set_global_mocks()
	unittest.main()