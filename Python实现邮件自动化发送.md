# Python实现邮件自动化发送

## 一、要求：

写个邮件发送模块和邮件发送机制，邮件发送模块需要可以发送多人需要有抄送功能，有附件功能，邮件正文需要支持HTML。邮件发送机制呢是一个应用场景，我当前有多个收件人，要给他们每个人都发送邮件，但是必须是每个人都要送单独邮件，所以要求引入多进程或者多线程或者协程。

## 二、实现过程

- python实现简单的邮件发送

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2497075649@qq.com"  # 用户名
mail_pass = "hliteqpyaaludjha"  # 口令


sender = '2497075649@qq.com'
receivers = ['2497075649@qq.com','zongxiang.yu@xquant.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8') # 主题内容
message['From'] = Header("2497075649@qq.com", 'utf-8')   # 邮件显示发件人
message['To'] = Header("2497075649@qq.com", 'utf-8')    # 邮件显示收件人

subject = 'Python SMTP 邮件测试'# 主题
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件",e)
```

* 实现抄送功能

```python
# 字段Cc中加入抄送人
message['Cc'] = ';'.join(self.receivers_cc) 
.....
# 将邮件发给抄送人
smtpObj.sendmail(self.mail_user,send_to_user.split(','), message.as_string())
```

* 实现附件功能

```python
        for att in self.attachment:
            att1 = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="'+att+'"'
            message.attach(att1)
```

* 实现正文html

```python
        if self.mail_msg and self.mail_msg_html is None:
            message.attach(MIMEText(self.mail_msg, 'plain', 'utf-8'))
        elif self.mail_msg is None and self.mail_msg_html:
            message.attach(MIMEText(self.mail_msg, 'html', 'utf-8'))
        elif self.mail_msg  and self.mail_msg_html:
            info = "<p>{}</p>"+self.mail_msg_html
            message.attach(MIMEText(info.format(self.mail_msg), 'html', 'utf-8'))
```

> 当正文有普通文本和html超文本时，会覆盖普通文本 这里做一个判断

将这几个功能插进前面的 python实现简单的邮件发送 中

## 三、问题

* 当使用公司的授权码时无法登陆  报`Connection unexpectedly closed`  个人认为是没有开启smtp服务 但是公司邮件没有开启这个服务的设置 所以用的是qq邮箱进行的实验

* 当前用的是多线程，只实现了并行。