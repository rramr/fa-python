class People:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def __str__(self) :
        return f'Имя: {self.name}, Возраст: {self.age}'

    def info(self):
        print (self.__class__.__name__ + ': ' + str(self))

class Worker(People):
    def __init__(self, name, age, post, salary):
        People.__init__(self, name, age)
        self.post = post
        self.salary = salary

    def __str__(self):
        return f'{super().__str__()}, Должность: {self.post}, Зарплата: {self.salary}'

class Teacher(Worker):
    _disciplines = ['Математика', 'Физика']

    def __init__(self, name, age, post, salary):
        self.salary = salary
        self.post = post
        super().__init__(name, age, post, salary)

    def __str__(self):
        return f'{super().__str__()}'
    
    def add_dis(self, dis):
        self._disciplines.append(dis)
        print(self._disciplines)
    
    def delete_dis(self, dis):
        self._disciplines.remove(dis)
        print(self._disciplines)


p1 = People('Chung', 21)
p2 = People('Adkins', 32)
w1 = Worker('Mcfarland', 48, 'Garden worker', 12321)
w2 = Worker('Gilbert', 28, 'Truck loader', 12321)
t1 = Teacher('Fowler', 36, 'Teacher', 45800)
t2 = Teacher('Mcfarland', 53, 'Professor', 89990)
members = [p1, p2, w1, w2, t1, t2]

# Вывод инормации о каждом человеке
print("\nВывод инормации о каждом человеке\n")
for member in members:
    member.info()

# Вывод тех, кто моложе 30 лет
print("\nВывод фамилий тех, кто моложе 30 лет\n")
for member in members:
    if(int(member.age) < 30):
        print(member.name)

print("\n")

t1.add_dis('Информатика')
t1.delete_dis('Физика')