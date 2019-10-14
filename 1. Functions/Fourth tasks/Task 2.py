# При помощи функций map/filter/reduce превратить список целых чисел в строку, содержащую строковое представление этих чисел, разделенных пробелами.

from functools import reduce

lst = list(range(1,20))
lst = list(map(str, lst))
lst = reduce(lambda x,y: x + " " + y, lst)

print(lst)