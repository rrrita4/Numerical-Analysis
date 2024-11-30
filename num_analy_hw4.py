import numpy as np


def phi(f, x, h):
    """
    phi(f, h) = 1/2h[f(x + h) - f(x - h)]
    :param f: f(x)
    :param x: 自变量x
    :param h: h = input
    :return: function value
    """
    return 1. / (2 * h) * (f(x + h) - f(x - h))


def richardson(f, x, h, M):
    """
    Richardson Extrapolation
    :param f: f(x)
    :param x: 自变量x
    :param h: h = 1
    :param M: M步理查森外推
    """
    D = np.zeros((M + 1, M + 1))
    for n in range(M + 1):
        D[n][0] = phi(f, x, h / 2 ** n)
    for k in range(1, M + 1):
        for n in range(k, M + 1):
            D[n][k] = D[n][k - 1] + (D[n][k - 1] - D[n - 1][k - 1]) / (4 ** k - 1)
    print(D)


if __name__ == '__main__':
    choice = input('choose the function:\n【1】log(x) \n【2】tan(x) \n【3】sin(x^2 + 1/3x)\n')
    if choice == '1':
        f = lambda x: np.log(x)
        h = 1
        M = 3
        x = 3
        richardson(f, x, h, M)
    elif choice == '2':
        f = lambda x: np.tan(x)
        h = 1
        M = 4
        x = np.arcsin(0.8)
        richardson(f, x, h, M)
    elif choice == '3':
        f = lambda x: np.sin(x ** 2 + 1. / 3 * x)
        h = 1
        M = 5
        x = 0
        richardson(f, x, h, M)
    else:
        exit()
