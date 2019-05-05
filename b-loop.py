# for循环
# 1-10累加
sum = 0
for v in range(1, 11):
    sum += v
    print(v)
print('sum is:', sum)

# while循环
# 从 0 开始打印不大于 N 的整数
N = 10
x = 0
while x < N:
    print(x)
    x += 1

# break退出死循环
sum = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum += x
    x *= 2
    n += 1

print(sum)

# continue继续循环
# 0-100内奇数和
sum = 0
x = 0
while True:
    x += 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print(sum)

# 嵌套循环
for x in range(1, 11):
    for y in range(0, 10):
        if x < y:
            print(x * 10 + y)


# 索引迭代
L = ['Adam', 'Lisa', 'Bart', 'Paul']
# 迭代的每一个元素实际上是一个tuple[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
for x in L:
    k = x[0]
    v = x[1]
    print(k, '-', v)
# 可简写为
for k, v in enumerate(L):
    print(k, '-', v)
# zip()函数可以把两个 list 变成一个list
# >>> zip([10, 20, 30], ['A', 'B', 'C'])
# [(10, 'A'), (20, 'B'), (30, 'C')]
for k, v in zip(range(0, len(L)), L):
    print(k, '-', v)


# 迭代dict的value
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
print(d.values())
for v in d.values():
    print(v)


# 迭代dict的key和value
print(d.items())
for k, v in d.items():
    print(k, '-', v)
