# list类型
L = [1, 2, 3]

# 索引
print(L[0], L[1], L[2])

# 倒序
print(L[-1], L[-2], L[-3])

# 添加 insert(索引,值)
L.insert(3, 4)
print(L)

# 删除 pop(索引)
L.pop(3)
print(L)

# 替换
L[0] = 3
L[-1] = 1
print(L)


# list切片
L = []
for x in range(1, 101):
    L.insert(x, x)

print('slices')
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3])
# 从0开始0可以省略
print(L[:3])
# :从头到尾
print(L[:])
# 从索引1开始，取出2个元素出来
print(L[1:3])
# 第三个参数表示每N个取一个
# 不大于50的5的倍数
print(L[4:50:5])


# 倒序切片
# 最后10个
print(L[-10:])
# 大于50的5的倍数
print(L[-46::5])


# 字符串切片
# 首字母大写
def make_first_upper(str):
    return str[0].upper() + str[1:]
print(make_first_upper('morin'))
