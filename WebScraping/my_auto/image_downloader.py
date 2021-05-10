import requests
import json
import os
import time
import random

if not os.path.exists("./images"):
    os.mkdir("images")
os.chdir("images") 

with open("../details.json", "r") as f:
    data = json.load(f)
    for item in data:
        _id = item["id"]
        images = item["images"]

        for index, image_url in enumerate(images[:10]):
            image_name = f"{_id}-{index + 1}"
            if index == 0:
                image_name += "-large"

            with open(f"{image_name}.jpg", "wb") as image_file:
                image_file.write(requests.get(image_url).content)
            print(f"downloaded {image_name}")
            time.sleep(.4 + random.random())
