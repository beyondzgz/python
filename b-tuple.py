# tuple(元组)一旦创建完毕就不能修改
t = (1, 2, 3)
print(t)

# 单元素tuple
t = (1,)
print(t)

# 可变tuple
# tuple一开始指向的list并没有改成别的list
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a' 就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = (1, 2, ['A', 'B'])
L = t[2]
L[0] = 'C'
L[1] = 'D'
print(t)
