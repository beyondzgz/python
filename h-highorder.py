import math
from functools import reduce

# 高阶函数，把函数作为参数传给另一个函数


def add(x, y, f):
    return f(x) + f(y)

# 绝对值之和
print(add(-1, -2, abs))
# 平方根之和
print(add(25, 9, math.sqrt))


def format_name(s):
    return s[0].upper() + s[1:].lower()
print(map(format_name, ['adam', 'LISA', 'barT']))


def prod(x, y):
    return x * y

print(reduce(prod, [2, 4, 5, 7, 12]))
