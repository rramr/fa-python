class Order:
    def __init__(self, code, price, count) :
        self.code = code
        self.price = price
        self.count = count

    def __str__(self) :
        return f'Код товара: {self.code}, Цена: {self.price}, Количество: {self.count}'
    
class Opt(Order):
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def __str__(self) :
        return f'{super().__str__()}'
    
    def summa(self):
        if(self.count > 500):
            return f'{super().__str__()}, Сумма = {self.count * (self.price/100*95)}'
        return f'{super().__str__()}, Сумма = {self.count * self.price}'

class Retail(Order):
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def __str__(self) :
        return f'{super().__str__()}'
    
    def summa(self):
        return f'{super().__str__()}, Сумма = {self.count * self.price}'

o = Opt(112, 350, 600)
r = Retail(111, 350, 50)

members = [o, r]

for member in members:
    print(member.summa())