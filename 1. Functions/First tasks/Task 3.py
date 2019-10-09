import math

def calc(x, y, z):
    xy = math.degrees(math.acos((pow(x, 2) + pow(y, 2) - pow(z, 2))/(2 * x * y)))
    yz = math.degrees(math.acos((pow(y, 2) + pow(z, 2) - pow(x, 2))/(2 * y * z)))
    xz = math.degrees(math.acos((pow(x, 2) + pow(z, 2) - pow(y, 2))/(2 * x * z)))
    return((xy, yz, xz))

xyz = (4, 3, 5)

res = calc(*xyz)

print(
    "Угол между сторонами xy = " , calc(*xyz)[0] ,
    ", угол между сторонами yz = " , calc(*xyz)[1] ,
    ", угол между сторонами xz = " , calc(*xyz)[2]
)