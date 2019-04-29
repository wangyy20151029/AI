#cdding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class Action(object):

    def __init__(self,selenium_driver,base_url,pagetitle):
        self.base_url=base_url
        self.pagetitle=pagetitle
        self.driver=selenium_driver

    def _open(self,url,pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        assertself.on_page(pagetitle).u"打开页面失败%s" %url

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed)
            return self.driver.find_element(*loc)
            except：
        print(u"%s页面中未能找到%s元素")%(self,loc)

    def swithc_frame(self,loc):
        return self.driver.swith_to_frame(loc)

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def script(self,src):
        self.driver.execute_script(src)

    def send_keys(self,loc,vaule,clear_first=True,click_first=True):
        try:
            loc=getattr(self,"_%s" %loc)
        if click_first:
            self.find_element(*loc).click()
        if clear_first:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s页面中未能找到%s元素") %(self,loc)
        