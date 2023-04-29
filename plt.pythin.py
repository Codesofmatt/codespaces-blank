# creating 3d plot using matplotlib
# in python
# for creating a responsive plot
# %matplotlib qt
import matplotlib.pyplot as plt

import numpy as np
from mpl_toolkits import mplot3d
fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection='3d')

np.random.seed(3)
y = np.random.random(100)
x = np.random.random(100)
z = np.random.random(100)
ax.scatter3D(x, y, z, color='red')
ax.set_title("3D scatterplot", pad=25, size=15)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()