import math
import matplotlib.pyplot as plt


# 函数f(x)
def f(x):
    """
    :param x: double, 函数自变量
    :return:  double, 函数值
    """
    assert -5 <= x <= 5
    return 1 / (1 + x ** 2)


def f1(x):
    """
    :param x: double, 函数自变量
    :return:  double, 函数值
    """
    assert -1 <= x <= 1
    return 1 / (1 + 25 * x ** 2)


# 拉格朗日插值函数
def Lagrange_interpolation(N, a, x):
    """
    :param N: int, 插值点个数
    :param a: double[], 插值点的值
    :param x: double, 自变量
    :return: double, 插值函数值
    """

    assert len(a) == N + 1
    fx = 0
    for m in range(N + 1):
        tmp = 1
        for j in range(m):
            tmp = tmp * (x - a[j]) / (a[m] - a[j])
        for j in range(m + 1, N + 1):
            tmp = tmp * (x - a[j]) / (a[m] - a[j])
        fx = fx + tmp * f(a[m])
    return fx


def Newton_Interpolation(N, a, x):
    """
    :param N: int, 插值点个数
    :param a: double[], 插值点的值
    :param x: double, 自变量
    :return: double, 插值函数值
    """

    assert len(a) == N + 1
    y = [f1(a[i]) for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(N, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (a[j] - a[j - i])
    fx = y[N]
    for i in range(N, 0, -1):
        fx = y[i - 1] + (x - a[i - 1]) * fx
    return fx


if __name__ == '__main__':
    N = [5, 10, 20, 40]
    Max1, Max2 = 0, 0
    choice = input("请输入要选择的方法:【1】Lagrange\n【2】Newton\n")
    if choice == "1":
        for N_i in N:
            a1 = list()
            a2 = list()
            for i in range(N_i + 1):
                a1.append(5 - (10 * i) / N_i)
                a2.append(-5 * math.cos((2 * i + 1) * math.pi / (2 * N_i + 2)))
            Max1, Max2 = 0, 0
            for k in range(101):
                Max1 = max(Max1, abs(f(k / 10 - 5) - Lagrange_interpolation(N_i, a1, k / 10 - 5)))
                Max2 = max(Max2, abs(f(k / 10 - 5) - Lagrange_interpolation(N_i, a2, k / 10 - 5)))
            print("N = ", N_i)
            print("Max Error of grid 1 : ", Max1)
            print("Max Error of grid 2 : ", Max2)
            # 画图
            if N_i == 10:
                x = [k / 10 - 5 for k in range(101)]
                y1 = [f(x[i]) for i in range(101)]
                y2 = [Lagrange_interpolation(N_i, a1, x[i]) for i in range(101)]
                y3 = [Lagrange_interpolation(N_i, a2, x[i]) for i in range(101)]
                plt.figure()
                plt.plot(x, y1, color='red', label='f(x)')
                plt.plot(x, y2, color='blue', label='interpolation with uniform nodes')
                plt.plot(x, y3, color='green', label='interpolation with Chebyshev point')
                plt.legend()
                plt.show()
    if choice == "2":
        for N_i in N:
            a1 = list()
            a2 = list()
            for i in range(N_i + 1):
                a1.append(1 - (2 * i) / N_i)
                a2.append(-1 * math.cos((2 * i + 1) * math.pi / (2 * N_i + 2)))
            Max1, Max2 = 0, 0
            for k in range(101):
                Max1 = max(Max1, abs(f1(k / 50 - 1) - Newton_Interpolation(N_i, a1, k / 50 - 1)))
                Max2 = max(Max2, abs(f1(k / 50 - 1) - Newton_Interpolation(N_i, a2, k / 50 - 1)))
            print("N = ", N_i)
            print("Max Error of grid 1 : ", Max1)
            print("Max Error of grid 2 : ", Max2)
            # 画图
            if N_i == 20:
                x = [k / 50 - 1 for k in range(101)]
                y1 = [f1(x[i]) for i in range(101)]
                y2 = [Newton_Interpolation(N_i, a1, x[i]) for i in range(101)]
                y3 = [Newton_Interpolation(N_i, a2, x[i]) for i in range(101)]
                plt.figure()
                plt.plot(x, y1, color='red', label='f(x)')
                plt.plot(x, y2, color='blue', label='interpolation with uniform nodes')
                plt.plot(x, y3, color='green', label='interpolation with Chebyshev point')
                plt.legend()
                plt.show()
