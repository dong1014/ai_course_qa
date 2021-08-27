import requests
from common.login_test import login
import unittest

class user_info():

    @classmethod
    def userinfo(cls):
        url = 'https://aries.yuanfudao.biz/aries-server/android'
        header = login.headers
        cookies = login().get_cookies()
        params = "_productId=1911&_hostProductId=1911&platform=android29&version=1.6.0&av=5"
        s = login.s
        res = s.request('get', url+'/userinfo', cookies=cookies, headers=header,params=params).json()
        return res

class test_user_info(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('case 开始执行')

    @classmethod
    def tearDownClass(cls) -> None:
        print('case 执行完毕')

    def test_success(self):
        data = user_info.userinfo()
        code = data['code']
        self.assertEqual(code,200,msg="接口返回状态码：200")

    def test_phone(self):
        data = user_info.userinfo()
        phone = data['data']['phone']
        test_phone = '133****9095'
        self.assertEqual(test_phone,phone,msg="返回的手机号是加密的")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_user_info('test_phone'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

