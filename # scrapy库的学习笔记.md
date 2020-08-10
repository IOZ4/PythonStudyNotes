# scrapy库的学习笔记

## 一、scrapy框架组成

### 1.1五个核心

* **engine引擎**，协调其它四个组件 之间的联系，即与其它四个组件进行通信，也是scrapy框架的核心。
* **siders 爬虫类**，爬虫程序的编写代码所在，也是发起请求的起始位置。spider发起的请求经过engine转入到scheduler中。
* **scheduler 调度器**，调度所有的请求（优先级高的则会先执行）。当执行某一个请求时，由engine转入downloader中。
* **donwloader下载器**，实现请求任务的执行，从网络上请求数据,将请求到的数据封装成响应对象，并将响应的对象返回给engine。engine将响应的数据对象（以回调接口的方式）回传给它的爬虫类对象进行解析。
* **itemoioeline 数据管道**。当spider解析完以后，将数据经过engine转入到此（数据管道）再根据数据类型进行处理（图片、文本）

### 1.2两个中间件

* **爬虫中间件**，介于Spider和Engine之间的， 可以拦截Spider的发起的请求及数据。
* **下载中间件**，介于Engine和Downloader之间的， 可以拦截下载和响应。当然在下载处理之前，可以设置代理、请求头、Cookie等操作(反反爬设置)，还可以基于Splash和Selenium执行特定的操作。

## 二、scrapy数据管道

### 2.1指令方式存储

```sh
scrapy crawl 爬虫名 -o xxx.json|csv
```

> 只是适合单页数据的爬取，如何多页多层次数据爬取时，不适合此方式

### 2.2Item类

作用：用于区别中哪一页（类型）的数据

用法:类似于dict用法， 在数据管道类的process_ item()方法中，通过isinstance()方法来判断item是哪一类型的。

### 2.3Pipeline

* 处理数据的方法

  ```python
  def process_item(self, item, spider):
  	return item
  ```

  * item参数表示爬虫类中解释到的数据(yield item)
  * spider参数表示爬虫类对象
  * 如果item被返回，则表示可以被优先级低的pipeline处理

* 初始化方法
  
  * 属于定制方法，可以初始化一些参数或对象， 如文件名，数据库的连接等。
* process item和init的调用次数说明
  * process_ item方法会被(engine) 多次调用
  * init 随着爬虫程序的启动时创建pipeline类时调用，只会被调用一次

## 三、定量爬虫

```sh
scrapy crawl -s 信号
```

常用的scrapy信号

* **CLOSESPIDER_ ITEMCOUNT**=条目的数量
* CLOSESPIDER_ PAGECOUNT=请求页的数量
* CLOSESPIDER_ ERRORCOUNT=请求错误的数量
* CLOSESPIDER_ _TIMEOUT=超时的时长

## 四、两个中间件

### 4.1爬虫中间件

```tex
监测爬虫类与引擎之间的交互数据(请求request、 响应response、 数据item)及异常情况
```

```python
@classmethod
def from_crawler(cls，crawler): pass #启动爬虫时用于创建爬虫中间件类的实例对象

def process_spider_input(self, response, spider) #流程中第6步，engi ne将请求响应的数据输入给spider时，调用此方法。

def process_spider_output(se1f, response, result, spider) #流程中第7步，由spider类解析response数据之后产生结果输出给engine时，调用此方法

def process_spider.exception(self, response, exception, spider): #解析数据时发异常时

def process_start_requests(self, start_requests, spider): #第一次爬虫发起请求时，调用此方法，即流程中第1步，从Spider->Engine时。
```

### 4.2下载中间件

```tex
下载中间件是引擎engi ne和下载器downloader之间的中间件，可以拦截请求和响应以及请求异常的处理。
```

````python
@classmethod
def from_ crawler(cls，crawler)

def process_ request(self, request, spider)

def process_ request(self, request, spider)

def process_ exception(self, request, exception, spider)
````

* process_ request()方法可返回的对象(四种可能)
  * scrapy.http.Request
  * scrapy.http.HtmlResponse/Response
  * None 表示不拦截
  * raise lgnoreRequest不下载这个请求

* process. response(方法可以返回的对象
  * scrapy.http.Request 未下载成功请求
  * scrapy.http.Response 进-步封装 之后的response

**下载中间件的作用** 

在下载中间件中，可以设置代理、设置cookie、 设置请求头以及基于Selenium实现动态js渲染和用户登录

## 五、常见反爬虫问题解决

### 5.1解决cookie登录

在项目内新建cookie_文件

```python
import random

cookie_texts = ['login=flase; ASP.NET_SessionId=hadxyn4hpv2bao301kq3dxqf; Hm_lvt_9007fab6814e892d3020a64454da5a55=1595833584; codeyzgswso=5bedff597f96ccb6; gsw2017user=1142751%7cF5071CD9CE978E5BE8728C772E7F76DF; login=flase; gswZhanghao=13359702032; gswPhone=13359702032; wxopenid=defoaltid; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1595833670',]

def get_cookie():
    cookie = random.choice(cookie_texts)
    return {
        content.split('=')[0].strip():content.split('=')[1].strip() for content in cookie.split(';')
    }

if __name__ == '__main__':
    print(get_cookie())
```

在调试环境中测试

```shell
>>>scrapy shell 目标网址
>>>requests.cookies
{}
>>>from gushiwen import cookies_
>>>cookies_.get_cookie()
{'login': 'flase', 'ASP.NET_SessionId': 'hadxyn4hpv2bao301kq3dxqf', 'Hm_lvt_9007fab6814e892d3020a64454da5a55': '1595833584', 'codeyzgswso': '5bedff597f96ccb6', 'gs
w2017user': '1142751%7cF5071CD9CE978E5BE8728C772E7F76DF', 'gswZhanghao': '13359702032', 'gswPhone': '13359702032', 'wxopenid': 'defoaltid', 'Hm_lpvt_9007fab6814e89
2d3020a64454da5a55': '1595833670'}
>>>request.cookies = cookies_.get_cookie()
>>>fetch(request)
>>>view(response)
True
```

在下载中间件内

```python
def process_request(self, request:Request, spider):
    request.cookies = cookies_.get_cookie()
```

### 5.2解决代理问题

```python
def process_request(self, request:Request, spider):
	request.meta['proxy'] = 'https://127.168.6.192:9999'
```

## 六、规则爬虫

* 创建规则爬虫的指令

```sh
scrapy genspider -t crawl 爬虫名 域名
```

* 链接提取器
  * 正则方式(allow | deny)
  * restrict xpaths() xpath方式指定`a`标签所在的(间接)父级标签
  * restrict css()样式方式指定``a`标签所在的(间接) 父级标签

* Rule() 规则
  * extractor
  * callback
  * follow=True 表示提取的连接在请求成功后，解析时是否继续按此规则提取连接