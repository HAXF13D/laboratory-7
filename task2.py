# variant 6
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    array = list(map(int, input("Введите список целых чисел\n").split()))
    if not array:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    pos = 0
    maximum = array[0]
    count = 0
    first_zero_pos = None
    second_zero_pos = None
    for i in range(len(array)):
        if array[i] > maximum:
            maximum = array[i]
            pos = i
        if array[i] == 0:
            if count == 0:
                first_zero_pos = i
                count += 1
            elif count == 1:
                second_zero_pos = i
                count += 1
    compos = 1
    for i in range(first_zero_pos + 1, second_zero_pos):
        compos *= array[i]
    print(f"Позиция минимального элемента - {pos}")
    print(f"Произведение чисел между первым и втормы нулем - {compos}")
