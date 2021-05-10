#!python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import random


def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    html = requests.get(url, headers=headers).text
    return BeautifulSoup(html, "html.parser")

def get_info(movie_item):
    href = "http://geo.saitebi.ge{}".format(movie_item.a["href"])
    image = "http://geo.saitebi.ge{}".format(movie_item.a.div.img["src"])
    ge_title,en_title = movie_item.a.find(class_="a").get_text(),movie_item.a.find(class_="b").get_text()
    year = movie_item.a.find(class_="c").get_text()

    hover_wraper = movie_item.find("div", class_="hover-wraper")
    description = hover_wraper.find(class_="h-desc").get_text()
    imdb_rating,imdb_votes = hover_wraper.a.imdb.get_text(),hover_wraper.imdb_vote.get_text()

    result =  {
        "href": href,
        "image": image,
        "ge_title": ge_title,
        "en_title": en_title,
        "year": year,
        "description": description,
        "imdb_rating": imdb_rating,
        "imdb_votes": imdb_votes
    }
    return result

def scrape():
    fieldnames = ["href", "image", "ge_title", "en_title", "year", "description", "imdb_rating", "imdb_votes"]
    url = "http://geo.saitebi.ge"
    page_count = 0
    elapsed = 0
    next_btn = 1
    with open('movies_info.csv', mode='w', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        while next_btn:
            soup = get_soup(url)
            print("Scraping: {}".format(url))
            for movie in soup.find_all(class_="movie-items-wraper"):
                if movie.parent(id="content"):        
                    info = get_info(movie)
                    writer.writerow(info)
                else:
                    info = None

            next_btn = soup.find("a", attrs={"aria-label":"Next"})["href"]
            url = "http://geo.saitebi.ge{}".format(next_btn) if next_btn else None

            n = round(2+random.random(),3)
            elapsed+=n
            sleep(n)

            page_count+=1
            if page_count%20==0:
                print("Elapsed time: {}".format(elapsed))
            elif page_count==301:
                break
    print("\n\n*** Done Scraping ***\n")

def read():
    with open('movies_info.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(r"movies.txt", mode="w", encoding="utf-8") as file:
            ratings = []
            for row in csv_reader:
                try:
                    rating = float(dict(row)["imdb_rating"])
                except ValueError:
                    rating = 0
                if rating>8.5:
                    a = "Title: {0}\nRating: {1}\nVotes: {3}\nDescription: {2}\nImage: {4}\n\n".format(dict(row)["en_title"], rating, dict(row)["description"], dict(row)["imdb_votes"], dict(row)["image"])
                    file.write(a)
                    print(".", end="")
            #     ratings.append(rating)
            # rating = [round(x) for x in ratings]
            # print(rating)

read()