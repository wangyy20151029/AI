#coding:utf-8\
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = "smtp.qq.com"
port = 465
sender = "329231117@qq.com"
psw = "wyy2019"
receiver = ["wangyinyin@kunteng.org.cn","wangyinyin@kunteng.org"]

file_path = "result.html"
with open(file_path,"rb") as fp:
    mail_body=fp.read()
msg=MIMEMultipart()
subject="这个是我的主题"
msg['from'] = sender
msg['to'] = ";".join(receiver)
msg['subject'] = subject

body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment;filename="test_report.html"'
msg.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()