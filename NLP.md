# 中文分词

## 一、用命令创建虚拟环境

#### 1. 安装虚拟环境的第三方包 virtualenv

```
pip install virtualenv
```

使用清华源安装：`pip install virtualenv -i https://pypi.python.org/simple/`

#### 2. 创建虚拟环境

cd 到存放虚拟环境光的地址

`virtualenv ENV` 在当前目录下创建名为ENV的虚拟环境（如果第三方包virtualenv安装在python3下面，此时创建的虚拟环境就是基于python3的）

`virtualenv -p /usr/local/bin/python2.7 ENV2` 参数 -p 指定python版本创建虚拟环境

`virtualenv --system-site-packages ENV` 参数 --system-site-packages 指定创建虚拟环境时继承系统三方库

#### 4. 激活/退出虚拟环境

`cd ~/ENV` 跳转到虚拟环境的文件夹

`source bin/activate` 激活虚拟环境

`pip list` 查看当前虚拟环境下所安装的第三方库

`deactivate` 退出虚拟环境

#### 5. 删除虚拟环境

直接删除虚拟环境所在目录即可

## 二、选择wheels安装pyltp方法

1）下载wheels

下面两个文件针对不同的python版本下载一个即可，电脑（win10），64bit的windows应该都可以。

[pyltp-0.2.1-cp35-cp35m-win_amd64.whl](http://mlln.cn/2018/01/31/pyltp在windows下的编译安装/pyltp-0.2.1-cp35-cp35m-win_amd64.whl)

[pyltp-0.2.1-cp36-cp36m-win_amd64.whl](http://mlln.cn/2018/01/31/pyltp在windows下的编译安装/pyltp-0.2.1-cp36-cp36m-win_amd64.whl)

2）安装文件

下载好了以后, 在命令行下, cd到wheel文件所在的目录, 然后使用命令pip install wheel文件名安装.

![img](https:////upload-images.jianshu.io/upload_images/6102062-c80bdbed62968d34.png?imageMogr2/auto-orient/strip|imageView2/2/w/906/format/webp)

3）测试

可以直接在命令窗口中测试，代码如下：

<img src="https:////upload-images.jianshu.io/upload_images/6102062-e5019b6045e70c3c.png?imageMogr2/auto-orient/strip|imageView2/2/w/754/format/webp" alt="img"  />

## 三、部署语言模型库

[语言模型库下载](https://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569#list/path=%2Fltp-models)

将文件解压在项目内

## 四、基本组件使用

### 4.1 分句



```python
from pyltp import SentenceSplitter
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print('\n'.join(sents))
```

输出：



```undefined
元芳你怎么看？
我就趴窗口上看呗！
```

### 4.2 分词



```go
import os
from pyltp import Segmentor
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'
cws_model_path=os.path.join(LTP_DATA_DIR,'cws.model')
segmentor=Segmentor()
segmentor.load(cws_model_path)
words=segmentor.segment('熊高雄你吃饭了吗')
print(type(words))
print('\t'.join(words))
segmentor.release()
```

输出



```undefined
熊高雄 你   吃饭  了   吗
```

### 4.3 使用自定义词典

lexicon文件如下：



![img](https:////upload-images.jianshu.io/upload_images/1531909-9c98472755065972.png?imageMogr2/auto-orient/strip|imageView2/2/w/208/format/webp)



```python
import os
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path, 'lexicon') # 加载模型，第二个参数是您的外部词典文件绝对路径
words = segmentor.segment('亚硝酸盐是一种化学物质')
print('\t'.join(words))
segmentor.release()
```

输出



```css
[INFO] 2018-08-16 19:18:03 loaded 2 lexicon entries
亚硝酸盐        是      一      种      化学    物质
```

### 4.4 词性标注



```python
import os
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'
# ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']  # 分词结果
postags = postagger.postag(words)  # 词性标注

print('\t'.join(postags))
postagger.release()  # 释放模型
```

输出如下



```undefined
nh      r       r       v
```

### 4.5 命名实体识别



```python
import os
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'  # ltp模型目录的路径
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

from pyltp import NamedEntityRecognizer
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
netags = recognizer.recognize(words, postags)  # 命名实体识别

print('\t'.join(netags))
recognizer.release()  # 释放模型
```

输出



```undefined
S-Nh    O   O   O
```

### 4.6 依存句法分析



```python
import os
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'  # ltp模型目录的路径
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
arcs = parser.parse(words, postags)  # 句法分析

print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
parser.release()  # 释放模型
```

输出为:



```css
4:SBV   4:SBV   4:ADV   0:HED
```

标注集请参考 [依存句法关系](https://links.jianshu.com/go?to=http%3A%2F%2Fltp.readthedocs.org%2Fzh_CN%2Flatest%2Fappendix.html%23id5) 。

### 4.7 语义角色标注



```csharp
import os
LTP_DATA_DIR='D:\Data\ltp_data_v3.4.0'  # ltp模型目录的路径
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl_win.model')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。

from pyltp import SementicRoleLabeller
labeller = SementicRoleLabeller() # 初始化实例
labeller.load(srl_model_path)  # 加载模型

words = ['元芳', '你', '怎么', '看']
postags = ['nh', 'r', 'r', 'v']
# arcs 使用依存句法分析的结果
roles = labeller.label(words, postags, arcs)  # 语义角色标注

# 打印结果
for role in roles:
    print(role.index, "".join(
        ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
labeller.release()  # 释放模
```

输出为：



```css
[dynet] random seed: 1676210130
[dynet] allocating memory: 2000MB
[dynet] memory allocation done.
3 A0:(1,1)ADV:(2,2)
```

例如上面的例子，由于结果输出一行，所以“元芳你怎么看”有一组语义角色。 其谓词索引为3，即“看”。这个谓词有三个语义角色，范围分别是(0,0)即“元芳”，(1,1)即“你”，(2,2)即“怎么”，类型分别是A0、A0、ADV。
 标注集请参考 [语义角色关系](https://links.jianshu.com/go?to=http%3A%2F%2Fltp.readthedocs.org%2Fzh_CN%2Flatest%2Fappendix.html%23id6) 。

### 4.8词性表

![](D:\Desktop\python学习\词性表1.jpg)

![](D:\Desktop\python学习\词性表2.jpg)

