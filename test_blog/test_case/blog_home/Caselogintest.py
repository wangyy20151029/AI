#coding:utf-8
import sys
import unittest
from test_case.blog_home import LoginPage
from selenium import webdriver

class Caselogin124mail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.url="https:www.baidu.com"
        cls.username="wyy"
        cls.password="123"

    def test_login_mail(self):
        login_page=LoginPage.LoginBase(self.driver,self.url,u"baidu")
        login_page.open()
        login_page.input_usename(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()