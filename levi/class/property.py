class Student(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('名称')
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = '名称: %s' % name

    @property
    def score(self):
        return 150




s = Student('levi')
print(s.name)
s.name = 'Levi.Ding'
print(s.name)
print(s.score)