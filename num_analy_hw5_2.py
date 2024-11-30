import numpy as np
import warnings
import scipy

warnings.filterwarnings('error')


def romberg(f, M, a, b):
    """
    Romberg
    :param f: function f(x)
    :param M: calculate 2^M + 1 times
    :param a: left end point
    :param b: right end point
    """
    R = np.zeros((M + 1, M + 1))
    h = b - a
    R[0][0] = 1. / 2. * (b - a) * (f(a) + f(b))
    for n in range(1, M + 1):
        sum = 0.
        h = h / 2.
        for i in range(1, 2 ** (n - 1) + 1):
            sum = sum + f(a + (2 * i - 1) * h)
        R[n][0] = 1. / 2. * R[n - 1][0] + h * sum

        for m in range(1, n + 1):
            R[n][m] = R[n][m - 1] + (R[n][m - 1] - R[n - 1][m - 1]) / (4 ** m - 1)

    print(R)


if __name__ == '__main__':
    choice = input('choose the integrate:\n【1】sinx/x \n【2】(cosx-e^x)/sinx \n【3】(xe^x)^-1\n')
    M = 6
    if choice == '1':
        f1 = lambda x: np.sin(x) / x if x != 0 else 1
        a1, b1 = 0, 1
        real1 = scipy.integrate.quad(f1, a1, b1)[0]
        # M1 = 3
        romberg(f1, M, a1, b1)
        print(real1)
    elif choice == '2':
        f2 = lambda x: (np.cos(x) - np.exp(x)) / np.sin(x) if x != 0 else -1
        a2, b2 = -1, 1
        real2 = scipy.integrate.quad(f2, a2, b2)[0]
        # M2 = 4
        romberg(f2, M, a2, b2)
        print(real2)
    elif choice == '3':
        f3 = lambda x: 1 / (x * np.exp(1 / x)) if x != 0 else 0
        a3, b3 = 0, 1
        # M3 = 5
        romberg(f3, M, a3, b3)
