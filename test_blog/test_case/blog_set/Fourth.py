#coding:utf-8
import unittest
from test_case.blog_set.Second import browser
from test_case.blog_set.Third import LoginPage,login_url

class Login_test(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver=browser()
        self.login=LoginPage(self.driver)
        self.login.open(login_url)
    def login_case(self,username,psw,expect=True):
        self.login.input_username(username)
        self.login.input_password(psw)
        self.login.click_submit()
        result=self.login.is_text_in_element(("id","lnk_current_user"),"上海-悠悠")
        expect_result=expect
        self.assertEqual(result,expect_result)
    def test_login01(self):
        self.login_case("xx","xx",True)
    def test_login02(self):
        self.login_case("xx","xx",False)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()