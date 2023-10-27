class Student(object):
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __str__(self):
        return f'Student name: {self.name} '

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.name) :
            raise StopIteration()
        result = self.name[self.index]
        self.index += 1
        return result
    def __getitem__(self, item):
        return self.name[item]

    def __getattr__(self, item):
        if item == 'score':
            return 1000
        if item == 'getAge':
            return lambda : 30

    def __call__(self, *args, **kwargs):
        print('测试一下')
#
stu = Student('Levi.Ding')
# print(stu)
#
# for i in stu:
#     print(i)
#
# print(stu[5])


# print(stu[5:7])

print(f'{stu.name} 分数为 : {stu.score} 年龄为 : {stu.getAge()}')

stu()

print(f'当前对象是否可调用: Student : {callable(stu)} , int : {callable(1)} , list : {callable([1,2,3])} , str : {callable("123")}')




