# %matplotlib inline
# Above line allows plot to show inline in ipython
import matplotlib.pyplot as plt
# plotting a line
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))

#start new plot
plt.close()

# scatter-plot points
x = np.random.normal(size=500)
y = np.random.normal(size=500)
plt.scatter(x, y)

#Vew
#http://matplotlib.org/mpl_examples/pylab_examples/ellipse_collection.py
