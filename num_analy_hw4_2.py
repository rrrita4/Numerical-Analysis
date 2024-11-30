import numpy as np


def simpson(n, f, a, b):
    """
    复化Simpson积分公式
    :param n: int even
    :param f: function f(x)
    :param a: left end point
    :param b: right end point
    :return: value of Integrate[f(x), {x, a, b}]
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    result = f(x[0]) + f(x[n]) + 4 * f(x[1])
    for i in range(2, int(n / 2) + 1):
        result = result + 2 * f(x[2 * i - 2]) + 4 * f(x[2 * i - 1])
        # result = result + f(x[2 * i - 2]) + 4 * f(x[2 * i - 1]) + f(x[2 * i])
    return result * h / 3


def trapezoid(n, f, a, b):
    """
    复化梯形法则
    :param n: divide the interval
    :param f: function f(x)
    :param a: left end point
    :param b: right end point
    :return: value of Integrate[f(x), {x, a, b}]
    """
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, int(n)):
        result = result + 2 * f(a + i * h)
    return result * h / 2


if __name__ == '__main__':
    choice = input("请输入要选择的方法: \n【1】Simpson\n【2】梯形\n")
    f = lambda x: np.sin(x)
    a = 0
    b = 4
    real = 1 - np.cos(4)
    error_list = []
    ord = []
    if choice == '1':
        for k in range(1, 13):
            n = 2 ** k
            error_list.append(abs(real - simpson(n, f, a, b)))
        print(error_list)
        for k in range(11):
            ord.append(np.log(error_list[k] / error_list[k + 1]) / np.log(2))
        print(ord)
    elif choice == '2':
        for k in range(1, 13):
            n = 2 ** k
            error_list.append(abs(real - trapezoid(n, f, a, b)))
        print(error_list)
        for k in range(11):
            ord.append(np.log(error_list[k] / error_list[k + 1]) / np.log(2))
        print(ord)
