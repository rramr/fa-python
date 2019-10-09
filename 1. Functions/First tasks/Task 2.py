import math

def calc(r):
    s = math.pi * pow(r, 2)
    p = 2 * math.pi * r
    return((s, p))

r = 5

print("Площадь круга = " , calc(r)[0] , ", длина окружности = " , calc(r)[1])