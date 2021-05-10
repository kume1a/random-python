#!python3
# -*- coding: utf-8 -*-

import requests
import re
from time import sleep
import os

os.mkdir("Images")
os.chdir("Images")

image_url_regex = re.compile(r"([a-z\-_0-9\/\:\.]*\.(jpg|jpeg|png|gif))")

url = "https://pixabay.com/images/search/nature/"
html = requests.get(url)

urls = image_url_regex.findall(html.text)
num=1
for url in set(urls):
	if not url[0].startswith("/"):
		print("Downloading %s"%url[0])
		image_binary = requests.get(url[0]).content
		with open("Image%s.%s"%(num, url[1]), "wb") as file:
			file.write(image_binary)
		num+=1
		sleep(1.2)