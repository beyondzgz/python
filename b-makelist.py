# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)
L = []
for x in range(1, 11):
    L.insert(x, x)
print(L)
L = []
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
for x in range(1, 11):
    L.append(x * x)
print(L)


# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
# 这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成List
L = [x * x for x in range(1, 11)]
print(L)

# range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
# 生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
L = [x * (x + 1) for x in range(1, 101, 2)]
print(L)


# 复杂表达式
# 注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' %
       (name, score) for name, score in d.items()]
print(tds)
print('<table>')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')


def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]
print(tds)
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')


# 条件过滤
# 有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)


# 多层表达式
L = [m + n for m in 'ABC' for n in '123']
print(L)
# 翻译成循环代码就像下面这样
L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)
print(L)
