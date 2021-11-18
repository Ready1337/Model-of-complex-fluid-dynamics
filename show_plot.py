import matplotlib.pyplot as plt


def show(x_coords, y_coords):
    plt.plot(x_coords, y_coords)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
