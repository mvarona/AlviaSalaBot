from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import os

def days_between(date1, date2):
	d1 = datetime.strptime(date1, "%Y-%m-%d")
	d2 = datetime.strptime(date2, "%Y-%m-%d")
	days = d2 - d1
	return days.days

def build_message():
	today = date.today().strftime("%Y-%m-%d")
	days = days_between('2020-03-14', today)
	message = "Hace " + str(days) + " días @Renfe quitó el 50% de los Alvia entre Salamanca y Madrid.\nLlevamos 3 años aislados!!\nHartos de ser ciudadanos de 2ª!\nFirma https://www.change.org/p/tren-rápido-salamanca-ya\n@raquelsjimenez @mitmagob @alferma1 @CGCarbayo @A3Noticias @cyltv @elmundoes\n#EspañaVaciada #Renfe #TrenRápidoYa"
	return message

def main():
	load_dotenv()
	#tweet()

if __name__ == "__main__":
	main()
	