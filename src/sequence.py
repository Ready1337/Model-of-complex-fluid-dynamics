from methods import eulers_example, eulers_model, runge_kutta_example, runge_kutta_model
from plot import plot_sequence


def calculate_sequences(start, precision, method_name):
    for j in range(len(start)):
        x_coords = [start[j][0]]
        y_coords = [start[j][1]]

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

        plot_sequence(x_coords, y_coords)
