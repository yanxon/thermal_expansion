import numpy as np
import matplotlib.pyplot as plt


tim = np.loadtxt('tim.txt')
howard = np.loadtxt('output.txt')

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(tim[:,0], tim[:,1], s=10, c='b', marker='s', label='Tim')
ax1.scatter(howard[:,0], howard[:,1], s=10, c='r', marker='s', label='Howard')
plt.legend(loc='upper left')
plt.savefig('comparison.png')
