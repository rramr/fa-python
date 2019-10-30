# • создайте класс, моделирующий работу с двумерным массивом с аналогичными методами. Индексы массива изменяются с1.

import random

class Arr:
    def __init__(self, n, m) :
        self.__n = n
        self.__m = m
        self.__val = []
        for i in range(n):
            self.__val.append([])
            for j in range(m):
                self.__val[i].append(j * 0)

    n = property(lambda self:self.__n)
    m = property(lambda self:self.__m)

    def __str__(self):
        return " ".join(map(str,self.__val))

    def arr_range_n(self):
        return range(1, self.n)

    def arr_range_m(self):
        return range(1, self.m)

    def get(self):
        return random.randint(self.n, self.m)

    def put(self, i, j, x):
        self.__val[i][j] = x

#использование класса
Z = Arr(3,5)
print(Z.n, Z.m)
print(Z)
for i in Z.arr_range_n():
    for j in Z.arr_range_m():
        Z.put(i,j,Z.get())
print (Z)