import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
   #return np.sin(x) + x + x * np.sin(x)
   #return (np.exp(1)*2)**2/2*(x-2)*np.exp(-1*(x-2)**2/2**2)
   return (np.exp(-x**2))

x = np.linspace(-10, 10, 1000)

#plt.plot(x, f(x), color='red')
sns.lineplot(x,f(x))

plt.show()