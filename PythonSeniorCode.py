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


def sayhello(*args,**kwargs):
    print(args)
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


class B():
    __slots__ = ['ice','cream']

b = B()
b.ice = False
b.cream = True
b.icy = False


print(dir(B))
a = B()
print(dir(a))

class C(B):
    pass
c= C()
c.icy = False
c.ss = 'ss'
print(c.icy)
print(dir(c))

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
# class C(A,B):
#     def __init__(self):
#         print('C')
#         A.__init__(self)
#         B.__init__(self)
#
# print(C.mro())
# C()


def parametrized_short_repr(max_width=8):
    "缩短表示的参数化装饰器"
    def parametrized(cls):
        """内部包装函数，是实际的装饰器"""
        class ShortlyRepresented(cls):
            """提供装饰器行为的子类"""
            def __repr__(self):
                return super() .__repr__()[:max_width]
        return ShortlyRepresented
    return parametrized









