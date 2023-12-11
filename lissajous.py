import os
import math

# Функция для вычисления значения x с использованием конкретной формулы
def calculate_x(x):
    if abs(x) < 0.1:
        return x / (math.sqrt(1 + x) + math.sqrt(1 - x))
    else:
        return x + (x ** 3) / 6 + 0.075 * (x ** 5) + (x ** 7) / 22.4

# Функция для генерации и отображения узора Лиссажу
def calculate_lissajous():
    # Вывод информации заголовка
    print(" " * 22 + "LISSAJOUS")
    print(" " * 18 + "CREATIVE COMPUTING")
    print(" " * 16 + "MORRISTOWN  NEW JERSEY")
    print("\n" * 3)

    # Получение ввода для относительной частоты X
    print("RELATIVE FREQ. FOR X", end=": ")
    f1 = float(input())
    if int(f1) != f1 or f1 < 1:
        calculate_lissajous()

    # Подгонка частоты для вычислений
    f = f1
    f1 *= 2 * math.pi

    # Получение ввода для относительной частоты Y
    print("RELATIVE FREQ. FOR Y", end=": ")
    f2 = float(input())
    if int(f2) != f2 or f2 < 1:
        calculate_lissajous()

    # Получение ввода для фазы Y (в кратных значениях pi)
    print("Y PHASE, MULTIPLE OF PI", end=": ")
    p2 = float(input())
    p2 *= math.pi

    # Подгонка частоты для вычислений
    f2 *= 2 * math.pi

    # Установка переменных для построения узора
    max_y = 35
    y_values = [[' ' for _ in range(max_y * 2 + 1)] for _ in range(39)]

    # Итерация по значениям x для генерации точек узора Лиссажу
    for x1 in range(-18, 19):
        x = x1 / 18
        x = calculate_x(x)
        t1 = x
        t2 = math.pi - x

        # Итерация по значениям времени для вычисления координат Y
        for i in range(int(f)):
            t3 = (t1 + 2 * i * math.pi) / f1
            t4 = (t2 + 2 * i * math.pi) / f1
            y1 = round(30 * math.sin(f2 * t3 + p2))
            y2 = round(30 * math.sin(f2 * t4 + p2))

            # Гарантия, что значения Y находятся в указанном диапазоне
            y1 = min(max_y, max(-max_y, y1))
            y2 = min(max_y, max(-max_y, y2))

            # Пометка точек в матрице для представления узора Лиссажу
            y_values[x1 + 18][y1 + max_y] = '*'
            y_values[x1 + 18][y2 + max_y] = '*'

    # Вывод сгенерированного узора Лиссажу
    for row in y_values:
        print(''.join(row))

# Вызов функции для генерации и отображения узора Лиссажу
calculate_lissajous()
