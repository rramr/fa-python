def calc(num1, num2, act):
    if act == "+":
        return (num1 + num2)
    elif act == "-":
        return (num1 - num2)
    elif act == "*":
        return (num1 * num2)
    elif act == "/":
        return (num1 / num2)
    return("Неизвестная операция")

print(calc(2, 6, "+"))