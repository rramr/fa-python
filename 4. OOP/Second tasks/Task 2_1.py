# • добавьте в этот класс метод, заполняющий массив случайными целыми числами из заданного диапазона (границы диапазона – параметры метода);

class Arr:
    def __init__(self, a, b) :
        self. __a = a
        self. __b = b
        self. __val = [0]*(self.b - self.a+1)

    a = property(lambda self:self.__a)
    b = property(lambda self:self.__b)

    def __str__(self):
        return " ".join(map(str,self.__val))

    def arr_range(self):
        return range(self.a, self.b+1)

    def get(self, i):
        if self.a <= i <= self.b:
            return self.__val[i - self.a]
        else:
            print ("Недопустимый индекс", i)

    def put(self, i, x):
        if self.a <= i <= self.b:
            self.__val[i - self.a] = x
        else:
            print("Недопустимый индекс", i)

#использование класса
Z = Arr(-5,5)
print(Z.a, Z.b)
print(Z)
for i in Z.arr_range():
    Z.put(i,Z.get(i)+i)
print (Z)