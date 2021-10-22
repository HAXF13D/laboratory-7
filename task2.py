# variant 6
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import prod

if __name__ == '__main__':
    array = list(map(int, input("Введите список целых чисел\n").split()))
    if not array:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    maximum = array[0]
    pos = 0
    first_zero_pos = None
    second_zero_pos = None
    zero_count = 0
    for i, elem in enumerate(array):
        if elem > maximum:
            maximum = elem
            pos = i
        if elem == 0:
            if zero_count == 0:
                first_zero_pos = i
                zero_count += 1
            elif zero_count == 1:
                second_zero_pos = i
                zero_count += 1
    compos = 0
    if first_zero_pos is not None and second_zero_pos is not None:
        compos = prod(array[first_zero_pos + 1:second_zero_pos])

    odd_part = [elem for i, elem in enumerate(array) if i % 2 == 0]
    even_part = [elem for i, elem in enumerate(array) if i % 2 != 0]
    result = odd_part+even_part

    print(f"Позиция максимального элемента - {pos}")
    print(f"Произведение чисел между первым и втормы нулем - {compos}")
    print(f"Список, где эелменты с нечетных позиций в начале, а с четных в конце - {result}")
