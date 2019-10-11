# Напишите функцию, которая находит все точки, в которых достигается максимальное значение, на заданном отрезке. Функция возвращает список найденных точек. Считаем, что 𝑓(𝑥1) = 𝑓(𝑥2), если |𝑓(𝑥1) − 𝑓(𝑥2)| ≤ 𝑒𝑝𝑠. 𝑒𝑝𝑠 является параметром функции, по −3 умолчанию 𝑒𝑝𝑠 = 10^-3. Остальные параметры такие же, как в предыдущей функции. Используя эту функцию, найдите точки, в которых достигается максимум функций 𝑠𝑖𝑛^2(𝑥/2) и 2*𝑠𝑖𝑛^2(3𝑥), на отрезке [0, 4].

import math

f1 = lambda x: pow(math.sin(x / 2), 2)
f2 = lambda x: 2 * pow(math.sin(3 * x), 2)

def calc(f, a = 0, b = 5, h = 0.1):
    list = []
    while a <= b:
        list.append(f(a))
        a += h
    return list

def maxi(f_list, a = 0, b = 5, eps = pow(10, -3), h = 0.1):
    list_max = []
    list_pop = []
    for i in range(len(f_list) - 1):
        if (abs(f_list[i] - f_list[i + 1]) <= eps):
            if f_list[i] < f_list[i + 1]:
                list_pop.append(i)
            else:
                list_pop.append(i+1)

    for i in range(len(list_pop)):   
        f_list.pop(i)

    for i in range(len(f_list) - 1):
        if f_list[i - 1] < f_list[i] > f_list[i + 1]:
            list_max.append(f_list[i])
    return list_max

a = 0
b = 4

f1_list = calc(f1, a, b)
f2_list = calc(f2, a, b)

print("Точки максимума первой функции: ", maxi(f1_list, a, b, pow(10, -3)))
print("Точки максимума второй функции: ", maxi(f2_list, a, b, pow(10, -3)))