from sequence import calculate_sequences
from plot import show_sequence


class SequencesSetter:
    def __init__(self, points, parameter, precision, method_name):
        self.starting_points = points
        self.parameter = parameter
        self.precision = precision
        self.method_name = method_name

    def get_starting_points(self):
        return self.starting_points

    def get_parameter(self):
        return self.parameter

    def get_precision(self):
        return self.precision

    def get_method_name(self):
        return self.method_name


if __name__ == '__main__':
    # фазовый портрет - устойчивый фокус
    starting_points = [
        (0, 0.1),
        (0, -0.1)
    ]

    # фазовый портрет - центр
    # starting_points = [
    #     (1, 0.1),
    #     (1, 0.8),
    #     (1, 1.5),
    #     (1, 2.2),
    #     (1, 2.9)
    # ]

    # фазовый портрет - неустойчивый фокус
    # starting_points = [
    #     (1.5, 170),
    #     (1.5, -170)
    # ]

    # фазовый портрет - центр
    # starting_points = [
    #     (2, 0.1),
    #     (2, 0.8),
    #     (2, 1.5),
    #     (2, 2.2),
    #     (2, 2.9)
    # ]

    # фазовый портрет - устойчивый фокус
    # starting_points = [
    #     (3, 0.1),
    #     (3, -0.1)
    # ]

    # фазовый портрет - устойчивый узел
    # starting_points = [
    #     (9, 0.01),
    #     (9, -0.01),
    #     (9, 0.005),
    #     (9, -0.005)
    # ]

    # eulers_example - метод Эйлера для примера
    # eulers_model - метод Эйлера для модели
    # runge_kutta_example - метод Рунге-Кутта 4-го порядка для примера
    # runge_kutta_model - метод Рунге-Кутта 4-го порядка для модели
    precision = 0.01
    parameter = 0
    sequence_setter = SequencesSetter(starting_points, parameter, precision, 'runge_kutta_model')

    calculate_sequences(sequence_setter)
    show_sequence()
