from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import requests
from requests_oauthlib import OAuth1
import json
import os

def days_between(date1, date2):
	d1 = datetime.strptime(date1, "%Y-%m-%d")
	d2 = datetime.strptime(date2, "%Y-%m-%d")
	days = d2 - d1
	return days.days

def build_message():
	today = date.today().strftime("%Y-%m-%d")
	days = days_between("2020-03-14", today)
	message = "Hace " + str(days) + " días @Renfe quitó el 50% de los Alvia entre Salamanca y Madrid.\nLlevamos 3 años y medio aún más aislados!!\nHartos de ser ciudadanos de 2ª!\nFirma https://www.change.org/p/tren-rápido-salamanca-ya\n@oscar_puente_ @transportesgob @alferma1 @CGCarbayo\n#EspañaVaciada #Renfe #TrenRápidoYa"
	return message

def format_message(message):
	return {"text": "{}".format(message)}

def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
	auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
	return auth

def get_url():
	return "https://api.twitter.com/2/tweets"

def make_request():
	consumer_key = os.environ.get("CONSUMER_KEY")
	consumer_secret = os.environ.get("CONSUMER_SECRET")
	access_token = os.environ.get("ACCESS_TOKEN")
	access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

	message = build_message()
	payload = format_message(message)
	url = get_url()

	auth = connect_to_oauth(
		consumer_key, consumer_secret, access_token, access_token_secret
	)

	response = requests.post(
		auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
	)

	if 'content-type' in response.headers:
		if 'json' in response.headers['content-type']:
			debug_response = json.dumps(response.json())
	else:
		debug_response = response.text

	if response.status_code not in range(200, 300):
		raise ValueError("Error " + str(response.status_code) + ". Response: " + debug_response + ". Tweet: " + build_message())
		return False
	else:
		print("Status: " + str(response.status_code) + ". Tweet: " + build_message())
		return True

def main():
	load_dotenv()
	make_request()

if __name__ == "__main__":
	main()
