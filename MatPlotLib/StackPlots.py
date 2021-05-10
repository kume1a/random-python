from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
# plt.pie([1, 1, 1], labels=["Player 1", "Player2", "Player3"])


# minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

# colors = ["#008fd5", "#fc4f30", "#e5ae37"]
# labels = ["Player1", "Player2", "Player3"]

# plt.stackplot(minutes, player1, player2, player3, colors=colors, labels=labels)


days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

developer1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
developer2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
developer3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

colors = ["#008fd5", "#fc4f30", "#e5ae37"]
labels = ["developer1", "developer2", "developer3"]

plt.stackplot(days, developer1, developer2, developer3, colors=colors, labels=labels)

# plt.legend(loc="upper left")
plt.legend(loc=(0.07, 0.05)) # 7% from left and 5% from bottom
plt.title("Stack Plot")
plt.tight_layout()
plt.show()