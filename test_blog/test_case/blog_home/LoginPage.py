#coding:utf-8
from selenium.webdriver.common.by import By
from test_case.blog_home import BasePage

class LoginBase(BasePage.Action):
    username_loc=(By.ID,"idInput")
    password_loc=(By.ID,"pwdInput")
    submit_loc=(By.ID,"loginBtn")
    span_loc=(By.CSS_SELECTOR,"div.error-tt>p")
    dynpw_loc=(By.ID,"lbDynPw")
    userid_loc=(By.ID,"spnUid")

    def open(self):
        self._open(self.base_url,self.pagetitle)
    def input_usename(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def show_span(self):
        return self.find_element(*self.span_loc).text
    def swith_DynPw(self):
        self.find_element(*self.dynpw_loc).click()
    def show_userid(self):
        return self.find_element(*self.userid_loc).text
    