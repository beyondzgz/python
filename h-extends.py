# 类的继承
# 必须从某类继承，如果没有合适的类就是object继承
# super().__init__()初始化父类的属性


class Person(object):

    def __init__(self, name):
        self.name = name


class Family(Person):

    def __init__(self, name, sex):
        super(Family, self).__init__(name)
        self.sex = sex

p = Person('Morin')
fa = Family('Morin', 'Man')
print(fa.name)
print(fa.sex)
print(isinstance(fa, Person))
print(isinstance(p, Family))


# type()
print(type(fa))

# dir()
print(dir(fa))

# 如果已知一个属性名称，要获取或者设置对象的属性用getattr()和setattr()
setattr(fa, 'name', 'Daisy')
print(getattr(fa, 'name'))
