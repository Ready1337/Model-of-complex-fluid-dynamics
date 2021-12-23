def f_example(x, y):
    return y


def g_example(x, y):
    return -x


def eulers_example(point, precision):
    x_m = point[0]
    y_m = point[1]
    h = precision

    x_m_next = x_m + h * f_example(x_m, y_m)
    y_m_next = y_m + h * g_example(x_m, y_m)

    return x_m_next, y_m_next


def runge_kutta_example(point, precision):
    x_m = point[0]
    y_m = point[1]
    h = precision

    k1 = h * f_example(x_m, y_m)
    l1 = h * g_example(x_m, y_m)

    k2 = h * f_example(x_m + k1 / 2, y_m + l1 / 2)
    l2 = h * g_example(x_m + k1 / 2, y_m + l1 / 2)

    k3 = h * f_example(x_m + k2 / 2, y_m + l2 / 2)
    l3 = h * g_example(x_m + k2 / 2, y_m + l2 / 2)

    k4 = h * f_example(x_m + k3, y_m + l3)
    l4 = h * g_example(x_m + k3, y_m + l3)

    x_m_next = x_m + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    y_m_next = y_m + 1 / 6 * (l1 + 2 * l2 + 2 * l3 + l4)

    return x_m_next, y_m_next


def f(x, y):
    return y


def g(x, y, param):
    return (-x**2 + 3*x - 2) * y - 4*x + 4*param


def eulers_model(point, precision, param):
    x_m = point[0]
    y_m = point[1]
    h = precision

    x_m_next = x_m + h * f(x_m, y_m)
    y_m_next = y_m + h * g(x_m, y_m, param)

    return x_m_next, y_m_next


def runge_kutta_model(point, precision, param):
    x_m = point[0]
    y_m = point[1]
    h = precision

    k1 = h * f(x_m, y_m)
    l1 = h * g(x_m, y_m, param)

    k2 = h * f(x_m + k1 / 2, y_m + l1 / 2)
    l2 = h * g(x_m + k1 / 2, y_m + l1 / 2, param)

    k3 = h * f(x_m + k2 / 2, y_m + l2 / 2)
    l3 = h * g(x_m + k2 / 2, y_m + l2 / 2, param)

    k4 = h * f(x_m + k3, y_m + l3)
    l4 = h * g(x_m + k3, y_m + l3, param)

    x_m_next = x_m + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    y_m_next = y_m + 1/6 * (l1 + 2*l2 + 2*l3 + l4)

    return x_m_next, y_m_next
