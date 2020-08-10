# socket 实现通讯

## 实现通讯

### upd发送数据

```python
import socket
# udp只管发送数据不管对方是否能够接收到

# 创建socket 并连接
# AF_INET 表示是网络连接
# SOCK_DGRAM 表示是 udp协议的连接
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 发送数据
# data: 需要发送的二进制数据 IP地址和端口号组成的元组
s.sendto('你好'.encode('utf8'),('192.168.6.193',9090))

# 关闭socket
s.close()
```

### udp接收数据

```python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定自己的IP  表明自己用哪一个端口进行接收数据
s.bind(('192.168.6.193',9090))

# recvfrom 等待接收数据  一次拿1024字节数据  会有队列阻塞问题
content,addr = s.recvfrom(1024)
print("在IP:{}的端口:{},给我们发送了:{}".format(addr[0],addr[1],content.decode('utf8')))

s.close()
```

### TCP/IP 协议的服务端

```python
import socket

# TCP/IP 是先建立连接然后进行通信  知识点: 三次握手和四次挥手
# SOCK_STREAM:表示使用的是TCP/IP协议进行的通信
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.6.193',9090))
# 当超过服务器负载时的可排队数量128
s.listen(128)

client_socket,client_addr = s.accept()
# recv 表示每次取1024字节的数据
data = client_socket.recv(1024)
print('IP:{}的端口:{}给我们发送了{}'.format(client_addr[0],client_addr[1],data.decode('utf8')))
```

### TCP/IP 协议的客户端

```python
import socket

# SOCK_STREAM 表示用TCP/IP协议进行通信
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 在数据发送之前必须要和服务器建立连接
s.connect(('192.168.6.193',9090))

# 发送数据
s.send('hello'.encode('utf-8'))

s.close()
```

> 实现文件下载案例   思路：首先在客户端输入要下载的文件名，服务器收到然后找到文件，打开文件并发送给客户端，客户端再写入文件 
>
> ps:在进行照片的传输的时候 rb wb whil True 循环 content = client_socket.recv(1024) if content: break

### TCP/IP协议的三次握手、四次挥手

#### 三次握手过程

第一次握手：客户端给服务端发一个 SYN 报文，并指明客户端的初始化序列号 ISN©。此时客户端处于 SYN_SEND 状态。

首部的同步位SYN=1，初始序号seq=x，SYN=1的报文段不能携带数据，但要消耗掉一个序号。

第二次握手：服务器收到客户端的 SYN 报文之后，会以自己的 SYN 报文作为应答，并且也是指定了自己的初始化序列号 ISN(s)。同时会把客户端的 ISN + 1 作为ACK 的值，表示自己已经收到了客户端的 SYN，此时服务器处于 SYN_REVD 的状态。

在确认报文段中SYN=1，ACK=1，确认号ack=x+1，初始序号seq=y。

第三次握手：客户端收到 SYN 报文之后，会发送一个 ACK 报文，当然，也是一样把服务器的 ISN + 1 作为 ACK 的值，表示已经收到了服务端的 SYN 报文，此时客户端处于 ESTABLISHED 状态。服务器收到 ACK 报文之后，也处于 ESTABLISHED 状态，此时，双方已建立起了连接。

#### 握手的意义

第一次握手：客户端发送网络包，服务端收到了。

这样服务端就能得出结论：客户端的发送能力、服务端的接收能力是正常的。

第二次握手：服务端发包，客户端收到了。

这样客户端就能得出结论：服务端的接收、发送能力，客户端的接收、发送能力是正常的。不过此时服务器并不能确认客户端的接收能力是否正常。

第三次握手：客户端发包，服务端收到了。

这样服务端就能得出结论：客户端的接收、发送能力正常，服务器自己的发送、接收能力也正常。

#### 三次握手图解

![](D:\Desktop\python学习\三次握手.jpg)

#### 四次挥手过程

刚开始双方都处于 ESTABLISHED 状态，假如是客户端先发起关闭请求。四次挥手的过程如下：

第一次挥手：客户端发送一个 FIN 报文，报文中会指定一个序列号。此时客户端处于 FIN_WAIT1 状态。

即发出连接释放报文段（FIN=1，序号seq=u），并停止再发送数据，主动关闭TCP连接，进入FIN_WAIT1（终止等待1）状态，等待服务端的确认。

第二次挥手：服务端收到 FIN 之后，会发送 ACK 报文，且把客户端的序列号值 +1 作为 ACK 报文的序列号值，表明已经收到客户端的报文了，此时服务端处于 CLOSE_WAIT 状态。

