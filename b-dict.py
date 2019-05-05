# dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
# 不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
# dict的第二个特点就是存储的key-value序对是没有顺序的！
# dict的第三个特点是作为 key 的元素必须不可变

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print(d)

# 更新dict
d['Morin'] = 100
print(d)
d['Morin'] = 99
print(d)

# 遍历dict
for k in d:
    print(k)
    print(d[k])
