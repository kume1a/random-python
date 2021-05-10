#!python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import ssl
import requests
import csv
from random import random
from time import sleep, perf_counter
import pycountry
import matplotlib.pyplot as plt
import numpy as np


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


countries = [
    'cok', 'vir', 'hmd', 'cck', 'mhl', 'fro', 'slb', 'stp', 'zmb', 'zwe', 'are', 'ant',
    'arm', 'abw', 'aus', 'aut', 'aze', 'bhs', 'bhr', 'bgd', 'brb', 'bel', 'blz', 'ben',
    'bmu', 'btn', 'blr', 'bol', 'bes', 'bih', 'bwa', 'bra', 'brn', 'iot', 'vgb', 'bgr',
    'bfa', 'bdi', 'chl', 'chn', 'hrv', 'cuw', 'cyp', 'tcd', 'mne', 'cze', 'umi', 'dnk',
    'cod', 'dma', 'dom', 'dji', 'egy', 'ecu', 'eri', 'est', 'eth', 'flk', 'fji', 'phl',
    'fin', 'fra', 'atf', 'gab', 'gmb', 'sgs', 'gha', 'gib', 'grc', 'grd', 'grl', 'geo',
    'gum', 'ggy', 'guf', 'guy', 'glp', 'gtm', 'gnb', 'gnq', 'gin', 'hti', 'esp', 'nld',
    'hnd', 'hkg', 'ind', 'idn', 'irq', 'irn', 'irl', 'isl', 'isr', 'jam', 'jpn', 'yem',
    'jey', 'jor', 'cym', 'khm', 'cmr', 'can', 'qat', 'kaz', 'ken', 'kgz', 'kir', 'col',
    'com', 'cog', 'kor', 'prk', 'cri', 'cub', 'kwt', 'lao', 'lso', 'lbn', 'lbr', 'lby',
    'lie', 'ltu', 'lux', 'lva', 'mkd', 'mdg', 'myt', 'mac', 'mwi', 'mdv', 'mys', 'mli',
    'mlt', 'mnp', 'mar', 'mtq', 'mrt', 'mus', 'mex', 'fsm', 'mmr', 'mda', 'mco', 'mng',
    'msr', 'moz', 'nam', 'nru', 'npl', 'deu', 'ner', 'nga', 'nic', 'niu', 'nfk', 'nor',
    'ncl', 'nzl', 'omn', 'pak', 'plw', 'pse', 'pan', 'png', 'pry', 'per', 'pcn', 'pyf',
    'pol', 'pri', 'prt', 'zaf', 'caf', 'cpv', 'reu', 'rus', 'rou', 'rwa', 'esh', 'kna',
    'lca', 'vct', 'blm', 'maf', 'spm', 'slv', 'asm', 'wsm', 'smr', 'sen', 'srb', 'syc',
    'sle', 'sgp', 'sxm', 'svk', 'svn', 'som', 'lka', 'usa', 'swz', 'sdn', 'ssd', 'sur',
    'sjm', 'syr', 'che', 'swe', 'tjk', 'tha', 'twn', 'tza', 'tls', 'tgo', 'tkl', 'ton',
    'tto', 'tun', 'tur', 'tkm', 'tca', 'tuv', 'uga', 'ukr', 'ury', 'uzb', 'vut', 'wlf',
    'vat', 'ven', 'hun', 'gbr', 'vnm', 'ita', 'civ', 'bvt', 'cxr', 'imn', 'shn', 'ala',
    'afg', 'alb', 'dza', 'and', 'ago', 'aia', 'ata', 'atg', 'sau', 'arg'
]

fieldnames = [
    'country', 'total', 'maleP', 'femaleP', '13-17 female',
    '13-17 male', '18-24 female', '18-24 male', 
    '25-34 female', '25-34 male', '35-44 female', 
    '35-44 male', '45-54 female', '45-54 male',
    '55-64 female', '55-64 male', '65+ female', '65+ male'
]


def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    try:
        html = requests.get(url, headers=headers).text
        return BeautifulSoup(html, "html.parser")#.prettify('utf-8')
    except requests.exceptions.ConnectionError:
        return None

def extract_data(soup, country):
    total = soup.select(".visualize-stats--total")[0].get_text().strip()
    genders = soup.select(".visualize-stats--genders")[0].get_text()

    femaleP, maleP = list(filter(lambda x: r"%" in x, genders.split(" ")))

    data = {
        "country": country,
        "total": total,
        "maleP" : maleP.strip(),
        "femaleP" : femaleP.strip()
    }

    for element in soup.select(".visualize-chart--column"):
        age = element.select(".visualize-chart--gender")[0]["title"].split(":")[0].split(" ")[1]
        data["{} female".format(age)] = element.select(".visualize-chart--gender")[0].get_text().strip()
        data["{} male".format(age)] = element.select(".visualize-chart--gender")[1].get_text().strip()
                
    return data

def scrape():
    start = perf_counter()
    with open('napoleonFacebook.csv', mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i,country in enumerate(countries):
            url = "https://napoleoncat.com/stats/facebook-users-in-{}/2019/11".format(country)
            try:
                writer.writerow(extract_data(get_soup(url), country))        
            except Exception:
                print("### Error ###")
                sleep(1+random())
                continue
            print("Scraped >> %s"%url)

            if i%5==0:
                print("Elapsed {} seconds".format(round(perf_counter()-start),3))
            sleep(3+random())

with open('napoleonFacebook.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    countries, total = [],[]
    for i in csv_reader:
        countries.append(pycountry.countries.get(alpha_3=i.get("country").upper()).name)
        total.append(i.get("total"))

print(countries, total)
plt.barh(countries[:10], range(max(*total)))

# plt.xticks(ticks=np.arange(max(*total)), labels=np.arange(100))

plt.show()