from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")


# slices0 = [12, 42, 0.9, 102]
# labels0 = ["12", "42", "0.9", "102"]
# colors = ["#008fd5", "#fc4f30", "#e5ae37", "#6d904f"]
# plt.pie(slices0, labels=labels0, colors=colors, wedgeprops={"edgecolor":"black"})

slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
explode = [0,0,0,.15,0] # 15% of radius exploded out 

plt.pie(slices[:5], labels=labels[:5], wedgeprops={"edgecolor":"black"},
        explode=explode, shadow=True, startangle=30, autopct="%1.1f%%")


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()