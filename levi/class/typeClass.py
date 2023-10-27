class Hello(object):
    def fn(self,name = 'world') -> None:
        print(f'Hello, {name}.')

def fn1(self,name) -> None:
    print(f'Hello1, {name}.')

Hello1 = type('Hello1',(object,),dict(hello = fn1,test = lambda x:print(x)))
h1 = Hello1()
h1.hello('Levi')
h1.test('测试')