import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing


def task1():
    numbers = []
    n2 = []
    print("Вводите числа, пока их сумма не равна 0")
    while not len(numbers) or sum(numbers) != 0:
        numbers.append(int(input('Введите очередное целое цисло: ')))
        n2.append(numbers[-1]**2)

    # sum_sq = sum([number ** 2 for number in numbers])
    print(f"Сумма квадратов чисел равна: {sum(n2)}")


def task2(n: int):
    print(*prep_task2(n)[:n])


def prep_task2(n):
    res = []
    for i in range(1, n+1):
        for e in range(1, i+1):
            res.append(i)
    return res


def task3(n: int, m: int):
    matrix = np.random.rand(n, m)
    res = []
    for row in matrix:
        for item in row:
            res.append(item)

    print(matrix)
    print(res)


def task4(a: list, b: list):
    res = {}
    for idx, elem in enumerate(b):
        if elem not in res:
            res |= {elem: 0}
        res[elem] += a[idx]
    print(res)


def main():
    print('задание 1:')
    task1()
    print('задание 2:')
    task2(7)
    print('задание 3:')
    task3(3, 4)
    print('задание 4:')
    task4([1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2], ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a'])


if __name__ == "__main__":
    main()
