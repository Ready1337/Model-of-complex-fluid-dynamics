from sequence import calculate_sequences, find_cycle
from plot import show_sequence, show_t_dependence


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
    #     (1.5, 3)
    # ]

    starting_points = [
        # (1.0994022877585143, -1.3004596127658992) # 1.1   0.001
        # (1.2006580521359789, -1.7352321631882393) # 1.2   0.001
        # (0.7115819519055993, 1.2709935477389327)  # 1.3   0.01
        # (1.40824472794171, 1.9018139579166402)    # 1.4   0.01
        # (1.4816971580550782, 1.99519100039137)  # 1.5   0.01
        # (1.6090103469033865, 2.0234570512169685)  # 1.6   0.01
        # (1.7036760893009686, 1.9512500153349224)  # 1.7   0.01
        # (1.7990104300997234, 1.744160174889162)   # 1.8   0.01
        # (1.900597712241486, 1.3004596127659003)   # 1.9   0.001
    ]

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
    # starting_points = [
    #     (10, 0.1),
    #     (10, -0.1),
    #     (9.9, 0.1),
    #     (9.9, -0.1),
    #     (9.95, 0.1),
    #     (9.95, -0.1)
    # ]

    # eulers_example - метод Эйлера для примера
    # eulers_model - метод Эйлера для модели
    # runge_kutta_example - метод Рунге-Кутта 4-го порядка для примера
    # runge_kutta_model - метод Рунге-Кутта 4-го порядка для модели
    sequence_setter = SequencesSetter(starting_points, parameter=1.9, precision=0.01, method_name='runge_kutta_model')

    #calculate_sequences(sequence_setter)
    #find_cycle(sequence_setter, 0.001)

    # точки предельных циклов
    # (1.0994022877585143, -1.3004596127658992) # 1.1   0.001
    # (1.2006580521359789, -1.7352321631882393) # 1.2   0.001
    # (0.7115819519055993, 1.2709935477389327)  # 1.3   0.01
    # (1.40824472794171, 1.9018139579166402)    # 1.4   0.01
    # (1.4909152575156248, 1.9945702681119177)  # 1.5   0.01
    # (1.6090103469033865, 2.0234570512169685)  # 1.6   0.01
    # (1.7036760893009686, 1.9512500153349224)  # 1.7   0.01
    # (1.7990104300997234, 1.744160174889162)   # 1.8   0.01
    # (1.900597712241486, 1.3004596127659003)   # 1.9   0.001

    #show_sequence()
    #show_t_dependence()
