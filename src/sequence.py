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

        for i in range(10000):
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


def find_cycle(sequence_setter, epsilon):
    start = sequence_setter.get_starting_points()
    parameter = sequence_setter.get_parameter()
    precision = sequence_setter.get_precision()

    for j in range(len(start)):
        x_coords = [start[j][0]]
        y_coords = [start[j][1]]

        for i in range(10000):
            point = (x_coords[i], y_coords[i])
            x, y = runge_kutta_model(point, precision, parameter)

            for z in range(len(x_coords)):
                if abs(x_coords[z] - x) < epsilon and abs(y_coords[z] - y) < epsilon:
                    print('cycle ok')
                    print(f'#1: {(x, y)}')
                    print(f'#2: {(x_coords[z], y_coords[z])}')
                    print(f'start = {z}')
                    print(f'end = {i}')
                    plot_sequence(x_coords, y_coords)
                    return

            x_coords.append(x)
            y_coords.append(y)

        plot_sequence(x_coords, y_coords)
