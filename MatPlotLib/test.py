import numpy as np
import matplotlib.pyplot as plt
import math

x_axis = np.arange(1, 500)
y = [math.log(x) for x in x_axis]

plt.plot(x_axis, y)
plt.show()