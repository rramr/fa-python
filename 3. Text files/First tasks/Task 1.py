# Создать в текстовом редакторе файл, содержащий несколько строк. Определить максимальный и минимальный размер строки в файле и вывести их в другой файл. Вывести в этот же файл все строки максимальной длины.

def maxList(lst):
    mx = 0
    line = lst[1]
    for i in lst:
        if len(i) > mx:
            mx = len(i)
            line = i
    return line, mx

def minList(lst, mx):
    mn = mx
    line = lst[1]
    for i in lst:
        if len(i) < mn:
            mn = len(i)
            line = i
    return line, mn

def allMax(lst, mx):
    allMax = []
    for i in lst:
        if len(i) == mx:
            allMax.append(i)
    return allMax

r_path = "./3. Text files/First tasks/Task 1_r.txt"
w_path = "./3. Text files/First tasks/Task 1_w.txt"
lineList = []

txt_r = open(r_path, 'r')

line = txt_r.readline()
while line != '':
    lineList.append(line.rstrip('\n'))
    line = txt_r.readline()

txt_r.close()

max = maxList(lineList)
min = minList(lineList, max[1])
all = allMax(lineList, max[1])

txt_w = open(w_path, 'w')

print("Максимальный размер строки: " , max[1] , file = txt_w)
print("Минимальный размер строки: " , min[1] , file = txt_w)
print("\nМаксимальная строка: " , max[0] , file = txt_w)
print("Минимальная строка: " , min[0] , file = txt_w)
print("\nВсе строки максимальной длины: " , all , file = txt_w)

txt_w.close()