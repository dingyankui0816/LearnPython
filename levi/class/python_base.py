class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self) -> None:
        print('名称 %s,分数 %d' % (self.name, self.score))

    pass

# stu = Student('Levi.Ding',100)
# stu1 = Student('Levi.Ding.1',101)
# print(stu)
# print(Student)
# print(stu.name)
# print(stu.score)
# stu.age = '我是中文'
# print(stu.age)
# print(stu1.age)

from customEnum import Month, Weekday

# print(Month.Jan.name)
#
# print(Month.Jan.name)

print(Weekday.Wed.value)


print(Weekday(3))

for name,member in Month.__members__.items():
    print(f'{name} => {member},{member.value}')