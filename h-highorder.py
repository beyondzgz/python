import math
import time
import functools
from functools import reduce

# 高阶函数，把函数作为参数传给另一个函数


def add(x, y, f):
    return f(x) + f(y)

# 绝对值之和
print(add(-1, -2, abs))
# 平方根之和
print(add(25, 9, math.sqrt))


# map函数
def format_name(s):
    return s[0].upper() + s[1:].lower()
print(map(format_name, ['adam', 'LISA', 'barT']))


# reduce函数
def prod(x, y):
    return x * y
print(reduce(prod, [2, 4, 5, 7, 12]))


# filter函数
def is_odd(x):
    return x % 2 == 1
print(filter(is_odd, [1, 4, 6, 7, 9, 12, 17]))


# 自定义排序函数
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=lambda x: x.upper()))


# python中返回函数
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print(f())


# 闭包
# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())


# 匿名函数
# 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
print(filter(lambda s: s and len(s.strip()) > 0,
             ['test', None, '', 'str', '  ', 'END']))


# 装饰器
def log(f):
    def fn(*args, **kw):
        print('call ' + f.__name__ + '()...')
        return f(*args, **kw)
    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(10))


def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(10))


# 偏函数
# functools.partial帮助我们创建一个偏函数的
int2 = functools.partial(int, base=2)
print(int2('1000000'))


# 动态导入模块
# 先尝试从json导入，如果失败了再尝试从simplejson导入。
try:
    import json
except ImportError:
    import simplejson as json
print(json.dumps({'python': 2.7}))
