import matplotlib.pyplot as plt

# print(plt.style.available)
# plt.style.use("dark_background")
# plt.xkcd()


ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


plt.plot(ages_x, py_dev_y, label="Python", color="k", linestyle="--", marker="D")
plt.plot(ages_x, js_dev_y, label="JS", color="#ee2311", linewidth=5 )
plt.plot(ages_x, dev_y, label="All Devs")

plt.title("Salary (age)")
plt.xlabel("Age")
plt.ylabel("Median Salary")


# A format string consists of a part for color, marker and line:
# fmt = '[marker][line][color]'

# Markers

# character   description
# '.' point marker
# ',' pixel marker
# 'o' circle marker
# 'v' triangle_down marker
# '^' triangle_up marker
# '<' triangle_left marker
# '>' triangle_right marker
# '1' tri_down marker
# '2' tri_up marker
# '3' tri_left marker
# '4' tri_right marker
# 's' square marker
# 'p' pentagon marker
# '*' star marker
# 'h' hexagon1 marker
# 'H' hexagon2 marker
# '+' plus marker
# 'x' x marker
# 'D' diamond marker
# 'd' thin_diamond marker
# '|' vline marker
# '_' hline marker
# Line Styles

# character   description
# '-'     solid line style
# '--'    dashed line style
# '-.'    dash-dot line style
# ':'     dotted line style
# Example format strings:

# 'b'    # Cblue markers with default shape
# 'or'   # Cred circles
# '-g'   # Cgreen solid line
# '--'   # dashed line with default color
# '^k:'  # Cblack triangle_up markers connected by a dotted line
# Colors

# The supported color abbreviations are the single letter codes

# character   color

# 'b' Cblue
# 'g' Cgreen
# 'r' Cred
# 'c' Ccyan
# 'm' Cmagenta
# 'y' Cyellow
# 'k' Cblack
# 'w' Cwhite


plt.grid(True)
plt.tight_layout()
plt.legend()


# plt.savefig("plot.png")
plt.show()