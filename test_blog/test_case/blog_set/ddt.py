#coding:utf-8
import ddt
import unittest

testData = [{"username":"发票代码","psw":"1234567890"},
            {"username":"开票日期","psw":"0987654321"},
            {"username":"购货方名称","psw":"999888777"}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start！")

    def tearDown(self):
        print("end!")

    @ddt.data(*testData)
    def test_ddt(self,data):
        print(data)

if __name__ == '__main__':
    unittest.main()