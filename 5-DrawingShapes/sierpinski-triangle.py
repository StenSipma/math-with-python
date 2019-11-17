from random import choice

import matplotlib.pyplot as plt


def transformation_1(x, y):
    return x / 2, y / 2


def transformation_2(x, y):
    return x / 2 + 0.5, y / 2 + 0.5


def transformation_3(x, y):
    return x / 2 + 1, y / 2


def generate_points(n, transformations):
    xs = []
    ys = []
    x, y = (0, 0)
    xs.append(x)
    ys.append(y)
    for i in range(n):
        t = choice(transformations)
        x, y = t(x, y)
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == '__main__':
    n = int(input('Number of points to generate: '))
    xs, ys = generate_points(
        n, [transformation_1, transformation_2, transformation_3])
    plt.scatter(xs, ys, marker='.')
    plt.show()
