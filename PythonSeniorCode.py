# # 装饰器
# # import time
# #
# # def timer(function):
# #     def wrapped(*args,**kwargs):
# #         start_time = time.time()
# #         function(*args,**kwargs)
# #         end_time = time.time()
# #         return end_time-start_time
# #     return wrapped
# #
# # @timer
# from urllib import request
# from threading import Thread


# def sayhello(*args,**kwargs):
#     print(args)
# #
# # sayhello()
# #
# # sayhello = timer(sayhello)
# #
# # print(sayhello())
#
# class SayHello(object):
#     def __init__(self,function):
#         self.function = function
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         args = (1,2,3,4)
#         self.function(*args, **kwargs)
#
#     def ss(self):
#         print('我是SayHello类的ss函数')
#
#     def s(self):
#         self.function()
# s = SayHello(sayhello)
# # print(s.ss())
# s(1,2,3)
#
# def function_with_import_doc(*args,**kwargs):
#     """
#     这是我们需要的文档
#     :param args:
#     :param kwargs:
#     :return:
#     """
#
# print(function_with_import_doc.__name__)
# print(function_with_import_doc.__doc__)
#
# def dummy_decorator(function):
#     def wrapped(*args,**kwargs):
#         """包装函数的内部文档"""
#         result = function(*args,**kwargs)
#         return result
#     return wrapped
#
# @dummy_decorator
# def function_with_import_doc(*args,**kwargs):
#     """
#     这是我们需要的文档
#     :param args:
#     :param kwargs:
#     :return:
#     """
#
# print(function_with_import_doc.__name__)
# print(function_with_import_doc.__doc__)
#
#
# from functools import wraps
#
# def dummy_decorator(function):
#     @wraps(function)
#     def wrapped(*args,**kwargs):
#         """包装函数的内部文档"""
#         result = function(*args,**kwargs)
#         return result
#     return wrapped
#
# @dummy_decorator
# def function_with_import_doc(*args,**kwargs):
#     # """这是我们需要的文档"""
#     """
#     这是我们需要的文档
#     :param args:
#     :param kwargs:
#     :return:
#     """
#
# print(function_with_import_doc.__name__)
# print(function_with_import_doc.__doc__)
#
#
# # def my_decorator(function):
# #     def wrapped(*args,**kwargs):
# #         a1 = args
# #         function(*args,**kwargs)
# #         a2 = args
# #         if a1 is a2 :
# #             print('yes')
# #     return wrapped
# #
# #
# # @my_decorator
# # def hello(*args):
# #     pass
# # hello(1,2,3)

# def cshzsq(number):
#     def cf(function):
#         def wrapped(*args,**kwargs):
#             result = 0
#             for _ in range(number):
#                 result += function(*args,**kwargs)
#             return result
#         return wrapped
#     return cf
#
# @cshzsq(3)
# def he(num1,num2):
#     return num2+num1
#
#
# print(he(1,2))

# with
# class ContextIllustration():
#     def __enter__(self):
#         print('entering content')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('leaving context')
#         if exc_type is None:
#             print('no error')
#         else:
#             print('with an error {}'.format(exc_val))

# with ContextIllustration():
#     raise RuntimeError('raised within "with"')

# def annotation(num1:int,dict1:dict,str1='yu')->int:
#     return num1
#
# print(annotation(1,dict1={'s':1}))
# print(annotation.__annotations__)

# 迭代器
# class itertable():
#     def __init__(self,step):
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):


# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield b
#         a,b = b,a+b
#
# f = fibonacci()
# print([next(f) for _ in range(10)])
# print([next(f) for _ in range(10)])
# print([next(f) for _ in range(10)])
# class Mama(object):
#
#     def say(self):
#         print('do your home work')
#
# class Myself(Mama):
#     def mamasay(self):
#         super().say()
#
# m = Myself()
# m.mamasay()
#
# super(m.__class__,m).mamasay()

# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#     def sleep(self):
#         print("I'm sleeping")
#
# class Cat(Animal):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def yell(self):
#         print(self.name+'miao miao miao!!!')
#     def s(self):
#         super().sleep()

