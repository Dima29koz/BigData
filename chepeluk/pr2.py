import numpy as np
from sklearn.datasets import fetch_california_housing
import pandas as pd


def task1():
    list_ = [int(input())]
    while sum(list_) != 0:
        list_.append(int(input()))
    list_res = []
    for i in range(len(list_)):
        list_res.append(list_[i] ** 2)
    return sum(list_res)


def task2(n):
    list_res = []
    for i in range(n):
        for j in range(i+1):
            list_res.append(i+1)
    return list_res


def task3():
    matrix = np.random.rand(3, 3)
    # matrix.reshape(-1)
    matrix_res = []
    for i in range(3):
        for j in range(3):
            matrix_res.append(matrix[i][j])
    return matrix_res


def task4():
    list_a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    list_b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    dict_ab = {}.fromkeys(list_b, 0)
    for i in range(len(list_b)):
        dict_ab[list_b[i]] += list_a[i]
    return dict_ab


def foo(x):
    print(x.name, np.mean(x))


def task5():
    data = fetch_california_housing(as_frame=True)
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df = pd.concat([df, pd.DataFrame(data.target, columns=data.target_names)], axis=1)

    df.info()

    print(df.isna().sum())

    print(df.loc[(df.HouseAge > 50) & (df.Population > 2500)])

    print(max(df.MedHouseVal))

    print(min(df.MedHouseVal))

    df.apply(foo, axis=0)


def main():
    # print(task1())
    # print(task2(7))
    # print(task3())
    # print(task4())
    task5()
    return 0


if __name__ == '__main__':
    main()
