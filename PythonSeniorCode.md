

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

#### 6.2.1旧式

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

#### 6.2.2新式 super（）

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

#### 6.2.3python的继承规则总结

在python2.x中旧式类，关于菱形继承：从左到右 深度优先  新式类：从左到右 广度优先（MRO，C3算法）

#### 6.2.4混用super和显示类调用产生的问题

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

> 这是python自身的特性也算是坑吧，python的多继承和其他语言相比是有问题的，python会优先继承A类，而B类会默认被底层处理成更高一级，你试一下把C的继承顺序颠倒一下，A类就会被底层默认处理成更高一级 。在结构上A和B是同级  但是那个继承关系列表中其实也是代表了等级关系。Python的多继承是讲究就近原则的

#### 6.2.5解决办法

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

class B():
    def __repr__(self):
        return 'Bsdhjakhjkasdhjkdkhas'

@parametrized_short_repr()
class A(B):
    pass

print(A().__repr__())

```

#### 6.4.2使用\_\_new\_\_方法覆写实例创建过程

#### 6.4.3元类

[一篇好的元类解释文章](https://www.jianshu.com/p/c1ca0b9c777d)

```python
def method(self):
    return 1

klass = type('MyClass',(object,),{'method':method})

instance = klass()
print(instance.method())
```

> type(\_\_name\_\_,bases,\_\_dict\_\_)  类名  父类列表  属性、方法字典

## 七、并发

如果两个事件互不影响，则两个事件是并发的。

### 7.1什么是多线程

线程是执行线程的缩写。程序员可以将他或她的工作拆分到线程中，这些线程同时运行并共享同一内存上下文。除非你的代码依赖第三方资源，否则多线程不会在单核处理器上加速，甚至会增加线程管理的开销。多线程得益于多处理器或多核机器，将在每个CPU核上并行化每个线程执行，从而使程序更快。请注意，这是一个通用规则，应该适用于大多数的编程语言。

### 7.2多线程常见问题

* 竞争冒险

如果两个线程更新相同的没有任何保护的数据，则会发生竞态条件。这被称为竞争冒险(racehazard),这里可能发生意外的结果，因为每个线程运行的代码对数据的状态做出了错误的假设。

* 锁机制有助于保护数据，在多线程编程中，总是要确保线程以安全的方式访问资源。
* 死锁

两个线程锁定一个 资源，并尝试获取另-一个线程锁定的资源。它们将永远彼此等待。这被称为死锁( deadlock),并且很难调试。

* 可重入锁(Reentrantlocks)

它通过确保线程在尝试两次锁定资源时不会被锁定。

* 时间分片机制

时间分片(timeslicing) 机制。这里，CPU可以很快地从一- 个线程切换到另一个线程， 造成了线程同时运行的错觉。这也是在处理级别完成的。没有多个处理单元的并行显然是虚拟的，并且在这样的硬件上运行多个线程不会改善性能

### 7.3python如何处理多线程

* 全局锁串行化

所有访问Python对象的线程都会被--个全局锁串行化。这是由许多解释器的内部结构完成的，和第三方C代码- -样，它们不是线程安全的，需要进行保护。

> 全局解释器锁机制(GIL)

* python多线程的意义

当线程仅包含纯Python代码时，使用线程来加速程序没有什么意义，因为GIL会将其串行化。但请记住，GIL只是强制在任何时候只有一一个线程可以执行Python代码。实际上，全局解释器锁在许多阻塞系统调用上被释放，并且可以在不使用任何Python/C API 函数的C扩展的部分中被释放。这意味着，多个线程可以执行IO操作或在某些第三方扩展中并行执行C代码。对于使用外部资源或涉及C代码的非纯粹的代码块，多线程对于等待第三方资源返回对于使用外部资源或涉及C代码的非纯粹的代码块，多线程对于等待第三方资源返回对于使用外部资源或涉及C代码的非纯粹的代码块，多线程对于等待第三方资源返回与用户交互，同时在所谓的后台中执行一些繁重的计算。

> 并不是Python语言的每个实现中都会有GIL。它是CPython, Stackless Python和PyPy的限制，但在Jython和IronPython中不存在

### 7.4何时使用python多线程

* 构建响应式界面
* 委派工作
* 构建多用户应用程序

### 7.5一个多线程使用的例子

#### 7.5.1使用threading模块创建线程

- **run():** 用以表示线程活动的方法。
- **start()**:启动线程活动。
- **join([time]):** 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- **isAlive():** 返回线程是否活动的。
- **getName():** 返回线程名。
- **setName():** 设置线程名。

```python
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
# 等待所有线程运行完毕
thread1.join()
thread2.join()
print ("退出主线程")
```

#### 7.5.2线程同步

如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间

```python
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```

#### 7.5.3线程优先级队列（ Queue）

Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:



- Queue.qsize() 返回队列的大小
- Queue.empty() 如果队列为空，返回True,反之False
- Queue.full() 如果队列满了，返回True,反之False
- Queue.full 与 maxsize 大小对应
- Queue.get([block[, timeout]])获取队列，timeout等待时间
- Queue.get_nowait() 相当Queue.get(False)
- Queue.put(item) 写入队列，timeout等待时间
- Queue.put_nowait(item) 相当Queue.put(item, False)
- Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
- Queue.join() 实际上意味着等到队列为空，再执行别的操作

```python
import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```

## 八、多线程 多进程 的另一个理解方向

### 8.1多线程实现多任务

```python
from threading import Thread
import time,threading
import os

def sing():
    for i in range(10):
        time.sleep(1)
        print("I'm singing and {} and {}".format(os.getpid(),threading.current_thread().name))