#
# c = Cat('cc')
# c.s()
# c.yell()
# class B():
#     pass
# class Animal(B):
#     def __init__(self,name):
#         self.name = name
#     def sleep(self):
#         print("I'm sleeping")
#
# class Dog(Animal):
#     def yell(self):
#         print('wang wang wang!!!')
# class A():
#     pass
# class Cat(Dog,A):
#     def __init__(self,name):
#         Animal.__init__(self,'cc')
#
#     def yell(self):
#         print(self.name+'miao miao miao!!!')
#     def s(self):
#         Animal.sleep(self)
# def L(myclass):
#     return [k.__name__ for k in myclass.__mro__]
#
#
# print(L(Cat))
# class O():
#     pass
# class A(O):
#     def say(self):
#         print('A')
# class B(A):
#     # def say(self):
#     #     print("B")
#     pass
#
# class C(A):
#     def say(self):
#         print('C')
#
# class D(B,C):
#     pass

# d = D()
# d.say()
#
# print(D.mro())
#
# def L(myclass):
#     return [k.__name__ for k in myclass.__mro__]
#
# print(L(D))

# class A():
#     def __init__(self):
#         print('A')
#         super().__init__()
#
# class B():
#     def __init__(self):
#         print('B')
#         super().__init__()
#
# class C(A,B):
#     def __init__(self):
#         print("C")
#         A.__init__(self)
#         input()
#         B.__init__(self)
# C()
#
# class A():
#     def __init__(self,initval=None,name='var'):
#         self.name = name
#         self.val = initval
#
#     def __get__(self, instance, owner):
#         print('retrieing', self.name)
#         return self.val
#
#     def __set__(self, instance, value):
#         print('seting',self.name,self.val)
#
#     def __del__(self):
#         print('del')
#
# class X():
#     x = A(10,'var x')
#
# x = X()
# x.x=20
# print(x.x)

# class Rectangle():
#     def __init__(self,x1,y1,x2,y2):
#         self.x1,self.y1 = x1,y1
#         self.x2,self.y2 = x2,y2
#
#     def _width_get(self):
#         return self.x2 - self.x1
#
#     def _width_set(self,value):
#         self.x2 = self.x1+value
#
#     def _height_get(self):
#         return self.y2-self.y1
#
#     def _height_set(self,value):
#         self.y2 = self.y1 + value
#
#     @property
#     def height(self):
#         """rectangle height measured from top"""
#         return self.y2-self.y1
#
#     @height.setter
#     def height(self,value):
#         self.y2=self.y1+value
#
#     @height.deleter
#     def height(self):
#         del self.height
#
#     width = property(
#         _width_get,_width_set,
#         doc="rectangle width measured from left"
#     )
#     # height = property(
#     #     _height_get, _height_set,
#     #     doc="rectangle height measured from top"
#     # )
#
#     def __repr__(self):
#         return "{}({},{},{},{})".format(
#             self.__class__.__name__,
#             self.x1,self.y1,self.x2,self.y2
#         )
#
# if __name__ == '__main__':
#     rectangle = Rectangle(10,10,25,34)
#     print(rectangle.width)
#     rectangle.width=100
#     print(rectangle.width)
#     print(rectangle.x1,rectangle.x2)
#     print(rectangle)


# class A():
#     def __init__(self,name):
#         self.name = name
#
# a = A('yu')
# print(dir(a))
# print(a.__dict__)


# class B():
#     __slots__ = ['ice','cream']
#
# b = B()
# b.ice = False
# b.cream = True
# b.icy = False
#
#
# print(dir(B))
# a = B()
# print(dir(a))
#
# class C(B):
#     pass
# c= C()
# c.icy = False
# c.ss = 'ss'
# print(c.icy)
# print(dir(c))

# class A():
#     def __init__(self):
#         self.name = 'yu'
#     def say(self):
#         print("hello")
#
# def short_repr(cls):
#     cls.__repr__ = lambda self: super(cls,self).__repr__()[:3]
#     return cls
#
# @short_repr
# class ABCDEFGHIJK():
#     pass


# class A():
#     def __init__(self):
#         print("A")
#         super().__init__()
#
# class B():
#     def __init__(self):
#         print("B")
#         super().__init__()
#
# class D():
#     def __init__(self):
#         print("D")
#         super().__init__()
#
# class C(A,B,D):
#     def __init__(self):
#         print('C')
#         A.__init__(self)
#         B.__init__(self)
#         D.__init__(self)
#
# print(C.mro())
# C()


# def parametrized_short_repr(max_width=8):
#     "缩短表示的参数化装饰器"
#     def parametrized(cls):
#         """内部包装函数，是实际的装饰器"""
#         class ShortlyRepresented(cls):
#             """提供装饰器行为的子类"""
#             def __repr__(self):
#                 return super() .__repr__()[:max_width]
#         return ShortlyRepresented
#     return parametrized

