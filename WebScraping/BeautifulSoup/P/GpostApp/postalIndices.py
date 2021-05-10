#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import ssl
import requests
import time
import random

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, "html.parser")

def get_data(table_rows):
    for row in table_rows:
        index = row.find("td", class_="td-01").get_text()
        street_name = row.find("td", class_="td-03").get_text()
        yield f"{index} - {street_name}\n"

def scrape_and_write(URL, alphabet, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for letter in alphabet:
            url = URL%letter
            soup = get_soup(url)

            zipcode_tables = soup.select(".zipcodes-table")
            for table_rows in [e.findChildren("tr" , recursive=False) for e in zipcode_tables]:
                for row_data in get_data(table_rows):
                    file.write(row_data)
            print(f"Scraping done on {url}")
            time.sleep(random.uniform(1,2))

if __name__ == "__main__":
    ALPHABET_KA = [
    "ა","ბ","გ","დ","ე","ვ","ზ","თ","ი","კ","ლ",
    "მ","ნ","ო","პ","ჟ","რ","ს","ტ","უ","ფ","ქ",
    "ღ","ყ","შ","ჩ","ც","წ","ჭ","ხ","ჯ","ჰ"
    ]
    ALPHABET_EN = [
        "A", "B", "D", "E", "G", "I", "K", "L", "M",
        "N", "O", "P", "R", "S", "T", "V", "Z"
    ]

    URL_EN = "https://www.gpost.ge/?site-path=help/zipcodes/&group=1&letter=%s&site-lang=en"
    URL_KA = "https://www.gpost.ge/?site-path=help/zipcodes/&group=1&letter=%s"

    scrape_and_write(URL_KA, ALPHABET_KA, "postal_indices_ka.txt")
    scrape_and_write(URL_EN, ALPHABET_EN, "postal_indices_en.txt")