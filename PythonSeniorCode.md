

# PythonSeniorCode

## 一、Python的现状和未来

- python3的发布日期2008.12.03
- [python官方文档](https://www.python.org/dev/peps/pep-0001/)
- 延迟加载模块：延迟加载模块是指在全局导入时并不加载的模块。在Python中，import语句可以包含在函数内部，这入是在函数调用时才会发生，而不是在全局导入时发样导生。在某些情况下,模块的这种加载方式可能比较合理，但大多数情况下,这只是对设计不佳的模块结构的变通方法(例如避免循环导入)，通常应避免这种加载方式。当然，对于标准库模块来说，没有理由使用延迟加载。

## 二、python2.x和python3.x的差异

python2.x 

1. Unicode 需要有`u`前缀（例如u'some string') 
2. str 为字节字符串与python3.x的bytes大部分相同

python3.x 

1. 所有没有前缀的字符串都是Unicode 为保证向后兼容可以使用前缀但无任何语法意义
2. str 不可变序列 保存的是码位 Unicode

>Python字符串是不可变的。字节序列也是如此。这-事实很重要，因为它既有优点又有缺点。它还会影响Python高效处理字符串的方式。由于不变性，字符串可以作为字典的键或set的元素，因为一-. 旦初始化之后字符串的值就不会改变。另-方面，每当需要修改过的字符串时(即使只是微小的修改)，都需要创建一一个 全新的字符串实例。幸运的是，bytearray是bytes的可变版本，不存在这样的问题。字节数组可以通过元素赋值来进行原处修改(无需创建新对象),其大小也可以像列表一样动态地变化(利用append、pop、inseer等方法)。

## 三、类级以下

### 3.1列表推导

常用的for循环生成列表可能适用于C语言，但在Python中的实际运行速度很慢，原因如下。

- 解释器在每次循环中都需要判断序列中的哪一部分需要修改。
- 需要用-一个计数器来跟踪需要处理的元素。
- 由于append()是-一个列表方法，所以每次遍历时还需要额外执行一 一个查询函数。

> 列表推导和内部数组调整大小有些Python程序员中会谣传这样的说法:每添加几个元素之后都要对表示列表对象的内部数组大小进行调整，这个问题可以用列表推导来解决。还有人说一次分配就可以将数组大小调整到刚刚好。不幸的是，这些说法都是不正确的。解释器在对列表推导进行求值的过程中并小。因此，内部数组的重新分配方式与for循环中完不知道最终结果容器的大小，也就无法为它预先分配数组的最终大全相同。但在许多情况下，与普通循环相比，使用列表推导创建列表要更加整洁、更加快速。

### 3.2常用高级函数

- enumerate

```python
list1 = [1,2,3,4]
for i,element in enumerate(list1):
    print(i,element)
```

```sh
0 1
1 2
2 3
3 4
```

- zip

```python
list1 = [1,2,3,4]
list2 = [5,6,7,8]

for i,j in zip(list1,list2):
    print(i,j)
```

```sh
1 5
2 6
3 7
4 8
```

- 序列解包

```python
a,b,c = 1,'2',[3,4]
print(a,b,c)
```

```sh
1 2 [3, 4]
```

带星号的表达式可以获取序列的剩余部分

```python
a,*b,c = 1,2,3,4,5
print(a)
print(b)
print(c)
```

```shell
1
[2, 3, 4]
5
```

嵌套解包

```python
(a,b),(c,d) = (1,[2,3]),(4,5)
print(a)
print(b)
print(c)
print(d)
```

```sh
1
[2, 3]
4
5
```

### 3.3字典

字典的keys()、values ()和items ()3个方法的返回值类型不再是列表。此外，与之对应的iterkeys()、itervalues ()和iteritems ()本来返回的是迭代器，而Python 3中并没有这3个方法。现在keys ()、values ()和items ()返回的是**视图对象(view objects)**。

- keys(): 返回dict_ keys对象，可以查看字典的所有键。
- values():返回dict_ values对象，可以查看字典的所有值。
- items(): 返回dict_ items对象，可以查看字典所有的(key, value)二元元组。

视图对象可以动态查看字典的内容，因此每次字典发生变化时，视图都会相应改变，见下面这个例子:

```python 
a = {
    'a':[1,2,3],
    'b':'4',
}
work = a.items()
key = a.keys()
print(work,key)
a['c']='5'
print(work,key)
```