# def parametrized_short_repr(max_width=8):
#     "缩短表示的参数化装饰器"
#     def parametrized(cls):
#         """内部包装函数，是实际的装饰器"""
#         class ShortlyRepresented(cls):
#             """提供装饰器行为的子类"""
#             def __repr__(self):
#                 return super() .__repr__()[:max_width]
#         return ShortlyRepresented
#     return parametrized
#
# class B():
#     def __repr__(self):
#         return 'Bsdhjakhjkasdhjkdkhas'
#
# @parametrized_short_repr()
# class A(B):
#     pass
#
# print(A().__repr__())

# class A():
#     def __new__(cls,value,*args, **kwargs):
#         return super().__new__(cls) if value != 0 else None
#
#     def __init__(self,value):
#         print('initing ',value)
#
# A(0)

# def method(self):
#     return 1
#
# klass = type('MyClass',(object,),{'method':method})
#
# instance = klass()
# print(instance.method())

# class MyClass():
#     def method(self):
#         return 1
#
# instance = MyClass()
# print(instance.method())

# class A(metaclass=)


# b = type('B',(object,),{'want':'money'})
# print(b.__name__)
# class A(B):
#     pass
#
# a = A()
# print(a.want)

# class A(metaclass=type):
#     '这是A类'
#     pass


# print(A.__name__)
# print(A.__bases__)
# print(A.__dict__)

# class A():
#     def __new__(cls, *args, **kwargs):
#         pass
#     @classmethod
#     def __prepare__(metacls, name, bases):

# def a():
#     print('hello')
#
# eval('print("hello")')


# print(eval('"A" if 0<-1 else "B"'))

# print(globals())

# def a():
#     a=1
#     b=2
#     loc = locals()
#     print(loc)
    # exec('c = a+b')
    # c= loc['c']
    # print(c)

# a()
# exec ('print("hello")')
# exec("""
# print('hello')
# """)
# pre = 'print("hello",a,b)'
# exec(pre,{'a':2,'b':3})
# str1 = 'for i in range(10):print(i)'
# c = compile(str1,'','exec')
# exec(c)
# def a(**kwargs):
#     print(kwargs['cc'])
#
# a(cc='ss')

# def a(b,c):
#     assert isinstance(b,(int,float)),'类型错误'
#     print(b,c)
#
# a('2',2)

# from threading import Thread
# import time
#
# def say_hello():
#
#     for i in range(10):
#         time.sleep(0.2)
#         print("hello world")
#
# def say_dance():
#
#     for j in range(10):
#         time.sleep(0.2)
#         print("dancing")



# t_list = [Thread(target=say_hello),Thread(target=say_dance)]
# [t.start() for t in t_list]

# [t.start() for t in [t1,t2]]
# for t in t_list:
#     t.start()

# from gmaps import Geocoding
#
# api = Geocoding()
#
# geocoded = api.geocode('Warsaw')[0]
# print(geocoded)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
#
# def query(lat, loc):
#     url = "http://maps.google.cn/maps/api/geocode/xml?latlng=%.6f,%.6f&sensor=false" % (lat, loc)
#     html = urlopen(url)
#     bsObj = BeautifulSoup(html, "html.parser")
#     addr = bsObj.find('formatted_address')
#     return addr
#
#
# print(query(26.567175,106.71545))


# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# # 等待至线程终止
# thread1.join()
# thread2.join()
# print ("退出主线程")

"""
开始线程：Thread-1
开始线程：Thread-2
Thread-1: Mon Aug 17 13:54:44 2020
Thread-1: Mon Aug 17 13:54:45 2020
Thread-2: Mon Aug 17 13:54:45 2020
Thread-1: Mon Aug 17 13:54:46 2020
Thread-1: Mon Aug 17 13:54:47 2020
Thread-2: Mon Aug 17 13:54:47 2020
Thread-1: Mon Aug 17 13:54:48 2020
退出线程：Thread-1
Thread-2: Mon Aug 17 13:54:49 2020
Thread-2: Mon Aug 17 13:54:51 2020
Thread-2: Mon Aug 17 13:54:53 2020
退出线程：Thread-2
退出主线程
"""
import time
from multiprocessing.queues import Queue

"""
开始线程：Thread-1
开始线程：Thread-2
退出主线程
Thread-1: Mon Aug 17 13:55:10 2020
Thread-2: Mon Aug 17 13:55:11 2020
Thread-1: Mon Aug 17 13:55:11 2020
Thread-1: Mon Aug 17 13:55:12 2020
Thread-1: Mon Aug 17 13:55:13 2020
Thread-2: Mon Aug 17 13:55:13 2020
Thread-1: Mon Aug 17 13:55:14 2020
退出线程：Thread-1
Thread-2: Mon Aug 17 13:55:15 2020
Thread-2: Mon Aug 17 13:55:17 2020
Thread-2: Mon Aug 17 13:55:19 2020
退出线程：Thread-2
"""

