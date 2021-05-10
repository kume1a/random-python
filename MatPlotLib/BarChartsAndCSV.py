from matplotlib import pyplot as plt
import numpy as np
from collections import Counter 
from csv import DictReader
import pandas as pd

plt.style.use("fivethirtyeight")

# ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
# py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
#             84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
# js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
#             78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
# dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
#          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# x_indexes = np.arange(len(ages_x))
# width = .25 # defaultWidth = .8


# plt.bar(x_indexes - width, py_dev_y, label="Python", width=width, color="b")
# plt.bar(x_indexes, js_dev_y, label="JS", width=width, color="#ee2311")
# plt.bar(x_indexes + width, dev_y, label="All Devs", width=width)

# plt.xticks(ticks=x_indexes, labels=ages_x)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with open("data.csv") as csv_file:
    csv_reader = DictReader(csv_file)

    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

data = pd.read_csv("data5.csv")
lang_responses = data["LanguagesWorkedWith"]


language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(";"))


language_counter = language_counter.most_common(15)
languages = [x[0] for x in language_counter][::-1]
counter = [x[1] for x in language_counter][::-1]


plt.barh(languages, counter) # [0] Y_axis   [1] X_axis

plt.title("Most Popular Languages")
plt.xlabel("Num of People who Use")

plt.grid()
plt.legend()
plt.show()