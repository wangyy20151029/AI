#coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

try:
    element = driver.find_element_by_id("blog_nav_newpostxx")
except NoSuchElementException as msg:
    print(u"查找元素异常 %s" %msg)
    nowtime = time.strftime("%Y%m%d.%H.%M.%S")
    t = driver.get_screenshot_as_file('%s.jpg' % nowtime)
else:
    element.click()