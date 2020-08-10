# git

## 一、git和tortoisegit下载

```txt
https://tortoisegit.org/download/
```

```sh
https://git-scm.com/download/win
```

## 二、基础命令

```sh
git --version
```

> 查看版本号

## 三、创建仓库

在目标文件夹下

鼠标右击 选择 Git Base Here 

初始化git

```sh
git init
```

>初始化后，.git文件是隐藏文件   点击 组织>文件夹和搜索选项>查看>隐藏文件和文件夹

## 四、文件各类下标的意义

- 对勾  ：  以提交给本地服务器
- 叹号  ：  文件以修改还未提交|文件已添加到暂存区
- 红叉  ：  删除文件
- 蓝加  ：  已添加

## 五、基本操作

- 显示日志
- 比较版本差异
- 版本库浏览器（查看版本库目录结构）
- 文件删除（再未提交之间可以还原）
- 删除并保留本地副本
- ctrl 可以选择多个文件

## 六、GitHub远程仓库（多人开发同一个项目）

- [码云](https://gitee.com/)国内的github

### 6.1使用ssh通信协议将本地仓库推送到远程(命令行)

1. 生成密钥对(在git Bash Here窗口下)

```sh
ssh-keygen -t rsa
```

>默认路径C:\Users\zongxiang.yu\.ssh 带后缀.pub的为公钥 反之为私钥

2. GitHub的setings>SSH and GPG keys 将公钥设置好
3. 推送(在仓库内打开git Bash Here)

```sh
git remote add origin git@github.com:IOZ4/repo2.git     #建立连接
git push -u origin master							 #推送	
```

### 6.2使用https通信协议将本地仓库推送到远程（命令行）

```sh
git remote add origin https://github.com/IOZ4/repo2.git
git push -u origin master
```

### 6.3使用tortoise进行推送

在仓库内鼠标右键 Git同步>管理>

ssh通信协议进行推送

```tex
远端选项中 远端 这个远端名（随意）
		 URL 仓库地址 
		 推送URL 不填
		 putty秘钥 ssh私钥
网络选项中 SSH 为ssh.exe
```

https通信协议进行推送

```tex
远端：远端名（随意）
URL： 仓库https地址
```

## 七、克隆远程仓库到本地

### 7.1命令行

ssh

```
git clone git@github.com:IOZ4/repo1.git
```

https

```tex
git clone https://github.com/IOZ4/repo1.git
```

### 7.2鼠标右键>Git克隆

## 八、推送冲突

产生的原因：推送的文件不是在最新的文件上修改的

解决办法：手动合并并添加到暂存区，然后鼠标右键解决冲突，最后提交、推送

## 九、分支

### 9.1创建分支

鼠标右键>创建分支|切换、检出>创建新分支

### 9.2合并

切换到想保留的分支上 鼠标右键>合并(选择想要合并的分支)

### 9.3删除分支

在  切换\检出 中的分支选项中鼠标右键 选择删除分支

## 十、在pycharm中设置Git

1. 设置路径（点击test 返回版本号，则设置成功）默认路径（`C:\Program Files\Git\cmd\git.exe`）

settings>Version Control>Git>Path to Git executable

2. vcs能完成各个功能

