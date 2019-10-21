# Создайте текстовый файл, содержащий информацию о товарах и ценах на них. Каждая строка файла имеет вид: НАЗВАНИЕ ТОВАРА: ЦЕНА. 
# Используя данный файл:
# • найдите цену указанного товара, или выдайте сообщение о том, что цена не известна;
# • добавьте в файл информацию о трех новых товарах;
# • удалите из файла информацию о товаре;
# • создайте новый файл, в котором товары будут упорядочены в порядке возрастания цен. Выведите на экран информацию о двух самых дешевых и двух самых дорогих товарах.

def readFile():
    global dict
    lineList = []
    r_path = "./3. Text files/First tasks/Task 2_r.txt"
    txt_r = open(r_path, 'r')

    line = txt_r.readline()
    while line != '':
        lineList.append(line.rstrip('\n'))
        line = txt_r.readline()
    txt_r.close()
    dict.clear()
    for i in lineList:
        if i:
            key = i.split(":")[0]
            value = i.split(" ")[1]
            dict[key] = value

def findPrice(prod):
    global dict
    for i in dict:
        if i == prod:
            return str("Товар '" + i + "' - найден. Его цена: " + dict.get(i))
    return "Товар не найден"

def addToFile(lst):
    r_path = "./3. Text files/First tasks/Task 2_r.txt"
    txt_r = open(r_path, 'a')

    for i in lst:
        txt_r.write("\n" + str(i[0] + ": " + str(i[1])))
    txt_r.close()

def delItem(key):
    readFile()
    global dict
    try:
        del dict[key]
    except KeyError:
        print("Ключ не найден!")
    r_path = "./3. Text files/First tasks/Task 2_r.txt"
    txt_r = open(r_path, 'w')

    for i in dict:
        txt_r.write(str(i + ": " + dict.get(i)) + "\n")
    txt_r.close()

def sortItems():
    global dict
    sortListDict = list(dict.items())
    sortListDict.sort(key=lambda i: int(i[1]))

    w_path = "./3. Text files/First tasks/Task 2_w.txt"
    txt_w = open(w_path, 'w')
    for i in sortListDict:
        txt_w.write(str(i[0] + ": " + i[1] + "\n"))
    txt_w.close()

    print(str("Два самых дешёвых товара: " + str(sortListDict[0]) + ", " + str(sortListDict[1])))
    print(str("Два самых дорогих товара: " + str(sortListDict[len(sortListDict) - 2]) + ", " + str(sortListDict[len(sortListDict) - 1])))

dict = dict()
readFile() #Считывание и заполенние славоря
print(findPrice("Апельсины")) #Поиск стоимости
addToFile([["Хлеб", 15], ["Молоко", 64], ["Арахис", 115]]) #Добавление элементов в файл
delItem("Хлеб") #Удаление элемента
sortItems() #Сортировка