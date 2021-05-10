#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import requests
import csv
import time 
import random


def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, "html.parser")