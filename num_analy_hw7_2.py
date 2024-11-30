import numpy as np


def f(x, y):
    return (x - np.exp(-x)) / (y + np.exp(y))


def a_b(h, prev_x, prev_y):
    """
    :param prev_x: 数组，放xn, xn-1, xn-2, xn-3, xn-4
    :return: xn+1
    """
    return prev_y[0] + h / 720 * (1901 * f(prev_x[0], prev_y[0]) - 2774 * f(prev_x[1], prev_y[1]) + 2616 * f(prev_x[2],
                                                                                                             prev_y[
                                                                                                                 2]) - 1274 * f(
        prev_x[3], prev_y[3]) + 251 * f(prev_x[4], prev_y[4]))


def rk4(f, x, y, h):
    F1 = h * f(x, y)
    F2 = h * f(x + 1. / 2. * h, y + 1. / 2. * F1)
    F3 = h * f(x + 1. / 2. * h, y + 1. / 2. * F2)
    F4 = h * f(x + h, y + F3)
    return y + 1. / 6. * (F1 + 2 * F2 + 2 * F3 + F4)


if __name__ == '__main__':
    real = -1
    n_list = [2 ** k for k in range(3, 9)]
    x0 = 0
    y0 = 0
    error = []
    order = []
    for n in n_list:
        h = 1. / float(n)
        x_list = np.array([i * h for i in range(n + 1)])
        # print(x_list)
        y1 = rk4(f, x0, y0, h)
        y2 = rk4(f, x_list[1], y1, h)
        y3 = rk4(f, x_list[2], y2, h)
        y4 = rk4(f, x_list[3], y3, h)
        prev_y = np.array([y4, y3, y2, y1, y0])
        prev_x = x_list[:5]
        for k in range(5, n + 2):
            prev_y = np.insert(prev_y, 0, a_b(h, prev_x[::-1], prev_y))
            prev_x = x_list[k - 4: k + 1]
        error.append(abs(prev_y[1] - real))
    order = [np.log(error[i] / error[i + 1]) / np.log(2) for i in range(len(error) - 1)]
    print("error: ", error)
    print("order: ", order)