```sh
dict_items([('a', [1, 2, 3]), ('b', '4')]) dict_keys(['a', 'b'])
dict_items([('a', [1, 2, 3]), ('b', '4'), ('c', '5')]) dict_keys(['a', 'b', 'c'])
```

> 最后一件重要的事情是，在keys ()和values ()方法返回的视图中，键和值的顺序是完全对应的。在Python 2中，如果你想保证获取的键和值顺序一致， 那么在两次函数用之间不能修改字典的内容。现在dict_ keys和dict_ _values是动态的，所以即使在调用keys()和values()之间字典内容发生了变化，那么这两个视图的元素遍历顺序也是完全一致的。

#### 3.3.1 为解决按顺序存储字典

```python
from collections import OrderedDict

o = OrderedDict((number,None) for number in range(5))
print(o.keys())
```

```sh
odict_keys([0, 1, 2, 3, 4])
```

### 3.4集合

集合是一种鲁棒性很好的数据结构，当元素顺序的重要性不如元素的唯--性和测试元素是否包含在集合中的效率时，大部分情况下这种数据结构是很有用的。它与数学上的集合概念非常类似。Python的内置集合类型有两种。

- set(): - -种可变的、无序的、有限的集合，其元素是唯一-的、不可变的(可哈希
- frozenset(): 一种不可变的、可哈希的、无序的集合，其元素是唯- -的、不可变的(可哈希的)对象。

由于frozenset ()具有不变性，它可以用作字典的键，也可以作为其他set()和frozenset()的元素。在一个set() 或frozenset ()中不能包含另一个普通的可变set()，因为这会引发TypeError:

### 3.5超越基础集合类型一 collections模块

- namedtuple(): 用于创建元组子类的工厂 函数(factory function)， 可以通过属性名来访问它的元索引。
- deque: 双端队列，类似列表，是栈和队列的一-般化，可以在两端快速添加或取出元素。
- ChainMap: 类似字典的类，用于创建多个映射的单一 视图。
- Counter:字典子类，由于对可哈希对象进行计数。
- OrderedDict: 字典子类，可以保存元素的添加顺序。
- defaultdict: 字典子类，可以通过调用用户自定义的工厂函数来设置缺失值。

## 四、高级语法

### 4.1迭代器（iterator）

迭代器只不过是-一个实现了迭代器协议的容器对象。它基于以下两个方法。

- \_\_next__ :返回容器的下一个元素。
- \__iter__:返回迭代器本身

```python
class Countdown():
    def __init__(self,step):
        self.step = step

    def __next__(self):
        if self.step<0:
            raise StopIteration
        else:
            self.step-=1
            return self.step
    def __iter__(self):
        return self

c = Countdown(3)
print(c.__iter__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
```

```sh
<__main__.Countdown object at 0x00000000020FC4A8>
2
1
0
```

> for 循环首先找\_\_iter\_\_方法确定是可迭代对象，然后去调用\_\_next__方法
>
> 生成器 ：这个函数返回一个generator对象，是特殊的迭代器，它知道如何保存执行上下文。它可以被无限次调用，每次都会生成序列的下一一个元素。这种语法很简洁，算法可无限调用的性质并没有影响代码的可读性。不必提供使函数停止的方法。实际上，它看上去就像用伪代码设计的数列一样。

### 4.2yield语法

生成器提供了一种优雅的方法， 可以让编写返回元素序列的函数所需的代码变得简单、高效。基于yield语句，生成器可以暂停函数并返回一个中间结果。该函数会保存执行上下文，稍后在必要时可以恢复。

```python
def fibonacci():
    a = 0
    b = 1
    while True:
        yield b
        a,b = b,a+b

f = fibonacci()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
```

```sh
1
1
2
3
```

### 4.3send

```python
def pylist():
    print('place tell me your problems?')
    while True:
        answer = (yield)
        if 'bad' in answer:
            print("Don't so be negative")
        elif 'good' in answer:
            print("That good , go on !")
        elif answer.endswitch('?'):
            print("Don't ask yourself too much questions")

p = pylist()
next(p)
p.send('good')
```

```sh
place tell me your problems?
That good , go on !
```

send的作用和next类似，但会将函数定义内部传入的值变成yield的返回值。因此，这个函数可以根据客户端代码来改变自身行为。为完成这一-行为， 还添加了另外两个函数:throw和close。它们将向生成器抛出错误。

- throw:允许客户端代码发送要抛出的任何类型的异常。
- close:作用相同，但会引发特定的异常一-GeneratorExit。 在这种情况下，生成器函数必须再次引发GeneratorExit或StopIteration。

## 五、装饰器

### 5.1装饰器语法糖和显示的装饰器

```python
# 装饰器的简单定义
import time

def timer(function):
    def wrapped(*args,**kwargs):
        start_time = time.time()
        function(*args,**kwargs)
        end_time = time.time()
        return end_time-start_time
    return wrapped
```

```python
# 装饰器语法糖
@timer
def sayhello():
    print('我是sayhello函数')

# 调用
sayhello()
```

```python
# 显式的装饰器
sayhello = timer(sayhello)

# 调用函数
sayhello()
```

### 5.2作为一个类

```python
def sayhello():
    print('我是sayhello函数')

class SayHello(object):
    def __init__(self,function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # 原始函数调用前做点什么
        result = self.function(*args, **kwargs)
        # 原始函数调用后做点什么
        # 返回结果
        return result
s = SayHello(sayhello)
s()
```

> \_\_call\_\_方法被定义后，类就可以被定义

### 5.3参数化装饰器

```python
def cshzsq(number):
    def cf(function):
        def wrapped(*args,**kwargs):
            result = 0
            for _ in range(number):
                result += function(*args,**kwargs)
            return result
        return wrapped
    return cf

@cshzsq(3)
def he(num1,num2):
    return num2+num1


print(he(1,2))
```

```sh
9
```

> wrapped中的(*args,**kwargs)和function的``(*args,**kwargs)`是指向同一个地址的

### 5.4保存内省的装饰器

使用装饰器的常见错误是在使用装饰器时不保存**函数元数据**(主要是文档字符串和原始函数名)。前面所有示例都存在这个问题。装饰器组合创建了一个新函数，并返回-一个新对象，但却完全没有考虑原始函数的标识。这将会使得调试这样装饰过的函数更加困难，也会破坏可能用到的大多数自动生成文档的工具，因为无法访问原始的文档字符串和函数签名。

正常情况下

```python
def function_with_import_doc(*args,**kwargs):
    """
    这是我们需要的文档
    :param args:
    :param kwargs:
    :return:
    """

print(function_with_import_doc.__name__)
print(function_with_import_doc.__doc__)
```

```sh
function_with_import_doc

    这是我们需要的文档
    :param args:
    :param kwargs:
    :return:
```

问题

```python
def dummy_decorator(function):
    def wrapped(*args,**kwargs):
        """包装函数的内部文档"""
        result = function(*args,**kwargs)
        return result
    return wrapped

@dummy_decorator
def function_with_import_doc(*args,**kwargs):
    """
    这是我们需要的文档
    :param args:
    :param kwargs:
    :return:
    """

print(function_with_import_doc.__name__)
print(function_with_import_doc.__doc__)
```

```sh
wrapped
包装函数的内部文档
```

解决办法

```python
from functools import wraps

def dummy_decorator(function):
    @wraps(function)
    def wrapped(*args,**kwargs):
        """包装函数的内部文档"""
        result = function(*args,**kwargs)
        return result
    return wrapped

@dummy_decorator
def function_with_import_doc(*args,**kwargs):
    # """这是我们需要的文档"""
    """
    这是我们需要的文档
    :param args:
    :param kwargs:
    :return:
    """

print(function_with_import_doc.__name__)
print(function_with_import_doc.__doc__)

```

```sh
function_with_import_doc

    这是我们需要的文档
    :param args:
    :param kwargs:
    :return:
```

### 5.6for......else语句

### 5.7函数注解

```python
def annotation(num1:int,dict1:dict,str1='yu')->int:
    return num1

print(annotation(1,dict1={'s':1}))
print(annotation.__annotations__)
```

```sh
{'num1': <class 'int'>, 'dict1': <class 'dict'>, 'return': <class 'int'>}
```

## 六、类级别以上

### 6.1子类化内置类型

Python的子类化内置类型非常简单。有-一个叫作object的内置类型，它是所有内置类型的共同祖先，也是所有没有显式指定父类的用户自定义类的共同祖先。正由于此，每当需要实现与某个内置类型具有相似行为的类时,最好的方法就是将这个内置类型子类化。

### 6.2访问超类中方法

* 旧式

```python
class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,'cc')

    def yell(self):
        print(self.name+'miao miao miao!!!')
    def s(self):
        Animal.sleep(self)

