# 多返回值函数
def multiple_result(x, y):
    return x + y, x * y

x, y = multiple_result(1, 2)
print(x, y)


# 递归函数
def recursion(x, m):
    if x < m:
        x += 1
        recursion(x, m)
        print(x)
recursion(0, 10)


# 参数默认值
def hello(name='world'):
    print('Hello', name)
hello()
hello('Morin')


# 可变参数
def average_value(*args):
    sum = 0
    cnt = len(args)
    if cnt <= 0:
        return sum
    else:
        for v in args:
            sum += v
        return sum / cnt
print(average_value())
print(average_value(1, 2))
print(average_value(1, 2, 3))