# import queue
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

# from threading import Thread
# import threading

# threadLock = threading.Lock()
#
# threadLock.locked()
#
# threadLock.release()

# from threading import Thread
# import time,threading
# import os
#
# def sing():
#     for i in range(10):
#         time.sleep(1)
#         print("I'm singing and {} and {}".format(os.getpid(),threading.current_thread().name))
#
# def dance():
#     for i in range(10):
#         time.sleep(1)
#         print("I'm dancing and {} and {}".format(os.getpid(),threading.current_thread().name))
#
# t1 = Thread(target=sing,name='t1')
# t2 = Thread(target=dance,name='t2')
#
# t1.start()
# t2.start()



# from threading import Thread
# import time
# import threading
# import os
#
# TICKET =10
# threading_lock = threading.Lock()
#
# def sell_1():
#     global TICKET
#     while True:
#         threading_lock.acquire()
#         if TICKET>0:
#             time.sleep(0.3)
#             TICKET-=1
#             threading_lock.release()
#             print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
#         else:
#             print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET, os.getpid(), threading.current_thread().name))
#             threading_lock.release()
#             break
#
#
# def sell_2():
#     global TICKET
#     while True:
#         threading_lock.acquire()
#         if TICKET>0:
#             time.sleep(0.3)
#             TICKET-=1
#             threading_lock.release()
#             print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
#         else:
#             print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET, os.getpid(), threading.current_thread().name))
#             threading_lock.release()
#             break
#
# t1 = Thread(target=sell_1,name='t1')
# t2 = Thread(target=sell_2,name='t2')
#
# t1.start()
# t2.start()

from threading import Thread
# import time
# import threading
# import queue
#
# q = queue.Queue()
#
# def produce():
#     for i in range(10):
#         time.sleep(2)
#         q.put('b{}'.format(i))
#         print('+++生产面包b{}'.format(i))
#
# def consumer():
#     while True:
#         time.sleep(0.6)
#         print("---购买面包 {}".format(q.get()))
#
# produce_t = threading.Thread(target=produce,name='produce_t')
# consumer_t = threading.Thread(target=consumer,name='consumer')
#
# produce_t.start()
# consumer_t.start()


# import multiprocessing
# import os
# import time
#
# def sing():
#     for i in range(10):
#         time.sleep(1)
#         print("I'm singing and {}".format(os.getpid()))
#
# def dance():
#     for i in range(10):
#         time.sleep(1)
#         print("I'm dancing and {}".format(os.getpid()))
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=sing,name='t1')
#     p2 = multiprocessing.Process(target=dance,name='t2')
#
#     p1.start()
#     p2.start()

# import multiprocessing
# import os
# import time
#
# q = multiprocessing.Queue(2)
#
# def produce(q:Queue):
#     for i in range(10):
#         time.sleep(0.3)
#         q.put('b{}'.format(i))
#         print('生产++++++b{} and {}'.format(i,os.getpid()))
#
# def consumer(q):
#     for i in range(10):
#         time.sleep(0.6)
#         print('买面包---------{} and {}'.format(q.get(),os.getpid()))
#
# if __name__ == '__main__':
#
#     p1 = multiprocessing.Process(target=produce,args=(q,))
#     p2 = multiprocessing.Process(target=consumer,args=(q,))
#
#     p1.start()
#     p2.start()
import time

import sympy   # 引入解方程的专业模块sympy
# x = sympy.symbols("x")   # 申明未知数"x"
# a = sympy.solve([x+(1/5)*x-240],[x])   # 写入需要解的方程体
# print(a)  # 打印出结果

# r = sympy.symbols('r')
# result = sympy.solve([(100/(1+r))+(100/(1+r)**2)])


import queue
import multiprocessing

# q1 = queue.Queue()           # 线程间通信
# q2 = multiprocessing.Queue()  # 进程间通信

# q = multiprocessing.Queue(5)
# q.put('1')
# q.put('2')
# q.put('3')
# q.put('4')
# q.put('5')
# q.get()
# q.put('6')

# import threading
# x = 10
#
# def he(a,b):
#     time.sleep(1)
#     global x
#     x = a+b
#
# t1 = threading.Thread(target=he,args=(1,1))
# t1.start()
# print(x)
#
# t1.join()
#
# print(x)


