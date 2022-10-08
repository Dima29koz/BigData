import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sts
from numpy import mean
import scipy.stats as st
from scipy.stats import sem
from scipy.stats import t
import statsmodels.api as sm
from scipy.stats import kstest


def task1(df):
    print(df.describe())
    return 0


def task2(df):
    fig, axs = plt.subplots(1, 4, figsize=(12, 5))
    axs[0].hist(df.age, bins=20)
    axs[0].set_title('age')
    axs[1].hist(df.bmi, bins=20)
    axs[1].set_title('bmi')
    axs[2].hist(df.children, bins=20)
    axs[2].set_title('children')
    axs[3].hist(df.charges, bins=20)
    axs[3].set_title('charges')
    plt.show()
    return 0


def task3(df):
    mean_bmi = np.mean(df.bmi)
    moda_bmi = np.array(sts.mode(df.bmi, keepdims=False)).tolist()
    med_bmi = np.median(df.bmi)
    print("bmi: ", mean_bmi, "|", moda_bmi[0], "|", med_bmi)
    mean_charges = np.mean(df.charges)
    moda_charges = np.array(sts.mode(df.charges, keepdims=False)).tolist()
    med_charges = np.median(df.charges)
    print("charges: ", mean_charges, "|", moda_charges[0], "|", med_charges)

    list_mmm = [[mean_bmi, mean_charges], [moda_bmi[0], moda_charges[0]], [med_bmi, med_charges]]
    data_list_mmm = pd.DataFrame(list_mmm)
    print(data_list_mmm)

    data_list_mmm.plot.bar()

    std_bmi = df.bmi.std()
    raz_bmi = df.bmi.max() - df.bmi.min()
    iqr_bmi = sts.iqr(df.bmi, interpolation="midpoint")
    print("bmi: ", std_bmi, "|", raz_bmi, "|", iqr_bmi)
    std_charges = df.charges.std()
    raz_charges = df.charges.max() - df.charges.min()
    iqr_charges = sts.iqr(df.charges, interpolation="midpoint")
    print("charges: ", std_charges, "|", raz_charges, "|", iqr_charges)

    list_sri = [[std_bmi, std_charges], [raz_bmi, raz_charges], [iqr_bmi, iqr_charges]]
    data_list_sri = pd.DataFrame(list_sri)
    print(data_list_sri)

    data_list_mmm.plot.bar()
    plt.show()
    return 0


def task4(df):
    plt.boxplot([df.age, df.bmi, df.children, df.charges], labels=["age", "bmi", "children", "charges"], vert=False)
    plt.show()
    return 0


def bootstrap(xs, n, replace=True):
    return np.random.choice(xs, (len(xs), n), replace=replace)


def task5(df: pd.DataFrame):
    pd.Series(df.bmi).hist(bins=20)
    plt.xlabel('Стандартное отклонение')
    plt.ylabel('Частота')
    pd.Series(map(mean, bootstrap(df.bmi, 300))).hist(bins=20)
    plt.xlabel('Распределение средних значений')
    plt.ylabel('Частота')
    plt.show()
    return 0


def task6(df):
    df_bmi = df.bmi
    df_charges = df.charges
    list_bmi = df_bmi.values.tolist()
    list_charges = df_charges.values.tolist()

    print(st.t.interval(0.95, len(list_bmi) - 1, loc=np.mean(list_bmi), scale=st.sem(list_bmi)))
    print(st.t.interval(0.99, len(list_bmi) - 1, loc=np.mean(list_bmi), scale=st.sem(list_bmi)))
    print(st.t.interval(0.95, len(list_charges) - 1, loc=np.mean(list_charges), scale=st.sem(list_charges)))
    print(st.t.interval(0.99, len(list_charges) - 1, loc=np.mean(list_charges), scale=st.sem(list_charges)))
    return 0


def task7(df):
    s = np.random.normal(df.bmi.mean(), df.bmi.std(), df.bmi.size)
    s_ = np.random.normal(df.charges.mean(), df.charges.std(), df.charges.size)
    sm.qqplot(df.bmi, s, line='45')
    sm.qqplot(df.charges, line='45')
    plt.show()
    print(kstest(df.bmi, s))
    print(kstest(df.charges, s_))
    return 0


def main():
    df = pd.DataFrame(pd.read_csv("../pr4/insurance.csv"))
    # print(df)
    task1(df)
    task2(df)
    task3(df)
    task4(df)
    task5(df)
    task6(df)
    task7(df)
    return 0


if __name__ == '__main__':
    main()
