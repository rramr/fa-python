# Создайте класс Length (Длина), имеющий свойства:
# • value (значение),
# • unit (единица измерения).
# При изменении единицы измерения значение должно соответственно меняться. Например, при переходе от сантиметров к метрам значение должно уменьшаться в 100 раз. Допустимые значения свойства unit: ‘см’, ‘м’, ‘км’. Организуйте эту проверку. Продемонстрируйте работу с классом.

class Length:
    def __init__ (self, value, unit) :
        self.value = value
        self.unit = unit

    def __str__ (self) :
        return "Lenght("+str(self.value)+","+str(self.unit)+")"

    def show (self) :
        if self.unit == 'см':
            self.m = self.value / 100
            self.km = self.value / 100000
            return str("M: " + str(self.m) + ", KM: " + str(self.km))
        if self.unit == 'м':
            self.cm = self.value * 100
            self.km = self.value / 1000
            return str("CM: " + str(self.cm) + ", KM: " + str(self.km))
        if self.unit == 'км':
            self.cm = self.value * 100000
            self.m = self.value * 1000
            return str("CM: " + str(self.cm) + ", M: " + str(self.m))
        return "Недопустимое значение unit"

L = Length(5, 'км')

print(L, L.show())