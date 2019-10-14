# Дан список из N элементов.Вывести индексы списка в том порядке,в котором соответствующие им элементы образуют возрастающую последовательность

def sort(arr):
    ind = list(range(int(len(arr))))
    for i in range(int(len(arr))):
        mn = min(arr)
        mn_ind = arr.index(mn)
        arr[mn_ind] = max(arr) + 1
        ind[mn_ind] = i 
    return ind

lst = [1, 2, 3, 4, 4, 6, 7, 6, 2, 1]

print("Массив:  " , lst)
print("Индексы: " , sort(lst))