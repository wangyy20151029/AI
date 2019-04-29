#coding:utf-8
from selenium import webdriver
import unittest
import time

class Bolg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,username,psw):
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    def test_01(self):
        self.login(u"上海-悠悠",u"xxx")
        result = self.is_login_success()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()