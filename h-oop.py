# 面向对象编程
class Person():

    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__title__ = 'Monkey'
        # 双下划线开头__，该属性就无法被外部访问
        self.__married = 'True'
        for k, v in kw.items():
            setattr(self, k, v)

    def get_married(self):
        return self.__married


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'
morin = Person('Morin', 'Male', '1982-05-03', job='Coder')
print(morin.job)
print(morin.__title__)
print(morin.get_married())

# print(morin.__married)
# morin.name = 'Morin'
# daisy = Person()
# daisy.name = 'Daisy'
# print(morin.name)
# print(daisy.name)
# print(morin == daisy)
