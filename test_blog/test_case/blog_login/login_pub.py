#coding:utf-8


class Login_Blog():
    def __init__(self,driver):
        self.driver = driver

    def input_user(self,username):
        self.driver.find_element_by_id("input1").clear
        self.driver.find_element_by_id("input1").send_keys(username)

    def input_psw(self,psw):
        self.driver.find_element_by_id("input2").clear
        self.driver.find_element_by_id("input2").send_keys(psw)

    def click_button(self):
        self.driver.find_element_by_id("signin").click()

    def login(self,username,psw):
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()