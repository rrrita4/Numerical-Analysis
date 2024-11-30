import numpy as np
import math
import matplotlib.pyplot as plt


def LinearSpline(x, a, N):
    """
    一次分片线性样条
    :param x: double, 自变量
    :param a: list, 插值结点
    :param N: 结点个数 - 1
    :return: 插值函数在x处的函数值
    """
    assert len(a) == N + 1 and 0 <= x <= 1
    index = np.array([x < xi for xi in a])
    index = index + 0
    i = np.nonzero(index)[0][0]
    return (math.exp(a[i]) - math.exp(a[i - 1])) * (x - a[i - 1]) / (a[i] - a[i - 1]) + math.exp(a[i - 1])


def TripleSpline(x, a, N):
    """
    三次样条插值，S'(0) = 1, S'(1) = e
    :param x: double, 自变量
    :param a: list, 插值结点
    :param N: 结点个数 - 1
    :return: 插值多项式的函数值
    """
    assert len(a) == N + 1 and 0 <= x <= 1
    # 右端项
    b, v = [], []
    for i in range(N):
        b.append(6 * N * (math.exp(a[i + 1]) - math.exp(a[i])))
    for i in range(N - 1):
        v.append(b[i + 1] - b[i])
    v = np.array(v)
    v = np.insert(v, 0, 6 * N * (N * (math.exp(a[1]) - math.exp(a[0])) - 1))
    v = np.append(v, 6 * N * (math.e - (N * (math.exp(a[N]) - math.exp(a[N - 1])))))
    v.reshape(v.shape[0], 1)
    # 系数矩阵
    cof_mat = np.diag((4 / N) * np.ones(N + 1)) + np.diag((1 / N) * np.ones(N), k=1) + np.diag(
        (1 / N) * np.ones(N),
        k=-1)
    cof_mat[0][0], cof_mat[N][N] = 2, 2
    cof_mat[0][1], cof_mat[N][N - 1] = 1, 1
    # print(cof_mat)
    solve = np.linalg.solve(cof_mat, v)
    # m0 = (6 * N * (N * (math.exp(a[1]) - math.exp(a[0])) - 1) - solve[0]) / 2
    # solve = np.insert(solve, 0, m0)
    # solve = np.append(solve, (6 * N * (math.e - (N * (math.exp(a[N]) - math.exp(a[N - 1])))) - solve[N - 1]) / 2)
    # 求出M_n后可以解插值多项式
    index = np.array([x < xi for xi in a])
    index = index + 0
    i = np.nonzero(index)[0][0]
    A = (N / 6) * (solve[i] - solve[i - 1])
    B = solve[i - 1] / 2
    C = - solve[i] / (6 * N) - solve[i - 1] / (3 * N) + N * (math.exp(a[i]) - math.exp(a[i - 1]))
    return math.exp(a[i - 1]) + (x - a[i - 1]) * (C + (x - a[i - 1]) * (B + (x - a[i - 1]) * A))


if __name__ == '__main__':
    N = [5, 10, 20, 40]
    max_list = []
    choice = input("选择你要用的方法:\n【1】分片线性样条插值\n【2】三次样条插值\n")
    for Ni in N:
        a, mid = [], []
        Max = 0
        for i in range(Ni + 1):
            a.append(i / Ni)  # 插值结点
        for i in range(Ni):
            mid.append((a[i] + a[i + 1]) / 2)  # 结点的中点
        for middle in mid:
            if choice == '1':
                Max = max(Max, abs(math.exp(middle) - LinearSpline(middle, a, Ni)))
            elif choice == '2':
                Max = max(Max, abs(math.exp(middle) - TripleSpline(middle, a, Ni)))
            else:
                print("请在1和2里面选\n")
                exit()
        max_list.append(Max)
    Ord = []
    for i in range(1, 4):
        Ord.append(np.log(max_list[0] / max_list[i]) / np.log(N[i] / N[0]))
    print("error: ", max_list)
    print("order: ", Ord)
