def findWords(*list):
    print("\nПоиск совпадений: ")
    return [i for i in list[1] if list[0].lower() in i.lower()]

def simpleCalc(num1, num2, act):
    print("\nПростая арифметическая операция: ")
    if act == "+":
        return (num1 + num2)
    elif act == "-":
        return (num1 - num2)
    elif act == "*":
        return (num1 * num2)
    elif act == "/":
        return (num1 / num2)
    return("Неизвестная операция")