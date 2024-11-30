import numpy as np

a_list = [16 / 135, 0, 6656 / 12825, 28561 / 56430, -9 / 50, 2 / 55]
minus = [1 / 360, 0, -128 / 4275, -2197 / 75240, 1 / 50, 2 / 55]
b_list = [a_list[i] - minus[i] for i in range(6)]
c_list = [0, 1 / 4, 3 / 8, 12 / 13, 1, 1 / 2]
d_mat = [[0, 0, 0, 0, 0],
         [1 / 4, 0, 0, 0, 0],
         [3 / 32, 9 / 32, 0, 0, 0],
         [1932 / 2197, -7200 / 2197, 7296 / 2197, 0, 0],
         [439 / 216, -8, 3680 / 513, -845 / 4104, 0],
         [-8 / 27, 2, -3544 / 2565, 1859 / 4104, -11 / 40]]


def f(x, y):
    return np.exp(y * x) + np.cos(y - x)


def rkf45(t, x, h, delta, p):
    t_list = []
    x_list = []
    x_list.append(3)
    t_list.append(1)
    k = 0
    e = 0
    print('k \t t \t x \t e')
    while not np.isnan(x) and not np.isnan(e) and not np.isinf(x) and not np.isinf(e):
        F = [0 for i in range(6)]
        for i in range(6):
            sum = 0
            for j in range(i):
                sum += d_mat[i][j] * F[j]
            F[i] = h * f(t + c_list[i] * h, x + sum)
        sum = 0
        for i in range(6):
            sum += a_list[i] * F[i]
        x += sum
        x_list.append(x)
        e = 0
        for i in range(6):
            e += minus[i] * F[i]
        t += h
        t_list.append(t)
        k += 1
        print('{}\t{}\t{}\t{}'.format(k, t, x, e))
        h = 0.9 * h * (delta / abs(e)) ** (1 / (1 + p))
    return t_list, x_list


if __name__ == '__main__':
    t_list, x_list = rkf45(t=1, x=3, h=0.01, delta=1e-6, p=5)
    t = input("please input a float number ranging from 1 to 1.045463:\n")
    t = float(t)
    for i in range(len(t_list) - 1):
        if t_list[i] <= t < t_list[i + 1]:
            result = (x_list[i + 1] - x_list[i]) / (t_list[i + 1] - t_list[i]) * (t - t_list[i]) + x_list[i]
            print(result)
            break
