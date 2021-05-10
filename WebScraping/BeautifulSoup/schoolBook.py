#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from base64 import b64decode
from random import random
from time import sleep

payload = {"Username": b64decode(b'MDEwMjkwMDg2OTY=').decode(),
           "Password": b64decode(b'c2Nob29sYm9vazAwODg=').decode()}
URL = "https://eservices.schoolbook.ge"
print(payload)
# with requests.Session() as s:
#     s.post(URL, data=payload).text
#     sleep(1.5+random())
#     soup = BeautifulSoup(s.get(URL+"/Parent/HomeWorks").text, "html.parser")
#     sleep(1.5+random())

#     pdfLink = soup.find(class_="pdfDownload")["href"]

#     with open("homework.pdf", "wb") as pdfFile:
#         pdfFile.write(s.get(URL+pdfLink).content)