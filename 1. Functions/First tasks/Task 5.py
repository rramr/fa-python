# import math
from GCD import gcd_calc

def tuple_func(n, m, gcd):
    p = n / gcd
    q = m / gcd
    return((p, q))

def list_func(nm_gcd):
    global list
    p = nm_gcd[0] / nm_gcd[2]
    q = nm_gcd[1] / nm_gcd[2]
    list = [p, q]

n = 14
m = 2322
gcd = gcd_calc(n, m)

tuple = tuple_func(*(n, m, gcd))
list = [n, m, gcd]
list_func(list)

print("Результат сокращения через первую функцию: ", n, "/", m, " -> ", int(tuple[0]), "/", int(tuple[1]))
print("Результат сокращения через вторую функцию: ", n, "/", m, " -> ", int(list[0]), "/", int(list[1]))