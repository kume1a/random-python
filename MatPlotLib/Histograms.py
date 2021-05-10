import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = list(range(10, 101, 10))

median_age = 29

# plt.hist(ages, bins=6, edgecolor="black")
# plt.hist(ages, bins=bins, edgecolor="black")

data = pd.read_csv('data2.csv')
ages = data['Age']

plt.hist(ages, bins=bins, log=True, edgecolor="black")
plt.axvline(median_age, color="#8f0000", linewidth=2, label="Median Age")

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.legend()
plt.show()