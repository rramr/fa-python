# Создайте два текстовых файла, содержащие целые числа, в которых данные отсортированы по неубыванию. Каждая строка содержит одно число. Сформируйте новый файл из чисел входных файлов, чтобы его значения были также отсортированы по неубыванию (не использовать методы сортировки).

def readFile():
    global lineList

    r_path_1 = "./3. Text files/First tasks/Task 3_r1.txt"
    txt_r_1 = open(r_path_1, 'r')
    r_path_2 = "./3. Text files/First tasks/Task 3_r2.txt"
    txt_r_2 = open(r_path_2, 'r')

    line = txt_r_1.readline()
    while line != '':
        lineList.append(int(line.rstrip('\n')))
        line = txt_r_1.readline()
    txt_r_1.close()

    line = txt_r_2.readline()
    while line != '':
        lineList.append(int(line.rstrip('\n')))
        line = txt_r_2.readline()
    txt_r_2.close()

def sortItems(): #Сортировка методом пузырька
    global lineList
    for i in range(len(lineList) - 1):
        for j in range(len(lineList) - i - 1):
            if lineList[j] > lineList[j + 1]:
                sw = lineList[j]
                lineList[j] = lineList[j + 1]
                lineList[j + 1] = sw

def writeFile():
    global lineList
    w_path = "./3. Text files/First tasks/Task 3_w.txt"
    txt_w = open(w_path, 'w')
    for i in lineList:
        txt_w.write(str(i) + "\n")
    txt_w.close()

lineList = []
readFile() #Чтение файла
sortItems() #Сортировка
writeFile() #Запись в файл