#!/usr/bin/env python3
"""
Our multiplication table generator is cool, but it prints only the first 10
multiples. Enhance the generator so that the user can specify both the number
and up to which multiple. For example, I should be able to input that I want
to see a table listing the first 15 multiples of 9.
"""

_fmt_string = '{a:>{a_w}} x {n:>{n_w}d} = {result:>{r_w}d}'


def multiplication_table(a, n):
    """
    Creates a multiplication table for 'a'
    showing 'n' multiples of 'a'.
    """
    n_w = len(str(n))
    r_w = len(str(a * n))
    for i in range(1, n + 1):
        print(
            _fmt_string.format(a=a,
                               n=i,
                               result=a * i,
                               a_w=len(str(a)),
                               n_w=n_w,
                               r_w=r_w))


def correct_input(n):
    try:
        n = int(n)
    except ValueError:
        return False
    return True


def main():
    a = input('Please give an integer a: ')
    n = input('Please give an integer n: ')
    if not (correct_input(a) and correct_input(n)):
        print('Please give correct integers...')
        exit(1)
    a = int(a)
    n = int(n)
    multiplication_table(a, n)


if __name__ == '__main__':
    main()
