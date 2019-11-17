#!/usr/bin/env python
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = int(input('Numbers in the sequence: '))
    a = float(input('specify the first number: '))
    b = float(input('specify the second number: '))
    f = [a, b]
    for i in range(n - 2):
        f.append(f[i] + f[i + 1])
    ratio = [a / b for a, b in zip(f, f[1:])]
    plt.plot(range(n - 1), ratio)
    plt.show()
