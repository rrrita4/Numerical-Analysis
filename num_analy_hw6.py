import numpy as np
import csv


def classic_runge_kutta(t, x, h, f, u):
    """
    经典四阶龙格-库塔方法
    :param t: 初值的t
    :param x: 初值的x
    :param h: 步长
    :param f: 方程的右端项，是一个关于t和x的函数
    :param u: 方程的解析解
    :return: no return?
    """
    M = 5 / h
    e = abs(u(t) - x)
    print('k \t t \t x \t e')
    print(0, '\t', t, '\t', x, '\t', e)
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['k', 't', 'x', 'e'])
        for k in range(1, int(M) + 1):
            F1 = h * f(t, x)
            F2 = h * f(t + 1 / 2 * h, x + 1 / 2 * F1)
            F3 = h * f(t + 1 / 2 * h, x + 1 / 2 * F2)
            F4 = h * f(t + h, x + F3)
            x = x + (F1 + 2 * F2 + 2 * F3 + F4) / 6
            t = t + h
            e = abs(u(t) - x)
            # print(k, '\t', t, '\t', x, '\t', e)
            print('{}\t{:.2f}\t{}\t{}'.format(k, t, x, e))
            writer.writerow([k, '{:.2f}'.format(t), x, e])


if __name__ == '__main__':
    lam = [-5, 5, -10]
    f = lambda t, x: lam[0] * x + np.cos(t) - lam[0] * np.sin(t)
    t0, x0 = 0, 0
    h = 0.01
    u = lambda t: np.sin(t)
    classic_runge_kutta(t0, x0, h, f, u)
