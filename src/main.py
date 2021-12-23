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
    # фазовый портрет - устойчивый фокус 0.1
    # starting_points = [
    #     (0.1, 0.1),
    #     (0.1, -0.1),
    #     (0.12, -0.075),
    #     (0.08, 0.075)
    # ]

    # фазовый портрет - центр 1
    # starting_points = [
    #     (1, 0.01),
    #     (1, 0.025),
    #     (1, 0.05),
    #     (1, 0.1)
    # ]

    # фазовый портрет - неустойчивый фокус 1.5
    # starting_points = [
    #     (1.5, 0.01),
    #     (1.5, -0.01)
    # ]

    # фазовый портрет - центр 2
    # starting_points = [
    #     (2, 0.01),
    #     (2, 0.025),
    #     (2, 0.05),
    #     (2, 0.1)
    # ]

    # фазовый портрет - устойчивый фокус 2.5
    # starting_points = [
    #     (2.5, 0.1),
    #     (2.5, -0.1),
    #     (2.53, -0.08),
    #     (2.47, 0.08)
    # ]

    # фазовый портрет - устойчивый узел 10
    starting_points = [
        (10, 0.01),
        (10, -0.01),
        (10 + 0.0001, -0.01),
        (10 - 0.0001, 0.01)
    ]

    # eulers_example - метод Эйлера для примера
    # eulers_model - метод Эйлера для модели
    # runge_kutta_example - метод Рунге-Кутта 4-го порядка для примера
    # runge_kutta_model - метод Рунге-Кутта 4-го порядка для модели
    sequence_setter = SequencesSetter(starting_points, parameter=10, precision=0.01, method_name='runge_kutta_model')

    calculate_sequences(sequence_setter)
    show_sequence()
