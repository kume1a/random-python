import json
import requests
from bs4 import BeautifulSoup

import time
import random

f = open("data.json", "r")
data = json.load(f)
f.close()
f = None

res = []
for car in data:
    try:
        url = car["url"]
        _id = car["id"]

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        html_content = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html_content, "html.parser")

        is_levied = soup.find(class_="levy-true") is not None
        images = [soup.find(class_="main-image-block").img['src']]
        images.extend(list(map(lambda div: div.img['src'], soup.select(".thumbnail-image"))))

        details = {}
        table_rows = soup.select(".th-left")
        for row in table_rows:
            try:
                key = row.find("div", class_="th-key").text.strip()
                value = row.find("div", class_="th-value").text.strip()

                details[key] = value
            except AttributeError:
                pass

        category = details.get("კატეგორია")
        manufacturer = details.get("მწარმოებელი")
        model = details.get("მოდელი")
        release_year = details.get("გამოშვების წელი")
        fuel_type = details.get("საწვავის ტიპი")
        engine_capacity = details.get("ძრავის მოცულობა")
        distance = details.get("გარბენი").split(" ")[0]
        cylinders = details.get("ცილინდრები")
        gear_box = details.get("გადაცემათა კოლოფი")
        wheel_side = details.get("საჭე")
        color = details.get("ფერი")
        vin_code = details.get("VIN")

        car_details = {
            "id": _id,
            "is_levied": is_levied,
            "phone_number": None,
            "images": images,
            "category": category,
            "manufacturer": manufacturer,
            "model": model,
            "release_year": release_year,
            "fuel_type": fuel_type,
            "engine_capacity": engine_capacity,
            "distance": distance,
            "cylinders": cylinders,
            "gear_box": gear_box,
            "wheel_side": wheel_side,
            "color": color,
            "vin_code": vin_code
        }
        if not car_details["vin_code"]:
            car_details["vin_code"] = None

        res.append(car_details)
        print(f"scraping {url}")
    except Exception as e:
        print(e)
    time.sleep(random.random())

with open("details.json", "w") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
