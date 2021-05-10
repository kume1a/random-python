#!python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("movies_info.csv")
data = zip(data["year"], data["imdb_rating"])

imdb_by_years = {x:0 for x in range(1925, 2020)}
years_count = {x:0 for x in range(1925, 2020)}

for year,imdb in data:
    imdb_by_years[year] += imdb 
    years_count[year] += 1

data = {x:0 if years_count[x]==0 else imdb_by_years[x]/years_count[x] for x in range(1925, 2020)}

x,y = [year for year in range(1925, 2020)], [data[x] for x in range(1925, 2020)]

plt.style.use('fivethirtyeight')

plt.plot(x, y, linestyle='-', label="Median IMDB by year")

plt.xlabel("Year")
plt.ylabel("Medina IMDB")

plt.legend()
plt.show()