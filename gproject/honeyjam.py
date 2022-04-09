from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def a():
    x = np.arange(-5, 5, 0.5)
    y = np.arange(-5, 5, 0.5)
    X, Y = np.meshgrid(x, y)
    Z = X ** 2 + Y ** 2

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z)
    plt.show()


def b():
    x = np.arange(-5, 5, 0.5)
    y = np.arange(-5, 5, 0.5)
    X, Y = np.meshgrid(x, y)
    U = -2 * X
    V = -2 * Y

    plt.figure()
    Q = plt.quiver(X, Y, U, V, units='width')
    plt.show()


b()