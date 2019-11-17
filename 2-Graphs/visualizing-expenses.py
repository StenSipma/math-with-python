#!/usr/bin/env python3
"""
I always find myself asking at the end of the month, “Where did all that
money go?” I’m sure this isn’t a problem I alone face.
For this challenge, you’ll write a program that creates a bar chart for
easy comparison of weekly expenditures. The program should first ask for
the number of categories for the expenditures and the weekly total expen-
diture in each category, and then it should create the bar chart showing
these expenditures.
"""
import matplotlib.pyplot as plt


def barplot(categories, expenditures):
    ticks = range(len(categories))
    plt.barh(ticks, expenditures)
    plt.yticks(ticks, categories)
    plt.xlabel('Expenditure')
    plt.ylabel('Category')
    plt.title('Money Spend For Each Category')
    plt.axis(xmin=0)
    pass


def main():
    n = int(input('Specify a number of catogories: '))
    categories = []
    expenditures = []
    for _ in range(n):
        category = input('Specify a category: ')
        expenditure = input('The the amount of money spend on ' + category +
                            ': ')
        categories.append(category)
        expenditures.append(float(expenditure))
    barplot(categories, expenditures)
    plt.show()


if __name__ == '__main__':
    main()
