#coding:utf-8

from selenium import webdriver
from ddt import ddt,data,unpack
from test_case.csv import Csv
from test_case.csv import csv_xlrd
import unittest
import time as t

time.sleep(5)

@ddt
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.baidu.com")

    def testCase_01(self):
        driver = self.driver
        csv_xlrd.clickButton(driver)
        csv_xlrd.clickLogin(driver,csv_xlrd.getExcel(0,0),csv_xlrd.getExcel(1.0))
        self.assertEqual(csv_xlrd.getText(csv_xlrd.getExcel(1,1)))




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run(suite)