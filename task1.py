# variant 25
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    array = list(map(float, input(f"Введите время в секундах каждого спортсмена\n").split()))
    if len(array) <= 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    result = min(array)
    print(f"Лучее время - {result}")
