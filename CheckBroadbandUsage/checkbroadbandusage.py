#!usr/bin/python3

# Checks the remaining data for Home Broadband users and notifies the user.
# Author: digi0ps
# Language: Python
# Requiremnts: requests, bs4, pync

# Imports
try:
	import requests
	import os
	from bs4 import BeautifulSoup
	from pync import Notifier
except ImportError:
	print("ERROR: All requirements not installed")
	print("Run: 'pip install -r requirements.txt' to run properly.")


# URL of the remaining data page
URL = "http://172.172.72.254:2281/html/user_status.php"


def fetch_website_source():
	try:
		req = requests.get(URL)
		req.raise_for_status()
		return req.text
	except:
		print("ERROR")


def parse_website(source):
	webpage = BeautifulSoup(source, "html5lib")
	data = {"today": webpage.find_all("tr")[-2].get_text(), "monthly": webpage.find_all("tr")[-1].get_text()}
	return data


def notify_mac(data):
	message = "%s\n%s" % (data["today"], data["monthly"])
	print(message)
	Notifier.notify(message, title="Broadband Usage", open=URL)


def kill_notification():
	Notifier.remove(os.getpid())
	exit()


if __name__ == '__main__':
	source = fetch_website_source()
	data = parse_website(source)
	notify_mac(data)
