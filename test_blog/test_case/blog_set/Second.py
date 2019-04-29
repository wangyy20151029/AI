#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def browser(browser='firefox'):
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser,You can enter 'firefox','chrome','ie'")
    except Exception as msg:
        print("%s" % msg)

class Yoyo(object):
    def __init__(self,driver):
        self.driver=driver
    def open(self,url,t='',timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver,timeout,1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" %url)
        except Exception as msg:
            print("Errot:%s" %msg)
    def find_element(self,locator,timeout=10):
        element=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
        return element
    def find_elements(self,locator,timeout=10):
        elements=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
        return elements
    def click(self,locator):
        element=self.find_element(locator)
        element.click()
    def send_keys(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)
    def is_text_in_element(self,locator,text,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            print("元素没定位到:" + str(locator))
            return False
        else:
            return result
    def is_text_in_value(self,locator,value,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result
    def is_title(self,title,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
        return result
    def is_title_contains(self,title,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_contains(title))
        return result
    def is_selected(self,locator,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))
    def is_selected_be(self,locator,selected=True,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
        return result
    def is_alert_present(self,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
        return result
    def is_visibility(self,locator,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
        return result
    def is_invisibility(self,locator,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locator))
        return result
    def is_clickable(self,locator,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))
        return result
    def is_locator(self,locator,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return result
    def move_to_element(self,locator):
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()
    def get_title(self):
        return self.driver.title()
    def get_text(self,locator):
        element=self.find_element(locator)
        return element.text
    def get_attribute(self,locator,name):
        element=self.find_element(locator)
        return element.get_attribute(name)
    def js_execute(self,js):
        return self.driver.execute_script(js)
    def js_focus_element(self,locator):
        target=self.find_element(locator)
        self.driver.execute_script("argument[0].scrollIntoView;",target)
    def js_scroll_top(self):
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)
    def js_scroll_end(self):
        js="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
    def select_by_index(self,locator,index):
        element=self.find_element(locator)
        Select(element).select_by_index(index)
    def select_by_value(self,locator,value):
        element=self.find_element(locator)
        Select(element).select_by_value(value)
    def select_by_text(self,locator,text):
        element=self.find_element(locator)
        Select(element).select_by_value(text)

if __name__ == '__main__':
    driver = browser()
    driver_n = Yoyo(driver)
    driver_n.open("http://www.cnblogs.com/yoyoketang/")
    input_loc = ("id","kw")
    print(driver_n.get_title())
    el=driver_n.find_element(input_loc)
    driver_n.send_keys(input_loc,"yoyo")
    button_loc = ("id","su")
    driver_n.click(button_loc)
    print(driver_n.is_text_in_element("name","tj_trmap"),"地图")
    set_loc=("link text","设置")
    driver_n.move_to_element(set_loc)