c = Cat('cc')
c.s()
c.yell()
```

> self 作为当前实例传入，调用类的方法

* 新式 super（）

```python
class Animal(object):
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print("I'm sleeping")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def yell(self):
        print(self.name+'miao miao miao!!!')
    def s(self):
        super().sleep()
class Dog(Animal):
    def yell(self):
        print('wang wang wang!!!')

c = Cat('cc')
c.s()
c.yell()
```

> 在python2.x中有旧时类和新式类，旧式类无法使用super（）函数，在python3.x中写向后兼容的程序时，如果没有继承object 在pyhton2.x中将被解释为旧式类  super（）函数无法执行  python3.x不再保留旧式类的概念，并且都隐性的继承object

* MRO

在python2.x中旧式类，关于菱形继承：从左到右 深度优先  新式类：从左到右 广度优先（MRO，C3算法）

* 混用super和显示类调用

```python
class A():
    def __init__(self):
        print("A")
        super().__init__()

class B():
    def __init__(self):
        print("B")
        super().__init__()

class C(A,B):
    def __init__(self):
        print('C')
        A.__init__(self)
        B.__init__(self)

print(C.mro())
C()
```

```sh
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
C
A
B
B

```

> 产生问题的原因

- 应该避免多重继承:可以采用第14章介绍的一-些设计模式来代替它。
- super的使用必须-致:在类的层次结构中，要么全部用super,要么全不用。混用super: 和传统调用是一种混乱的做法。人们往往会避免使用super这样代码会更清晰
- 如果代码的使用范围包括Python 2，在Python 3中也应该显式地继承自object:在Python 2中，没有指定任何祖先的类被认为是旧式类。在Python 2中应避免混用旧式类和新式类。
- 调用父类时必须查看类的层次结构:为了避免出现任何问题，每次调用父类时，必须快速查看有关的MRO (使用_ mro_ )。

### 6.3高级属性访问模式

#### 6.3.1property 内置数据描述符

```python
class Rectangle():
    def __init__(self,x1,y1,x2,y2):
        self.x1,self.y1 = x1,y1
        self.x2,self.y2 = x2,y2

    def _width_get(self):
        return self.x2 - self.x1

    def _width_set(self,value):
        self.x2 = self.x1+value

    def _height_get(self):
        return self.y2-self.y1

    def _height_set(self,value):
        self.y2 = self.y1 + value

    @property
    def height(self):
        """rectangle height measured from top"""
        return self.y2-self.y1

    @height.setter
    def height(self,value):
        self.y2=self.y1+value

    @height.deleter
    def height(self):
        del self.height

    width = property(
        _width_get,_width_set,
        doc="rectangle width measured from left"
    )
    # height = property(
    #     _height_get, _height_set,
    #     doc="rectangle height measured from top"
    # )

    def __repr__(self):
        return "{}({},{},{},{})".format(
            self.__class__.__name__,
            self.x1,self.y1,self.x2,self.y2
        )

