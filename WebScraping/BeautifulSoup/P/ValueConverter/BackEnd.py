#!python3
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

class Crawler:
	def __init__(self, url):
		self.url = url
		self.soup = BeautifulSoup(requests.get(url).text, "html.parser")
		self.js = str(self.soup.body.script)

	def parse_js(self):
		valutes = re.search(r"(\"exchangeRates\":{)(.*)(}},\"routing\")", self.js).group(2)
		valutes_dict = {x[0].strip('"'):x[1] for x in [x.split(":") for x in valutes.split(",")]}
		return valutes_dict

	def parse_details(self):
		details = re.search(r"({\"currencyDetails\":{)(.*)(}}}}}})", self.js).group(2)
		return {x:x for x in details.split(":{")}

if __name__ == '__main__':
	spider = Crawler("https://valuta.exchange/")
	# details = spider.parse_details()
	# print(details)
	print(spider.js)