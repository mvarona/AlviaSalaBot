from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import os

def days_between(date1, date2):
	delta1 = datetime.strptime(date1, "%Y-%m-%d")
	delta2 = datetime.strptime(date2, "%Y-%m-%d")
	days = delta2 - delta1
	return days.days

def main():
	load_dotenv()
	#tweet()

if __name__ == "__main__":
	main()
