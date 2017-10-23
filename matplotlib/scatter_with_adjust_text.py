import numpy as np
def calc(ori, verbose=0):
    a = np.array(ori)*10
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    print(asum, ent)
    return asum ,ent

res = []
labels = []
ori = [5610, 13857]
res.append(calc(ori))
labels.append('original')
ori = [ 8174.,  9431.]
res.append(calc(ori))
labels.append('negative step function')
ori = [ 6622.,  11906.]
res.append(calc(ori))
labels.append('step function')
ori = [ 6142.,  12997.]
res.append(calc(ori))
labels.append('exponential')

res = np.array(res)

import matplotlib.pyplot as plt

plt.xlabel('sum of resources consumed by all agents(normalized)')
plt.ylabel('entropy')
x, y = res[:,0], res[:,1]
x = (x-min(x))/(max(x) - min(x))
print(y)

# calculate polynomial
z = np.polyfit(x, y, 2)
f = np.poly1d(z)
print(f)
# calculate new x's and y's
x_new = np.linspace(min(x), max(x), 50)
y_new = f(x_new)
fit_line, = plt.plot(x_new, y_new, '-.', color='g' )
plt.legend([fit_line], ['fitted curve'])

plt.scatter(x, y)
from adjustText import adjust_text
texts = []
for i in range(4):
    texts.append(plt.text(x[i], y[i], labels[i]))
    #plt.annotate(labels[i], (x[i], y[i]), (x[i]+0.005, y[i]+0.005))
adjust_text(texts)

plt.savefig('fuck.png')
plt.show()
input()
