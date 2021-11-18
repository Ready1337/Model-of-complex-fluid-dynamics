from sequence import calculate_sequence

if __name__ == '__main__':
    starting_point = (1.0, 1.0)
    precision = 0.01

    # eulers_example - метод Эйлера для примера
    # eulers_model - метод Эйлера для модели
    # runge_kutta_example - метод Рунге-Кутта 4-го порядка для примера
    # runge_kutta_model - метод Рунге-Кутта 4-го порядка для модели
    method_name = 'runge_kutta_model'

    calculate_sequence(starting_point, precision, method_name)
