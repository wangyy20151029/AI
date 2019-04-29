#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketeng")

title = EC.title_is(u"上海-悠悠-博客园")
title1 = EC.title_contains(u'上海-悠悠')
print(title(driver))

locator = ("name","tj_trnuomi")
text = u"糯米"
result = EC.text_to_be_present_in_element(locator,text)(driver)
print(result)

locator2 = ("id","su")
text2 = u"百度一下"
result2 = EC.text_to_be_present_in_element_value(locator2,text2)(driver)
print(result2)