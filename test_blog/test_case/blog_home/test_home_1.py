#coding:utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    def setUp(self):
        url_login = "https://passport.cnblogs.com/user/signin"
        self.driver = webdriver.Chrome()
        self.driver.get(url_login)
    def test_01(self):
        try:
            self.driver.find_element_by_id("input1").send_keys(u"上海-悠悠")
            self.driver.find_element_by_id("input2").send_keys("xxx")
            self.driver.find_element_by_id("sigin").click()
            time.sleep(3)
            locator = ("id","lnk_current_user")
            result = EC.text_to_be_present_in_element(locator,u"上海-悠悠")(self.driver)
            self.assertFalse(result)
        except Exception as msg:
            print(u"异常原因%s" %msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' %nowTime)
            raise
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
