
class Statement:
    disc_list = ['Математика', 'Физика', 'Информатика']
    assessments = tuple(['', 'н/я', 'неудовл.', 'удовл.', 'хорошо', 'отлично'])
    dict = {}

    def __init__(self, disc, grp):
        self.__disc = disc
        self.__grp = grp
        print('Предмет: ' + self.disc + ', группа: ' + self.grp)
    
    disc = property(lambda self:self.__disc)
    grp = property(lambda self:self.__grp)
    
    def __str__(self):
        return " ".join(map(str,(self.disc_list, self.disc, self.grp)))
    
    def put(self, name, asm):
        self.dict[name] = self.assessments[asm]

    def get(self, name):
        asm = self.dict.get(name)
        return str('Оценка ' + name + ': ' + asm)

    def change(self, name, asm):
        self.dict[name] = self.assessments[asm]
        print(self.dict)
    
    def dlt(self, name):
        self.dict.pop(name)
        print(self.dict)
    
    def result(self):
        return self.assessments

    def count(self):
        return len(self.dict)

    def names(self):
        return self.dict.keys()

S1 = Statement('Физика', 'ЗБ-ПИ2-1')
S1.put('Ivanov', 3)
S1.put('Petroff', 4)
S1.put('Guskoff', 5)
S1.put('Titoff', 5)
print(S1.get('Ivanov'))
S1.change('Ivanov', 4)
S1.dlt('Petroff')
print(S1.result())
print('Количество студентов в ведомости: ' + str(S1.count()))
print(S1.names())