# class test_await():
#     def __init__(self,time_):
#         time.sleep(time_)
#     def __await__(self):
#         yield
#
# async def washer_1():
#     close_time = 2
#     await asyncio.sleep(close_time)
#     await test_await(close_time)
#     print('washer_1 lose {} seconds'.format(close_time))
#
# async def washer_2():
#     close_time = 3
#     # await asyncio.sleep(close_time)
#     await test_await(close_time)
#     print('washer_2 lose {} seconds'.format(close_time))
#
# async def washer_3():
#     close_time = 1
#     # await asyncio.sleep(close_time)
#     await test_await(close_time)
#     print('washer_3 lose {} seconds'.format(close_time))
#
# if __name__ == '__main__':
#
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([washer_1(),washer_2(),washer_3()]))
#     loop.close()
#     end_time = time.time()
#     print(end_time-start_time)




# import asyncio
# import time
# import random
#
# async def saynumber(number):
#     wait_time = random.randint(1,4)/4
#     time.sleep(wait_time)
#     print(number,wait_time)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(
#     asyncio.wait([
#         saynumber(number) for number in range(10)
#     ])
# )
#
#
# loop.close()
# print('hello world')
#
# import asyncio
# import time
# import random
#
# async def waiter(name):
#     for _ in range(4):
#         time_to_sleep = random.randint(1,8)/4
#         time.sleep(time_to_sleep)
#         print(
#             "{} waited {} seconds".format(name,time_to_sleep)
#         )
#
# async def main():
#     await asyncio.wait([waiter("foo"),
#                         waiter("bar")])
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

#
# import asyncio
# import time
# import random
#
# async def waiter(name):
#     for _ in range(4):
#         time_to_sleep = random.randint(1,8)/4
#         await asyncio.sleep(time_to_sleep)
#         print(
#             "{} waited {} seconds".format(name,time_to_sleep)
#         )
#
# async def main():
#     await asyncio.wait([waiter("foo"),
#                         waiter("bar")])
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()
#
# def a():
#     for i in range(10):
#         yield i
#
# b =a()
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

# import asyncio
# import time
#
# async def wash_1():
#     spend_time = 2
#     await asyncio.sleep(spend_time)
#     print('washer_1 spend {} seconds'.format(spend_time))
#
# async def wash_2():
#     spend_time = 2
#     await asyncio.sleep(spend_time)
#     print('washer_2 spend {} seconds'.format(spend_time))
#
# async def wash_3():
#     spend_time = 2
#     await asyncio.sleep(spend_time)
#     print('washer_3 spend {} seconds'.format(spend_time))
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([wash_1(),wash_2(),wash_3()]))
#     end_time = time.time()
#     print('spend {} seconds'.format(end_time-start_time))

# import asyncio
# import time
#
# class Test():
#     def __init__(self):
#         self.content = []
#         for i in range(10):
#             if i%3==0:
#                 self.content.append(i)
#                 asyncio.sleep(9)
#
#
#
#     def __await__(self):
#         yield
#
#
# async def wash_1():
#
#     await Test()
#     print('washer_1')
#
# async def wash_2():
#     spend_time = 2
#     await Test()
#     print('washer_2')
#
# async def wash_3():
#     spend_time = 2
#     await Test()
#     print('washer_3')
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([wash_1(),wash_2(),wash_3()]))
#     end_time = time.time()
#     print('spend {} seconds'.format(end_time-start_time))


# start_time = time.time()
# list1 = []
# for i in range(10000000):
#     list1.append(i)
# end_time = time.time()
# print('spend {} seconds'.format(end_time-start_time))

# import sys
#
# print('hello world!!!')
#
# if __name__ == '__main__':
#     file_name = sys.argv[1]
#     print('file_name : {}'.format(file_name))

import asyncio
import time

async def get(url,page=2):
    if page==5:
        return
    print('---get_start----',page)
    await asyncio.sleep(2)
    print('----end_get------',page)
    await parse('',page)
    page+=1
    await get(url,page)

async def post(url,page_post=2):
    if page_post>=5:
        return
    print('---post_start----', page_post)
    await asyncio.sleep(2)
    print('----end_post------', page_post)
    await parse('', page_post)
    page_post += 1
    await get(url, page_post)


async def parse(html,page):
    print('---start_parse----',page)
    await asyncio.sleep(1)
    print('---end_parse---',page)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        get('http://'),post('https://')
    ]))
    end_time = time.time()
    print(end_time-start_time)



