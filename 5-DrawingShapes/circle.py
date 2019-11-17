import matplotlib.pyplot as plt


def make_circle(coordinate, radius):
    circle_patch = plt.Circle(coordinate, radius)
    return circle_patch


def add_patch(patch):
    axes = plt.gca()
    axes.add_patch(patch)


if __name__ == '__main__':
    circle = make_circle((0, 1), 1)
    add_patch(circle)
    plt.axis('scaled')
    plt.show()
