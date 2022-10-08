import math


def calc_square(input_data: dict[str, float | list[float]]):
    res = {}
    for fig in input_data:
        match fig:
            case 'triangle':
                s = calc_triangle_square(*input_data[fig])
                res |= {'triangle': s}
            case 'circle':
                s = math.pi * input_data[fig] ** 2
                res |= {'circle': s}
            case 'rectangle':
                s = input_data[fig][0] * input_data[fig][1]
                res |= {'rectangle': s}
            case _:
                pass
    return res


def calc(val_a: float | int, val_b: float | int, operation: str):
    match operation:
        case '+':
            res = val_a + val_b
        case '-':
            res = val_a - val_b
        case '/':
            try:
                res = val_a / val_b
            except ZeroDivisionError:
                res = 0
        case '//':
            try:
                res = val_a // val_b
            except ZeroDivisionError:
                res = 0
        case '**':
            res = val_a ** val_b
        case _:
            res = 0
    return res


def calc_triangle_square(a: int | float, b: int | float, c: int | float):
    p = sum([a, b, c]) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    data = {'triangle': [3, 4, 5], 'circle': 2, 'rectangle': [1, 2]}
    print('input data: ', data)
    print('task1\n', calc_square(data))
    print('task2')
    print(calc(float(input('val_a: ')), float(input('val_b: ')), input('operation: ')))
    print('task3\n', calc_triangle_square(3, 4, 5))


if __name__ == "__main__":
    main()
