# В списке 2n + 1 различных элементов. Найдите средний элемент списка. Под средним элементом понимают такой, для которого в списке n элементов больше его и n элементов меньше.

def calc(arr):
    if len(arr) % 2 == 0:
        print("В списке чётное количество элементов. Последний элемент будет удалён")
        arr.pop(len(arr) - 1)
    arr.sort()
    to = int(len(arr)/2)
    return arr[to]

lst = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 6, 1, 1, 2, 8, 2, 2, 3, 5, 1]

print("Средний элемент: " , calc(lst))