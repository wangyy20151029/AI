#coding:utf-8
import xlrd
import time
import ddt
import unittest
from selenium import webdriver

class ExcelUtil():

    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j += 1
            return r

filePath = "test.xlsx"
sheetName = "Sheet1"
data = ExcelUtil(filePath,sheetName)
testData = data.dict_data()
print(testData)

@ddt.ddt
class Bolg(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passort.cnblogs.com/user/sigin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,username,psw):
        u'''这里写了了一个登录方法，账号和密码参数化'''
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("sigin").click()
        time.sleep(3)

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    @ddt.data(*testData)
    def test_login(self,data):
        u'''登录案例参考'''
        print("当前测试数据%s" %data)
        #调用登录方法
        self.login(data["username"],data["password"])
        #判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
