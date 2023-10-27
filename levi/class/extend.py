import types


class Animal(object):
    def run(self):
        print('Animal is running...')

    def __len__(self):
        print('重写的len方法')
        return 'animal'.__len__()


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


print(type(Dog()) == type(Animal()))

print(type(i for i in range(1, 10)))

print(type(lambda x: x + 1) == types.LambdaType)

print(isinstance(Dog(),Dog) and isinstance(Dog(),Animal))

print(isinstance(Animal(),Dog) or isinstance(Animal(),Cat))

print(dir((Animal())))

print('%d %d' % (len((Animal())), Dog().__len__()))



