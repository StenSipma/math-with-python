import matplotlib.pyplot as plt
from matplotlib import animation

line, = plt.plot([], [], marker='.', ls='')
xs = []
ys = []


def transform(x, y):
    return y + 1 - 1.4 * x * x, 0.3 * x


def update(i):
    x, y = transform(xs[-1], ys[-1])
    xs.append(x)
    ys.append(y)
    line.set_data(xs, ys)
    return line,


def init():
    ax = plt.axes(xlim=[-5, 5], ylim=[-10, 0])
    ax.set_aspect('equal')
    xs.append(0)
    ys.append(0)
    line.set_data(xs, ys)
    return line,


if __name__ == '__main__':
    n = int(input('Number of points / iterations to generate: '))
    fig = plt.gcf()
    amin = animation.FuncAnimation(fig,
                                   update,
                                   init_func=init,
                                   frames=n,
                                   interval=10,
                                   blit=True)
    plt.show()