if __name__ == '__main__':
    rectangle = Rectangle(10,10,25,34)
    print(rectangle.width)
    rectangle.width=100
    print(rectangle.width)
    print(rectangle.x1,rectangle.x2)
    print(rectangle)

```

#### 6.3.2描述符

描述符(descriptor) 允许你自定义在引用-一个对象的属性时应该完成的事情。描述符是Python中复杂属性访问的基础。它在内部被用于实现property、方法、类方法、静态方法和susupeer类型。它是-一个类，定义了另一个类的属性的访问方式。换句话说，一个类可以将属性管理委托给另一个类。描述符类基于3个特殊方法，这3个方法组成了描述符协议( descriptor protocol):

* _set__ (self, obj, type=None): 在设置属性时将调用这一 方法。在下面的示例中，我们将其称为setter.

- _ get__ (self, obj, value):在读取属性时将调用这一 方法(被称为getter)。
- _ delete__ (self, obj):对属性调用de1时将调用这一方法。

实现了\_\_get\_\_ ()和_ set_\_() 的描述符被称为数据描述符( data descriptor)。如果只实现了\_\_get\_\_ ()， 那么就被称为非数据描述符(non-data descriptor)。

```python
class A():
    def __init__(self,initval=None,name='var'):
        self.name = name
        self.val = initval

    def __get__(self, instance, owner):
        print('retrieing', self.name)
        return self.val

    def __set__(self, instance, value):
        print('seting',self.name,self.val)

    def __del__(self):
        print('del')

class X():
    x = A(10,'var x')

x = X()
x.x=20
print(x.x)
```

```sh
seting var x 10
retrieing var x
10
del

```

#### 6.3.3槽

```python
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
```



### 6.4元编程

#### 6.4.1类装饰器

```python
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

```

