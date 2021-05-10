#!python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import random

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def scrapeGpost(trackingCodes):
    def get_soup(url, trackID):
        data = {"instance[trackid]": trackID, "submit": ""}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        }
        html = requests.post(url, headers=headers, data=data).text
        return BeautifulSoup(html, "html.parser")
    i = 1
    URL = "http://gpost.ge/?site-lang=ka&site-path=help/tracking/"

    for name,ID in trackingCodes.items():
        soup = get_soup(URL, ID)
        print("{} ({})\n".format(name, ID))
        for e in chunks(soup.select(".spb-04")[:-3], 2):
            print("\t{} {}".format(e[0].get_text(), e[1].get_text()))
            if i%2==0:
                print("\t", end="")
                print("_"*50)
            i+=1
        print("\n")
        sleep(.3+random())

trackingCodes = {
    "usb": "LA075761456CN",
    "keyboard": "LA085985095CN",
    "...": "S00000116888466"
}

if __name__=="__main__":
    scrapeGpost(trackingCodes)
    # scrapeParcel(trackingCodes)