import math

# 高阶函数，把函数作为参数传给另一个函数


def add(x, y, f):
    return f(x) + f(y)

if __name__ == '__main__':
    # 绝对值之和
    print(add(-1, -2, abs))

    # 平方根之和
    print(add(25, 9, math.sqrt))
