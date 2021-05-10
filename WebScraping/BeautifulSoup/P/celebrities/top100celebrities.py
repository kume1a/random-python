#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import ssl
import json
import os
import requests
from time import sleep
from random import random


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, "html.parser")

def get_data(item):
    name = item.find("h3").a.get_text()
    image = item.find("img")["src"]

    return {
        "name":name.strip(),
        "image":image
    }

def scrape():
    URL = "https://www.imdb.com/list/ls055075798/"
    soup = get_soup(URL)

    items = [get_data(e) for e in soup.select(".lister-item")]

    with open('celebrities.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def downloadImages():
    with open("celebrities.json", "r", encoding="utf-8") as file:
        items = []
        items = json.load(file)

    dstDir = "C:\\Users\\PC\\Desktop\\Java\\AndroidDevelopment\\GuessCelebrity\\app\\src\\main\\res\\drawable\\"

    for item in items[1:]:
        name, image = item.values()

        print("\t\timage_name.put(\"{}\", R.drawable.{});".format(name, name.lower().replace(" ", "_")))
        with open(dstDir + item["name"].lower().replace(" ", "_") + "." + image.split('.')[-1], "wb") as file:
            file.write(requests.get(image).content)
        sleep(.2+random())