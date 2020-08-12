import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import threading

class MailingAutomatic():
    def __init__(self,mail_host=None,mail_user=None,mail_pass=None,receivers:list=None,
                 receivers_cc:list=None,mail_msg:str=None,mail_msg_html:str=None,attachment:list=None,mail_subject=None):
        """
        完成邮件自动化发送：邮件发送模块和邮件发送机制，邮件发送模块需要可以发送多人需要有抄送功能，有附件功能，邮件正文需要支持HTML。
        邮件发送机制呢是一个应用场景，我当前有多个收件人，要给他们每个人都发送邮件，但是必须是每个人都要发送单独邮件，所以要求引入多
        进程或者多线程或者协程。
        :param mail_host: 设置服务器
        :param mail_user: 用户名
        :param mail_pass: 口令
        :param receivers: 接收人
        :param receivers_cc: 抄送人
        :param mail_msg: 正文
        :param attachment: 附件的绝对地址
        :param mail_msg_html: html内容
        :param mail_subject: 邮件主题
        """
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.receivers = receivers
        self.receivers_cc = receivers_cc
        self.mail_msg = mail_msg
        self.attachment = attachment
        self.mail_msg_html = mail_msg_html
        self.mail_subject = mail_subject

    def send(self,receiver:str):
        message = MIMEMultipart()
        # 主题内容
        if self.mail_msg and self.mail_msg_html is None:
            message.attach(MIMEText(self.mail_msg, 'plain', 'utf-8'))
        elif self.mail_msg is None and self.mail_msg_html:
            message.attach(MIMEText(self.mail_msg, 'html', 'utf-8'))
        elif self.mail_msg  and self.mail_msg_html:
            info = "<p>{}</p>"+self.mail_msg_html
            message.attach(MIMEText(info.format(self.mail_msg), 'html', 'utf-8'))

        # 构造附件
        for att in self.attachment:
            att1 = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="'+att+'"'
            message.attach(att1)

        message['From'] = Header(self.mail_user, 'utf-8')           # 邮件显示发件人
        message['To'] = Header(receiver, 'utf-8')                   # 邮件显示收件人
        message['Subject'] = Header(self.mail_subject, 'utf-8')     # 邮件主题
        message['Cc'] = ';'.join(self.receivers_cc)                 # 邮件抄送人
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.mail_user, self.mail_pass)
            send_to_user = ''.join(self.receivers_cc)+","+receiver
            smtpObj.sendmail(self.mail_user,send_to_user.split(','), message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件", e)

    def send_by_threading(self):
        t_list = [threading.Thread(target=self.send,args=(receiver,)) for receiver in self.receivers]
        [t.start() for t in t_list]

if __name__ == '__main__':
    m = MailingAutomatic(mail_host='smtp.qq.com',mail_user='2497075649@qq.com',mail_pass='hliteqpyaaludjha',
                         receivers=['guosong.lin@xquant.com','kesu.wang@xquant.com'],receivers_cc=['zongxiang.yu@xquant.com'],
                         mail_msg='python邮件自动化测试。。。',mail_subject='邮件测试',attachment=['test.txt','test2.txt'],mail_msg_html="""<p>Python 邮件发送测试...</p><p><a href="https://www.baidu.com">这是一个链接</a></p>""")
    m.send_by_threading()
