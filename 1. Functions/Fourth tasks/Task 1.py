# При помощи функций map/filter/reduce возвести в квадрат числа от 1 до 100, и рассчитать их сумму, не включая в сумму числа, кратные 9
from functools import reduce

lst = list(filter(lambda f: f % 9 != 0, range(1,100)))
lst = pow(reduce(lambda a, b: (a + b), lst), 2)

print(lst)