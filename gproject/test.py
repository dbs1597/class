import numpy as np
import matplotlib.pyplot as plt
 

def relu(x):
    return np.maximum(x, 0)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.arange(-10.0, 10.0, 0.1)
y = relu(x)
z = sigmoid(x)
# plt.plot(x, y)
plt.plot(x, z)
plt.show()
