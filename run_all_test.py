#!/usr/bin/python3
# -*- coding:utf-8 -*-
import unittest,time
from driver.HTMLTestRunner import HTMLTestRunner
from driver import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

#发送测试报告，需要配置邮箱账号
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    msg['From'] = 'zb194236@163.com'
    msg['To'] = 'zhangbin@veryci.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("zb194236@163.com","zhb194236")
    smtp.sendmail("zb194236@163.com","zhangbin@veryci.com",msg.as_string())
    smtp.quit()
    print('email has send out!')

#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

#指定测试用例为当前文件夹下的test_case目录
test_dir = './mail/test_case'
test_report = './mail/report/'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'login_case.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 10，Chrome")
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)