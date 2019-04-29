#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
WebDriverWait(driver,10).until(lambda x: x.find_element_by_id("kw")).sendkeys("yoyo")
is_disappeared = WebDriverWait(driver,10,1).until_not(lambda x: x.find_element_by_id("kw").displayed())
print(is_disappeared)