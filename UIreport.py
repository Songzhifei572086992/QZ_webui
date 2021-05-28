from HTMLTestReportCN import HTMLTestRunner
import unittest
from s_email import send_email

def reportHTML(regular):
    discover=unittest.defaultTestLoader.discover(start_dir=r'C:\Users\全诊医学\PycharmProjects\QZ_webui',pattern=regular)
    f=open('c.html','wb')
    runner = HTMLTestRunner(stream=f,tester='小宋同志',title='全诊通UI自动化测试报告',description='报告描述',verbosity=2)
    runner.run(discover)
    f.close()
reportHTML('case*.py')
send_email()

