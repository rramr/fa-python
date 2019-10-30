# Задание:
# • продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы;
# • создайте аналогичный класс для треугольника с такими же методами.

import math

class Point:
    def __init__ (self, x, y) :
        self.x=x
        self.y=y

    def __str__ (self) :
        return "Point("+str(self. x)+","+str(self.y)+")"

class Rect:
    def __init__ (self, top_left, bottom_right):
        self.A = top_left
        self.C = bottom_right

    def __str__ (self) :
        r = "Rect(" + str(self.A) + ","
        r = r + str(self.C) + ")"
        return r

    def sides (self) :
        return abs(self.C.x-self.A.x),abs(self.A.y-self.C.y)
    
    def perim(self):
        a, b = self.sides()
        return 2*(a+b)

class Triangle:
    def __init__ (self, left, top, right):
        self.A = left
        self.B = top
        self.C = right

    def __str__ (self) :
        r = "Triangle("
        r += str(self.A) + ","
        r += str(self.B) + ","
        r += str(self.C) + ")"
        return r

    def sides (self) :
        return (
            abs(math.sqrt(self.A.x ** 2 + self.A.y ** 2)),
            abs(math.sqrt(self.B.x ** 2 + self.B.y ** 2)),
            abs(math.sqrt(self.C.x ** 2 + self.C.y ** 2))
        )
    
    def perim(self):
        a, b, c = self.sides()
        return a+b+c

P1 = Point(3,4)
P2 = Point(7,9)
P3 = Point(5, 15)

R = Rect(P1, P2)
T = Triangle(P1, P2, P3)

print(P1, P2)
print(R, R.sides(), R.perim())
print(T, T.sides(), T.perim())