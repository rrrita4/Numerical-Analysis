import numpy as np
import scipy


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


def gauss(f, a, b):
    """
    3点高斯法则
    :param f: function f(x)
    :param a: left end point
    :param b: right end point
    :return: value of Integrate[f(x), {x, a, b}]
    """
    h = (b - a) / 2
    g = lambda x: f(((b - a) * x + b + a) / 2)
    result = 5. / 9. * g(-np.sqrt(3. / 5.)) + 8. / 9. * g(0) + 5. / 9. * g(np.sqrt(3. / 5.))
    return result * h


if __name__ == '__main__':
    choice = input("请输入要选择的方法: \n【1】复化梯形\n【2】复化3点Gauss\n")
    f1 = lambda x: np.exp(-x ** 2)
    f2 = lambda x: 1 / (1 + x ** 2)
    f3 = lambda x: 1 / (2 + np.cos(x))
    a1, b1 = 0, 1
    a2, b2 = 0, 4
    a3, b3 = 0, 2 * np.pi
    error_list1, ord1 = [], []
    error_list2, ord2 = [], []
    error_list3, ord3 = [], []
    real1, real2, real3 = scipy.integrate.quad(f1, 0, 1)[0], np.arctan(4), 2 * np.pi / np.sqrt(3)  # 第一个精确值不知道
    if choice == '1':
        for k in range(1, 8):
            n = 2 ** k
            error_list1.append(abs(real1 - trapezoid(n, f1, a1, b1)))
        print(error_list1)
        for k in range(6):
            ord1.append(np.log(error_list1[k] / error_list1[k + 1]) / np.log(2))
        print(ord1)
        for k in range(1, 8):
            n = 2 ** k
            error_list2.append(abs(real2 - trapezoid(n, f2, a2, b2)))
        print(error_list2)
        for k in range(6):
            ord2.append(np.log(error_list2[k] / error_list2[k + 1]) / np.log(2))
        print(ord2)
        for k in range(1, 8):
            n = 2 ** k
            error_list3.append(abs(real3 - trapezoid(n, f3, a3, b3)))
        print(error_list3)
        for k in range(6):
            ord3.append(np.log(error_list3[k] / error_list3[k + 1]) / np.log(2))
        print(ord3)
    elif choice == '2':
        for k in range(1, 8):
            n = 2 ** k
            h1 = (b1 - a1) / n
            x1_list = [a1 + i * h1 for i in range(n + 1)]
            result1 = 0.
            for i in range(n):
                result1 = result1 + gauss(f1, a1 + i * h1, a1 + (i + 1) * h1)
            error_list1.append(abs(real1 - result1))
        print('error: ', error_list1)
        for k in range(6):
            ord1.append(np.log(error_list1[k] / error_list1[k + 1]) / np.log(2))
        print('order: ', ord1)

        for k in range(1, 8):
            n = 2 ** k
            h2 = (b2 - a2) / n
            x2_list = [a2 + i * h2 for i in range(n + 1)]
            result2 = 0.
            for i in range(n):
                result2 = result2 + gauss(f2, a2 + i * h2, a2 + (i + 1) * h2)
            error_list2.append(abs(real2 - result2))
        print('error: ', error_list2)
        for k in range(6):
            ord2.append(np.log(error_list2[k] / error_list2[k + 1]) / np.log(2))
        print('order: ', ord2)

        for k in range(1, 8):
            n = 2 ** k
            h3 = (b3 - a3) / n
            x3_list = [a3 + i * h3 for i in range(n + 1)]
            result3 = 0.
            for i in range(n):
                result3 = result3 + gauss(f3, a3 + i * h3, a3 + (i + 1) * h3)
            error_list3.append(abs(real3 - result3))
        print('error: ', error_list3)
        for k in range(6):
            ord3.append(np.log(error_list3[k] / error_list3[k + 1]) / np.log(2))
        print('order: ', ord3)
