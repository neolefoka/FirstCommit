import matplotlib.pyplot as plt
import numpy as np

# My first plot
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
