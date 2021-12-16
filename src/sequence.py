from methods import eulers_example, eulers_model, runge_kutta_example, runge_kutta_model
from plot import plot_sequence


def calculate_sequences(sequence_setter):
    start = sequence_setter.get_starting_points()
    parameter = sequence_setter.get_parameter()
    precision = sequence_setter.get_precision()
    method_name = sequence_setter.get_method_name()

    for j in range(len(start)):
        x_coords = [start[j][0]]
        y_coords = [start[j][1]]

        for i in range(500):
            point = (x_coords[i], y_coords[i])
            if method_name == 'eulers_example':
                x, y = eulers_example(point, precision)
            elif method_name == 'eulers_model':
                x, y = eulers_model(point, precision, parameter)
            elif method_name == 'runge_kutta_example':
                x, y = runge_kutta_example(point, precision)
            elif method_name == 'runge_kutta_model':
                x, y = runge_kutta_model(point, precision, parameter)

            x_coords.append(x)
            y_coords.append(y)

        plot_sequence(x_coords, y_coords)
