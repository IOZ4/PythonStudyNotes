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
print(super)















