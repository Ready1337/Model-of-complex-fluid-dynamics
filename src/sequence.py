from methods import eulers_example, eulers_model, runge_kutta_example, runge_kutta_model
from show_plot import show


def calculate_sequence(start, precision, method_name):
    x_coords = [start[0]]
    y_coords = [start[1]]

    for i in range(10000):
        if method_name == 'eulers_example':
            x, y = eulers_example(x_coords[i], y_coords[i], precision)
        elif method_name == 'eulers_model':
            x, y = eulers_model(x_coords[i], y_coords[i], precision)
        elif method_name == 'runge_kutta_example':
            x, y = runge_kutta_example(x_coords[i], y_coords[i], precision)
        elif method_name == 'runge_kutta_model':
            x, y = runge_kutta_model(x_coords[i], y_coords[i], precision)

        x_coords.append(x)
        y_coords.append(y)

    show(x_coords, y_coords)
