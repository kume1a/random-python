import random
import time

import requests
from bs4 import BeautifulSoup
import json

pages = {
    "სედანი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/1/avtomobilebi-sedani?stype=0&currency_id=3&det_search=0&ord=7&category_id=1&keyword=",
    "ჯიპი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/5/avtomobilebi-jipi?stype=0&currency_id=3&det_search=0&ord=7&category_id=5&keyword=",
    "კუპე": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/4/avtomobilebi-kupe?stype=0&currency_id=3&det_search=0&ord=7&category_id=4&keyword=",
    "ჰეჩბექი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/2/avtomobilebi-hechbeqi?stype=0&currency_id=3&det_search=0&ord=7&category_id=2&keyword=",
    "უნივერსალი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/3/avtomobilebi-universali?stype=0&currency_id=3&det_search=0&ord=7&category_id=3&keyword=",
    "პიკაპი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/29/avtomobilebi-pikapi?stype=0&currency_id=3&det_search=0&ord=7&category_id=29&keyword=",
    "მინივენი": "https://www.myauto.ge/ka/s/00/0/00/00/00/00/00/30/avtomobilebi-miniveni?stype=0&currency_id=3&det_search=0&ord=7&category_id=30&keyword=",
}

res = []
for category, category_page in pages.items():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    html_content = requests.get(category_page, headers=headers).content
    soup = BeautifulSoup(html_content, "html.parser")

    for page in range(2):
        print(f"category {category} page {page}")
        for container in soup.select(".car-short-info")[:20]:
            url = container.find(class_="car-name-left").h4.a['href']
            name = container.find(class_="car-name-left").h4.a.text.strip()

            car_list_price = container.find(class_="car-list-price")
            prices = car_list_price.find(class_="price-title-container").text.strip()
            price_gel = prices.split(" ")[0].strip()
            price_usd = prices.split(" ")[-1].strip()
            _id = car_list_price.find(class_="car-list-id").div.text.strip().split(" ")[1]

            year = container.find(class_="car-year").text.strip().split(" ")[0]
            description = container.find(class_="car-list-info").p.text.strip()

            car_list_detail = container.find(class_="car-list-detail")
            fuel = car_list_detail.find(class_="cr-engine").p.text.strip().split(" ")[0]
            distance = car_list_detail.find(class_="cr-road").p.text.strip().split(" ")[0]

            data = {
                "url": url,
                "name": name,
                "price_gel": price_gel,
                "price_usd": price_usd,
                "id": _id,
                "year": year,
                "description": description,
                "fuel": fuel,
                "distance": distance
            }
            res.append(data)
        time.sleep(random.random())

with open("data.json", "w") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
