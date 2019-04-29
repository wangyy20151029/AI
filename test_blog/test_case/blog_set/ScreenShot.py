#coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
def get_screen():
    import time
    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
    driver.get_screenshot_as_file('%s.jpg' % nowTime)

def screen(func):
    def inner(*args,**kwargs)
        try:
            f=func(*args,**kwargs)
            return f
        except:
            get_screen()
            raise
    return inner
@screen
def search(driver):
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw11").send_keys("python")
    driver.find_element_by_id("su").click()
    search(driver)