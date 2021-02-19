import matplotlib
import matplotlib.pyplot as plt

plt.plot(x,y)
matplotlib.pyplot.plot()
plt.scatter(x,y)
plt.hist(x)
plt.vlines(x, y_min, y_max)
plt.hlines(y, x_min, x_max)

# 

plt.show()
plt.savefig('file.jpg')

# 

plt.close()