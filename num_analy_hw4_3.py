import numpy as np


# 拉格朗日插值基函数的积分
def int_lagrange_base(f, n, a):
    """
    计算拉格朗日插值基函数的积分
    :param f: function f(x)
    :param n: int 插值节点0到n
    :param a: list 所有结点
    :return: value of int
    """
    A = np.ones((n + 1, n + 1))
    b = np.ones(n + 1)
    for i in range(n + 1):
        b[i] = 1 / (i + 1) * (1 ** (i + 1) - (-1) ** (i + 1))
        for j in range(n + 1):
            A[i][j] = a[j] ** i
    coef = np.linalg.solve(A, b)
    result = 0
    for i in range(n + 1):
        result = result + f(a[i]) * coef[i]
    return result


if __name__ == '__main__':
    f = lambda x: 1 / (1 + 25 * x ** 2)
    real = 0.4 * np.arctan(5)  # scipy.integrate.quad(f, -1, 1)[0]
    error_list1 = []
    error_list2 = []
    N = [i for i in range(5, 41, 5)]
    for N_i in N:
        a1 = [1 - (2 * i) / N_i for i in range(N_i + 1)]
        a2 = [-1 * np.cos((i + 1) * np.pi / (N_i + 2)) for i in range(N_i + 1)]
        error_list1.append(abs(real - int_lagrange_base(f, N_i, a1)))
        error_list2.append(abs(real - int_lagrange_base(f, N_i, a2)))
    print(error_list1)
    print(error_list2)
