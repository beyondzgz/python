# 不重复的key
s = set(['adam', 'Lisa', 'bart', 'Paul'])
print(s)
print('adam' in s)
print('bart' in s)

# set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
# 应用：月份星期
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'
if x1 in months:
    print('x1: ok')
else:
    print('x1: error')
if x2 in months:
    print('x2: ok')
else:
    print('x2: error')

# 遍历set
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x[0] + ':', x[1])

# 更新set
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for k in L:
    if k in s:
        s.remove(k)
    else:
        s.add(k)
print(s)
