from sequence import calculate_sequences
from plot import show_sequence

if __name__ == '__main__':
    # фазовый портрет - устойчивый фокус
    starting_points = [
        (-0.5, 0.1),
        (-0.5, -0.1)
        (0.5, 250),
        (0.5, -250)
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
    #     (1.5, 200),
    #     (1.5, -200)
    # ]

    # ???
    # фазовый портрет - центр
    # starting_points = [
    #     (2, 0.00001)
    # ]

    # фазовый портрет - устойчивый фокус
    # starting_points = [
    #     (3, 150),
    #     (3, -150)
    # ]

    # фазовый портрет - устойчивый узел
    # starting_points = [
    #     (7, 150),
    #     (7, -150),
    #     (11, 150),
    #     (11, -150),
    #     (15, 150),
    #     (15, -150)
    # ]
    precision = 0.01

    # eulers_example - метод Эйлера для примера
    # eulers_model - метод Эйлера для модели
    # runge_kutta_example - метод Рунге-Кутта 4-го порядка для примера
    # runge_kutta_model - метод Рунге-Кутта 4-го порядка для модели
    method_name = 'runge_kutta_model'

    calculate_sequences(starting_points, precision, method_name)
    show_sequence()
