#coding = utf-8
import unittest
from case.test_userinfo import test_user_info
import os
from lib.HTMLTestRunner import HTMLTestRunner
base_path = os.getcwd()
print(base_path)


test_case01 = unittest.TestLoader().loadTestsFromTestCase(test_user_info)
suite = unittest.TestSuite(test_case01)
runner = unittest.TextTestRunner()
file_path = base_path+'/Report/Report.html'
with open(file_path,'wb') as f:
    runner = HTMLTestRunner(stream=f,title="这是张冬的测试报告",description="这是测试报告的描述")
    runner.run(suite)