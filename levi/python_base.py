# _*_ coding: utf-8 _*_


# print(100 ** 2)
# print('hello, world','levi.ding',sep='.')
# print(dir(int))
# print(help(int.__ceil__(11)))
# print('100 + 200 = ',100+200)
# print(input('随便输入吧！'))
import decimal
import fractions

# try:
#     a = eval(input('输入数字:'))
# except:
#     print('请输入数字')
#     exit(0)
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# a = 'ABC'
# b = a
# print(b)
# a = 'EDF'
# print(b)

# print(10/3)
# print(9/3)
# print(10//3)

# print('Hello, "Bart"')
# print(r'\'')

# print(ord('中'))

# print(u'中文')

# print('Hello, %s, %d' % ('World',1))

# print('%.2f/%.2f' % (10,3))

# names = ('levi','ding','yan','kui')
# for name in names:
#     print(name)

# print(list(range(1,5)))

# for i in range(1,5):
#     print(i)

# n = 0
# while n<=10:
#     print('测试一下 n:%d' % n)
#     n+=1
#     if n>5:
#         continue
#     if n>5 :
#         break

# d = {'levi':1,1:'levi',2:['测试']}
# print(d['levi'])
# d['测试v一下'] = 1
# print('levi' in d)
# print(d[[1]])
# print(d.get(1,'测试一下类型'))
# d[[1]] = '1'
# print(d.pop(1))
# print(d)

# print(max(list(range(100000))))

# a = abs
# print(a(-1))

# def my_abs(x):
#     if x >=0 :
#         return x
#     else :
#         return -x
# print(my_abs(-3))
import functools
from collections.abc import Iterator
from functools import reduce

from levi.module.test import test
from levi.python_method import my_abs, my_pass, my_if_pass, my_more_response, my_more_param, my_change_param, \
    my_key_param, my_yield_dir, my_inner_method, my_now, log, log_param, _private_1, __private_2, __abc, abc

# print(my_abs(-3))
# print(my_pass())
# print(my_if_pass(-3))
# # print(my_abs(''))
# print(type(my_more_response()))
# a,b = my_more_response()
# print(a)
# print(b)
# print(my_more_param(1,2,3))
# print(my_more_param(1,2,3))
# my_change_param(1,2,3,2,4,6, a=1)
# my_change_param(1,2,3,1,b=2,c=3)
# my_key_param(1,2,3,2,a=1,b=2)


# L = list(range(1,10))
# print(L)
# print(L[::2])

#
# for i,value in enumerate(range(1,100)):
#     print(i,value)

# print([x * x for x in range(1, 11)])

# print([i+1 for i in range(10)])

# print([i * 10 for i in range(10) if i > 5])

# print([k+str(y) for k,y in {'a' : 1,'b' : 2}.items() if k == 'a'])

# print([l[0:2] for l in [[1,2],[3,4],[5,6]]])

# print([l if not isinstance(l,list) else l[1] for l in [[1,2],[3,4],[5,6]]] )


# for d in my_yield_dir('/Users/levi.ding/Documents/project/LearnPython_1/MyShow'):
#     print(d)
#
# L = [1] + [2]
# print(L)

# print(isinstance((r for r in range(10)),Iterator))

# print(list(map(abs,(-1,-2,-3))))

# print(reduce(lambda x,y : x*y*10,(1,2,3,4,5)))

# print(list(filter(lambda i : i > 0,range(-10,10))))

# a = 1
# print(my_inner_method(a)())
# print(my_inner_method(a)())

# log(my_now)()

# my_now()
# now = log_param('execute')(my_now)
# print(now.__name__)

# my_now()

# int2 = functools.partial(int, base=2)
# print(int2('10'))
# int('10',{'base' : 2})

# test()

#
# print(_private_1('1'))
#
# print(__private_2('2'))
#
# print(__abc)
#
# print(abc)