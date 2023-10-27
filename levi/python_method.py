import functools
import os


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def my_pass():
    pass


def my_if_pass(x):
    if x >= 0:
        pass
    else:
        return '是负数'


def my_more_response():
    return 'Levi_1', 'Levi_2'


def my_more_param(x, y, z, a=2, b=3):
    b *= 2
    print(b)
    a *= 2
    return x + y / a, x + z / a, y + z * a


def my_change_param(x, y, z, *sums, a=2):
    print(a)
    for sum in sums:
        print(sum * x * y * z)


def my_change_param(x, y, z, a=2, **sums):
    print(a)
    print(type(sums))
    for sum in sums:
        print(sums[sum])
        print(x * y * z)


def my_key_param(x, y, z, *args, a, b):
    print(args)


def my_yield_dir(s):
    dir = os.listdir(s)
    for d in dir:
        di = s + '/' + d
        if os.path.isdir(di):
            yield os.listdir(di)
            for d1 in my_yield_dir(di):
                yield d1
        else:
            continue
    return 'done'


def my_inner_method(x):
    def inner_method():
        nonlocal x
        x = x + 1
        return x

    return inner_method


def log(func):
    # print('1',func.__name__)

    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

def log_param(test,a,b):
    def decorator(func):
        # print('2',func.__name__)
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (test,func.__name__))
            result = func(*args, **kw)
            print('%s %s' % (a,b))
            return result
        return wrapper
    return decorator

# @log
@log_param('execute','after','method')
def my_now():
    print('2023-09-07')



def _private_1(name) -> str:
    return 'Hello %s' % name

def __private_2(name) -> str:
    return 'Hi %s' % name

__abc = 'levi'

abc = 'abc'




