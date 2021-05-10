#!python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep

def GimmeSoup(url):
	html = requests.get(url).text
	return BeautifulSoup(html, "html.parser")

for page in range(1, 51):
	url = "http://books.toscrape.com/catalogue/page-%s.html"%page
	soup = GimmeSoup(url)

	print("Scraping %s"%url)
	elements = ""
	for li in soup.find("ol", class_="row"):
		try:
			elements+="Title: %s\n" % li.find("h3").a.get_text()
			elements+="Price: %s\n" % li.find("p", class_="price_color").get_text()
			elements+="href: %s\n" % li.find("div", class_="image_container").a["href"]
			elements+="Image src: http://books.toscrape.com/%s\n\n" % li.find("div", class_="image_container").a.img["src"]
		except Exception as e:
			pass

	with open("BooksToScrape.txt", "a") as file:
		try:
			file.write(elements)
		except Exception as err:
			print("*** Error Occured ***")

	sleep(.4)