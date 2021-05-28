#SMTP邮件传输协议
import smtplib
from email.mime.text import MIMEText
from email.header import  Header
from email.mime.multipart import MIMEMultipart
def send_email():
    #创建服务器链接
    con=smtplib.SMTP('smtp.163.com','25')
    #连接服务器
    con.login(user='songzf_1996@163.com',password='FNBSIFJRVIISDBQB')
    #发送者账号
    sender='songzf_1996@163.com'
    #接收者账号
    rece=['songzf_1996@163.com']
    #发送附件
    message=MIMEMultipart()
    content=open(r'C:\Users\全诊医学\PycharmProjects\QZ_webui\c.html',encoding='utf-8').read()
    #把读取出来的内容放在文本中
    filel=MIMEText(content,'base64','utf-8')
    filel['Content-Disposition']='attachment;filename="testing report.html"'
    message.attach(filel)
    # 发送正文 _text 邮件正文 _subtype 文件类型      html文本   base64（二进制类型）  plain默认就是纯文本   _charset 编码格式
    msg=MIMEText(_text='全诊通项目自动化测试报告',_subtype='plain',_charset='utf-8')
    #设置头部标题
    message['Subject']=Header('测试报告','utf-8')
    #发件人
    message['From']=Header('<songzf_1996@163.com>','utf-8')
    #收件人
    message['To']=Header('<songzf_1996@163.com>','utf-8')
    message.attach(msg)
    #发送邮件
    con.sendmail(sender,rece,message.as_string())


