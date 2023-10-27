from functools import reduce


class Student(object):

    name = 'Student'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self) -> str:
        return self.__name

    def get_score(self) -> int:
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def print_score(self) -> None:
        print('%s: %d' % (self.get_name(), self.get_score()))

    def power(self, i) -> int:
        # return reduce(lambda x,y: x*y , [self.get_score() for i in range(i)])
        return self.get_score() ** i

#
# stu = Student('Levi', 100)
# stu.print_score()
# stu.set_name('Ding')
# stu.set_score(99)
# stu.print_score()
# stu.__name = '测试一下'
# print(stu.__name)
# stu.print_score()
# stu.set_score(10)
# print(stu.power(2))
# print(hasattr(stu, '__name'))
# print(hasattr(stu, '__score'))
# print((getattr(stu,'__name')))
# print((setattr(stu,'__score',1)))
# print((getattr(stu,'__score')))
# print((hasattr(stu,'power')))
# fn = getattr(stu,'power')
# print(fn(2))

stu = Student('Levi',1)
print('对象属性: %s , 类属性: %s' % (stu.name, Student.name))
print(f'对象属性: %s , 类属性: ' % (stu.name, Student.name))
Student.name = 'Ding'
print('对象属性: %s , 类属性: %s' % (stu.name, Student.name))
stu.name = '1'
print('对象属性: %s , 类属性: %s' % (stu.name, Student.name))
del stu.name
print('对象属性: %s , 类属性: %s' % (stu.name, Student.name))
stu.name = '2'
print('对象属性: %s , 类属性: %s' % (stu.name, Student.name))
del Student.name
print('对象属性: %s , 类属性: %s' % (stu.name, '1'))