def dance():
    for i in range(10):
        time.sleep(1)
        print("I'm dancing and {} and {}".format(os.getpid(),threading.current_thread().name))

t1 = Thread(target=sing,name='t1')
t2 = Thread(target=dance,name='t2')

t1.start()
t2.start()
```

### 8.2多线程实现聊天室

```python
import socket
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.6.192', 9090))

def charge_from():
    while True:
        content,addr = s.recvfrom(1024)
        print("在IP:{}的端口:{},给我们发送了:{}".format(addr[0],addr[1],content.decode('utf8')))



def send_to(content=None):
    while True:
        content = input()
        s.sendto(content.encode('utf8'),('192.168.6.192',8080))

charge = Thread(target=charge_from)
send = Thread(target=send_to)

charge.start()
send.start()

charge.join()
send.join()
s.close()
print("聊天结束")
```

> 与网络调试助手实现聊天   当两个py端进行聊天时总是报错

### 8.3多线程共享全局变量

```python
from threading import Thread
import time
import threading
import os

TICKET =10


def sell_1():
    global TICKET
    while True:
        if TICKET>0:
            time.sleep(0.3)
            TICKET-=1
            print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
        else:
            print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET, os.getpid(), threading.current_thread().name))
            break


def sell_2():
    global TICKET
    while True:
        if TICKET>0:
            time.sleep(0.3)
            TICKET-=1
            print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
        else:
            print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET,os.getpid(),threading.current_thread().name))
            break

t1 = Thread(target=sell_1,name='t1')
t2 = Thread(target=sell_2,name='t2')

t1.start()
t2.start()
```

* 在实现多线程全局变量共享时也容易造成数据安全问题

```sh
购票成功 PID为14836 当前线程是t1
购票成功 PID为14836 当前线程是t2
购票成功 PID为14836 当前线程是t1
购票成功 PID为14836 当前线程是t2
购票成功 PID为14836 当前线程是t1
购票成功 PID为14836 当前线程是t2
购票成功 PID为14836 当前线程是t1
购票成功 PID为14836 当前线程是t2
购票成功 PID为14836 当前线程是t1
购票成功 PID为14836 当前线程是t2
票卖完了 剩余0 PID为14836 当前线程是t2
购票成功 PID为14836 当前线程是t1
票卖完了 剩余-1 PID为14836 当前线程是t1

Process finished with exit code 0
```

8.4多线程的数据安全为题解决--threading.Lock()

```python
from threading import Thread
import time
import threading
import os

TICKET =10
threading_lock = threading.Lock()

def sell_1():
    global TICKET
    while True:
        threading_lock.acquire()
        if TICKET>0:
            time.sleep(0.3)
            TICKET-=1
            threading_lock.release()
            print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
        else:
            print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET, os.getpid(), threading.current_thread().name))
            threading_lock.release()
            break


def sell_2():
    global TICKET
    while True:
        threading_lock.acquire()
        if TICKET>0:
            time.sleep(0.3)
            TICKET-=1
            threading_lock.release()
            print('购票成功 PID为{} 当前线程是{}'.format(os.getpid(),threading.current_thread().name))
        else:
            print('票卖完了 剩余{} PID为{} 当前线程是{}'.format(TICKET, os.getpid(), threading.current_thread().name))
            threading_lock.release()
            break
            
t1 = Thread(target=sell_1,name='t1')
t2 = Thread(target=sell_2,name='t2')

t1.start()
t2.start()
```

> 在敏感数据被调用之前上锁

### 8.4多线程之间的通信

```python
import time
import threading
import queue

q = queue.Queue()

def produce():
    for i in range(10):
        time.sleep(2)
        q.put('b{}'.format(i))
        print('+++生产面包b{}'.format(i))

def consumer():
    while True:
        time.sleep(0.6)
        print("---购买面包 {}".format(q.get()))

produce_t = threading.Thread(target=produce,name='produce_t')
consumer_t = threading.Thread(target=consumer,name='consumer')

produce_t.start()
consumer_t.start()
```

> queue.Queue() 是属于FIFO先进先出的队列

### 8.5多进程实现

```python
import multiprocessing
import os
import time

def sing():
    for i in range(10):
        time.sleep(1)
        print("I'm singing and {}".format(os.getpid()))

def dance():
    for i in range(10):
        time.sleep(1)
        print("I'm dancing and {}".format(os.getpid()))

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sing,name='t1')
    p2 = multiprocessing.Process(target=dance,name='t2')

    p1.start()
    p2.start()
```

> 在windows环境里多进程实现要在当先py文件 所以加 `if __name__ == '__main__':` mac系统不用

> 多进程之间无法共享全局变量

### 8.6多进程之间的通信

```python
import multiprocessing
import os
import time

q = multiprocessing.Queue(2)

def produce(q):
    for i in range(10):
        time.sleep(0.3)
        q.put('b{}'.format(i))
        print('生产++++++b{} and {}'.format(i,os.getpid()))

def consumer(q):
    for i in range(10):
        time.sleep(0.6)
        print('买面包---------{} and {}'.format(q.get(),os.getpid()))

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=produce,args=(q,))
    p2 = multiprocessing.Process(target=consumer,args=(q,))

    p1.start()
    p2.start()
```

> `put(self, obj, block=True, timeout=None):` block:是否使用阻塞  Ture 当队列满可以等待 False 队列满时加入报错  timeout ：当队列满时等待多久报错  单位秒

### 8.7join()方法

等待线程或进程结束再继续运行

```python
import threading
x = 10

def he(a,b):
    time.sleep(1)
    global x
    x = a+b

t1 = threading.Thread(target=he,args=(1,1))
t1.start()
print(x)

t1.join()

print(x)
```

```sh
10
2
```































































