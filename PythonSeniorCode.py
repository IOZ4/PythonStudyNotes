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

'''
MTW881U3Z5-eyJsaWNlbnNlSWQiOiJNVFc4ODFVM1o1IiwibGljZW5zZWVOYW1lIjoiTnNzIEltIiwiYXNzaWduZWVOYW1lIjoiIiwiYXNzaWduZWVFbWFpbCI6IiIsImxpY2Vuc2VSZXN0cmljdGlvbiI6IkZvciBlZHVjYXRpb25hbCB1c2Ugb25seSIsImNoZWNrQ29uY3VycmVudFVzZSI6ZmFsc2UsInByb2R1Y3RzIjpbeyJjb2RlIjoiSUkiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJBQyIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkRQTiIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IlBTIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiR08iLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJETSIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkNMIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUlMwIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUkMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJSRCIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IlBDIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiUk0iLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJXUyIsInBhaWRVcFRvIjoiMjAxOS0xMS0wNiJ9LHsiY29kZSI6IkRCIiwicGFpZFVwVG8iOiIyMDE5LTExLTA2In0seyJjb2RlIjoiREMiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifSx7ImNvZGUiOiJSU1UiLCJwYWlkVXBUbyI6IjIwMTktMTEtMDYifV0sImhhc2giOiIxMDgyODE0Ni8wIiwiZ3JhY2VQZXJpb2REYXlzIjowLCJhdXRvUHJvbG9uZ2F0ZWQiOmZhbHNlLCJpc0F1dG9Qcm9sb25nYXRlZCI6ZmFsc2V9-aKyalfjUfiV5UXfhaMGgOqrMzTYy2rnsmobL47k8tTpR/jvG6HeL3FxxleetI+W+Anw3ZSe8QAMsSxqVS4podwlQgIe7f+3w7zyAT1j8HMVlfl2h96KzygdGpDSbwTbwOkJ6/5TQOPgAP86mkaSiM97KgvkZV/2nXQHRz1yhm+MT+OsioTwxDhd/22sSGq6KuIztZ03UvSciEmyrPdl2ueJw1WuT9YmFjdtTm9G7LuXvCM6eav+BgCRm+wwtUeDfoQqigbp0t6FQgkdQrcjoWvLSB0IUgp/f4qGf254fA7lXskT2VCFdDvi0jgxLyMVct1cKnPdM6fkHnbdSXKYDWw==-
MIIElTCCAn2gAwIBAgIBCTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTE4MTEwMTEyMjk0NloXDTIwMTEwMjEyMjk0NlowaDELMAkGA1UEBhMCQ1oxDjAMBgNVBAgMBU51c2xlMQ8wDQYDVQQHDAZQcmFndWUxGTAXBgNVBAoMEEpldEJyYWlucyBzLnIuby4xHTAbBgNVBAMMFHByb2QzeS1mcm9tLTIwMTgxMTAxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxcQkq+zdxlR2mmRYBPzGbUNdMN6OaXiXzxIWtMEkrJMO/5oUfQJbLLuMSMK0QHFmaI37WShyxZcfRCidwXjot4zmNBKnlyHodDij/78TmVqFl8nOeD5+07B8VEaIu7c3E1N+e1doC6wht4I4+IEmtsPAdoaj5WCQVQbrI8KeT8M9VcBIWX7fD0fhexfg3ZRt0xqwMcXGNp3DdJHiO0rCdU+Itv7EmtnSVq9jBG1usMSFvMowR25mju2JcPFp1+I4ZI+FqgR8gyG8oiNDyNEoAbsR3lOpI7grUYSvkB/xVy/VoklPCK2h0f0GJxFjnye8NT1PAywoyl7RmiAVRE/EKwIDAQABo4GZMIGWMAkGA1UdEwQCMAAwHQYDVR0OBBYEFGEpG9oZGcfLMGNBkY7SgHiMGgTcMEgGA1UdIwRBMD+AFKOetkhnQhI2Qb1t4Lm0oFKLl/GzoRykGjAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBggkA0myxg7KDeeEwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgWgMA0GCSqGSIb3DQEBCwUAA4ICAQAF8uc+YJOHHwOFcPzmbjcxNDuGoOUIP+2h1R75Lecswb7ru2LWWSUMtXVKQzChLNPn/72W0k+oI056tgiwuG7M49LXp4zQVlQnFmWU1wwGvVhq5R63Rpjx1zjGUhcXgayu7+9zMUW596Lbomsg8qVve6euqsrFicYkIIuUu4zYPndJwfe0YkS5nY72SHnNdbPhEnN8wcB2Kz+OIG0lih3yz5EqFhld03bGp222ZQCIghCTVL6QBNadGsiN/lWLl4JdR3lJkZzlpFdiHijoVRdWeSWqM4y0t23c92HXKrgppoSV18XMxrWVdoSM3nuMHwxGhFyde05OdDtLpCv+jlWf5REAHHA201pAU6bJSZINyHDUTB+Beo28rRXSwSh3OUIvYwKNVeoBY+KwOJ7WnuTCUq1meE6GkKc4D/cXmgpOyW/1SmBz3XjVIi/zprZ0zf3qH5mkphtg6ksjKgKjmx1cXfZAAX6wcDBNaCL+Ortep1Dh8xDUbqbBVNBL4jbiL3i3xsfNiyJgaZ5sX7i8tmStEpLbPwvHcByuf59qJhV/bZOl8KqJBETCDJcY6O2aqhTUy+9x93ThKs1GKrRPePrWPluud7ttlgtRveit/pcBrnQcXOl1rHq7ByB8CFAxNotRUYL9IF5n3wJOgkPojMy6jetQA5Ogc8Sm7RG6vg1yow==

'''














