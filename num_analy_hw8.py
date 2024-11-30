import numpy as np


def exact_sol1(t):
    return 7 * np.sin(t) + 3 * np.cos(t)


def exact_sol2(t):
    return np.exp(t) + np.cos(t)


def finite_diff(n, a, b, alpha, beta, u, v, w):
    h = (b - a) / (n + 1)
    t = np.array([a + i * h for i in range(n + 2)])
    ai = np.array([-1 - 1. / 2. * h * w(t[i + 1]) for i in range(n)])
    di = np.array([2 + h ** 2 * v(t[i]) for i in range(1, n + 1)])
    ci = np.array([-1 + 1. / 2. * h * w(t[i]) for i in range(1, n + 1)])
    bi = np.array([-h ** 2 * u(t[i]) for i in range(1, n + 1)])
    A = np.diag(di) + np.diag(ci[:-1], 1) + np.diag(ai[1:], -1)
    rhs = bi.copy()
    rhs[0] = rhs[0] - ai[0] * alpha
    rhs[-1] = rhs[-1] - ci[-1] * beta
    x = np.linalg.solve(A, rhs)
    return x


if __name__ == '__main__':
    choice = input("选择题目a还是b:\n")
    num = [10, 20, 40, 80, 160]
    if choice == 'a':
        error_list = []
        a, b = 0, np.pi / 2
        alpha, beta = 3, 7
        u = lambda t: 0
        v = lambda t: -1
        w = lambda t: 0
        for n in num:
            sol1 = finite_diff(n, a, b, alpha, beta, u, v, w)
            t = np.array([a + i * (b - a) / (n + 1) for i in range(n + 2)])
            t = t[1:-1]
            error = [abs(sol1[i] - exact_sol1(t[i])) for i in range(n)]
            print("n: ", n)
            print("numerical sol:")
            print(sol1)
            # print("error:")
            # print(np.max(error))
            error_list.append(np.max(error))
        print("error: ", error_list)
        order = [np.log(error_list[i - 1] / error_list[i]) / np.log(2) for i in range(1, 5)]
        print("order: ", order)
    elif choice == 'b':
        error_list = []
        a, b = 0, 1
        alpha, beta = 2, np.e + np.cos(1)
        u = lambda t: 2 * np.exp(t)
        v = lambda t: -1
        w = lambda t: 0
        for n in num:
            sol2 = finite_diff(n, a, b, alpha, beta, u, v, w)
            t = np.array([a + i * (b - a) / (n + 1) for i in range(n + 2)])
            t = t[1:-1]
            error = [abs(sol2[i] - exact_sol2(t[i])) for i in range(n)]
            print("n: ", n)
            print("numerical sol:")
            print(sol2)
            # print("error:")
            # print(np.max(error))
            error_list.append(np.max(error))
        print("error: ", error_list)
        order = [np.log(error_list[i - 1] / error_list[i]) / np.log(2) for i in range(1, 5)]
        print("order: ", order)
