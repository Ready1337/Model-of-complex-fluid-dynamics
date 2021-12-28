import matplotlib.pyplot as plt


def plot_sequence(x_coords, y_coords):
    plt.plot(x_coords, y_coords)


def show_sequence():
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()


def show_t_dependence():
    t = [3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14]
    param = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

    plt.plot(param, t)
    plt.scatter(param, t)

    plt.xlabel("parameter")
    plt.ylabel("T")

    plt.show()
