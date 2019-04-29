#coding:utf-8
from test_case.blog_set.Second import Yoyo

login_url="https://passport.cnblogs.com/user/sigin"

class LoginPage(Yoyo):
    username_loc=("id","input1")
    password_loc=("id","input2")
    submit_loc=("id","sigin")
    remeber_loc=("id","remeber_me")
    retrieve_loc=('link text','找回')
    reset_loc=('link text','重置')
    register_loc=('link text','立即注册')
    feedback_loc=('link text','反馈问题')
    def input_username(self,username):
        self.send_keys(self.username_loc,username)
    def input_password(self,password):
        self.send_keys(self.password_loc,password)
    def click_submit(self):
        self.click(self.submit_loc)
    def click_remeber_live(self):
        self.click(self.remeber_loc)
    def click_retrieve(self):
        self.click(self.retrieve_loc)
    def click_reset(self):
        self.click(self.reset_loc)
    def click_register(self):
        self.click(self.register_loc)
    def click_feedback(self):
        self.click(self.feedback_loc)
    def login(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_submit()