即服务端收到连接释放报文段后即发出确认报文段（ACK=1，确认号ack=u+1，序号seq=v），服务端进入CLOSE_WAIT（关闭等待）状态，此时的TCP处于半关闭状态，客户端到服务端的连接释放。客户端收到服务端的确认后，进入FIN_WAIT2（终止等待2）状态，等待服务端发出的连接释放报文段。

第三次挥手：如果服务端也想断开连接了，和客户端的第一次挥手一样，发给 FIN 报文，且指定一个序列号。此时服务端处于 LAST_ACK 的状态。

即服务端没有要向客户端发出的数据，服务端发出连接释放报文段（FIN=1，ACK=1，序号seq=w，确认号ack=u+1），服务端进入LAST_ACK（最后确认）状态，等待客户端的确认。

第四次挥手：客户端收到 FIN 之后，一样发送一个 ACK 报文作为应答，且把服务端的序列号值 +1 作为自己 ACK 报文的序列号值，此时客户端处于 TIME_WAIT 状态。需要过一阵子以确保服务端收到自己的 ACK 报文之后才会进入 CLOSED 状态，服务端收到 ACK 报文之后，就处于关闭连接了，处于 CLOSED 状态。

即客户端收到服务端的连接释放报文段后，对此发出确认报文段（ACK=1，seq=u+1，ack=w+1），客户端进入TIME_WAIT（时间等待）状态。此时TCP未释放掉，需要经过时间等待计时器设置的时间2MSL后，客户端才进入CLOSED状态。

收到一个FIN只意味着在这一方向上没有数据流动。客户端执行主动关闭并进入TIME_WAIT是正常的，服务端通常执行被动关闭，不会进入TIME_WAIT状态。

在socket编程中，任何一方执行close()操作即可产生挥手操作。

#### 四次挥手图解

![](D:\Desktop\python学习\四次挥手.jpg)

#### **挥手为什么需要四次？**

因为当服务端收到客户端的SYN连接请求报文后，可以直接发送SYN+ACK报文。其中ACK报文是用来应答的，SYN报文是用来同步的。但是关闭连接时，当服务端收到FIN报文时，很可能并不会立即关闭SOCKET，所以只能先回复一个ACK报文，告诉客户端，“你发的FIN报文我收到了”。只有等到我服务端所有的报文都发送完了，我才能发送FIN报文，因此不能一起发送。故需要四次挥手。

#### **为什么TIME_WAIT状态需要经过2MSL才能返回到CLOSE状态？**

理论上，四个报文都发送完毕，就可以直接进入CLOSE状态了，但是可能网络是不可靠的，有可能最后一个ACK丢失。所以TIME_WAIT状态就是用来重发可能丢失的ACK报文。

# pip指令

- pip install <package_ name>                  用来下载一个第 三方的模块

- pip uninstall <package_ name>              用来删除第三方模块

- pip list                                                         用来列出当前环境安装的模块名和版本号

- pip freeze                                                   用来 列出当前环境安装的模块名和版本号

- pip freeze > file_ name                             将安装的模块名和版本号重定向输出到指定的文件

- pip install -r file_ name                             读取文件 里模块名和版本号并安装

  ```sh
  pip freeze > requirement.txt
  ```

  ```sh
  pip install -r requirement.txt
  ```

## 从指定的网址下载包（临时修改）

```sh
pip install <package_ name> -i <url> 从指定的地址下载包
```

## 永久修改镜像源

**Windows**：

1. 在 windows 命令提示符（控制台）中，输入 **%APPDATA%**，进入此目录
2. 在该目录下新建名为 pip 的文件夹，然后在其中新建文件 pip.ini。（例如："C:\Users\Administrator\AppData\Roaming\pip\pip.ini"）
3. 在文件中填入一下内容并保存（可替换为上述不同的镜像地址）：

```text
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

**Linux / Mac**：

文件地址为 ~/.pip/pip.conf，其余相同。

## 镜像源

```txt
清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/
```

# 导入模块

import  <model_name|function_name>

from <model_name> import <function_name>

import <model_name> as <another_name>

from <model_name> import *   只能读取\_\_all\_\_里面的属性或者是函数

```python
__all__ = ['a','b']
```

# 自定义模块的使用

下划线开头的函数和方法不建议被调用，但是可以通过`import <model_name>`'`<model_name>.<function|attribute_name>`使用。

如果不想让调库的人使用私有方法和私有属性，使用`del (<function_name|attribute_name>)`在模块的最后做删除操作