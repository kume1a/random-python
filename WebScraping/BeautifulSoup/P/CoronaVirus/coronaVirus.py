#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime



# Created on 23/3/2020

def getSoup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, "html.parser")

def scrape(tr):
    tds = tr.find_all("td")

    country = tds[0].get_text()
    totalCases = tds[1].get_text()
    newCases = tds[2].get_text()
    totalDeaths = tds[3].get_text().strip()
    newDeaths = tds[4].get_text()
    totalRecovered = tds[5].get_text()
    activeCases = tds[6].get_text()
    seriousCritical = tds[7].get_text()
    totCases1mPop = tds[8].get_text()

    return {
        "country":country,
        "totalCases":totalCases,
        "newCases":newCases,
        "totalDeaths":totalDeaths,
        "newDeaths":newDeaths,
        "totalRecovered":totalRecovered,
        "activeCases":activeCases,
        "seriousCritical":seriousCritical,
        "totCases1mPop":totCases1mPop
    }

fieldNames = [
    "country",
    "totalCases",
    "newCases",
    "totalDeaths",
    "newDeaths",
    "totalRecovered",
    "activeCases",
    "seriousCritical",
    "totCases1mPop"
]

URL = "https://www.worldometers.info/coronavirus/"
soup = getSoup(URL)

tableDiv = soup.find(class_="main_table_countries_div")
tableItems = tableDiv.find_all("tr")


today = datetime.today().strftime('_%Y.%m.%d_%H.%M.%S')
fileName = "coronaVirusStats{}.csv".format(today)

with open(fileName, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()

    for tr in tableItems[1:-1]:
        data = scrape(tr)
        writer.writerow(data)
        print(data)
        print("\n")