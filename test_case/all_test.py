#coding=utf-8
import unittest
import HTMLTestRunner
import os ,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

listaa='E:\\webTest\\Test-case'


def creatsuitel():
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa, pattern='start_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit

alltestnames = creatsuitel()


#定义发送邮件
def sentmail(file_new):
    # 发送邮箱
    sender = 'yangwl@jiaxun.com'
    # 接收邮箱
    receiver = 'dargons0207@163.com'
    # 发送邮件主题
    subject = 'python email test'
    # 发送邮箱服务器
    smtpserver = 'smtp.jiaxun.com'
    # 发送邮箱用户/密码
    username = 'yangwl@jiaxun.com'
    password = 'qwer.123'
    # HTML 形式的文件内容
    msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    msg['Subject'] = subject
    smtp = smtplib.SMTP()
    smtp.connect('smtp.jiaxun.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print 'email has send out !'


def sendreport():
    result_dir = 'E:\\webTest\\report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'上一次测试生成的报告： '+lists[-2])
    #找到上一次测试生成的文件
    file_new = os.path.join(result_dir,lists[-2])
    print file_new
    #调用发邮件模块
    sentmail(file_new)

if __name__ == "__main__":

    now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
    filename = 'E:\\webTest\\report\\'+now+'result.html'
    fp = file(filename, 'wb')

    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：')

    runner.run(alltestnames)
    #执行发邮件
    sendreport()