

class Student(object):
    __slots__ = ('name','age','set_age')
    pass


class GraduateStudent(Student):
    # __slots__ = ('test')
    pass

def MethodTypeCustom(func, o):
    def wrapper(*args, **kwargs):
        return func(o, *args, **kwargs)

    return wrapper


s = Student()
s1 = Student()
s.name = 'Levi'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodTypeCustom(set_age, s)
s.set_age(11)
print(s.age)
Student.set_age = set_age
s1.set_age(18)
print(s1.age)

gs = GraduateStudent()
gs.score = 100
print(gs.score)
