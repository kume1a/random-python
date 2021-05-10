import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

def getSoup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")

fieldnames = ["year", "company", "brand_value", "logo"] 

for year in range(2000, 2019):
    url = "https://www.interbrand.com/best-brands/best-global-brands/previous-years/{}/".format(year)
    soup = getSoup(url)


    with open('brands.csv', mode='a', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for a in soup.select(".brand-item"):
            brand_value = a.select(".brand-value")[0].get_text().strip()[:-1]
            company = a.select(".logo-img")[0]["alt"]
            logo = a.select(".logo-img")[0]["src"]
            info = {"year": str(year), "company": company, "brand_value": brand_value, "logo": logo}

            print(info)
            # exit()
            writer.writerow(info)
        print((" --=-- {} ==-== ".format(year))*50)
        print(year)
        sleep(2)