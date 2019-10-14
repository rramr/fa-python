# При помощи функций map/filter/reduce из несколько одинаковых подряд идущих элементов списка оставить только один. Например, [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 6, 1, 1] -> [1, 2, 3, 4, 5, 6, 7, 6, 1]

from functools import reduce

def sort(x):
    global temp
    if (temp != x):
        temp = x
        return x
    else:
        temp = x
        return None

temp = None
lst = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 6, 1, 1]

lst = list(filter(sort, lst))
print(lst)