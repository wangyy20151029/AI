#coding:utf-8
import logging,time,os
import ddt
from ddt import ddt,data,unpack
import pymysql

log_path=""
@ddt
class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log' %time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter('[%(asctime)s] - %(filename)s - %(levelname)s:%(message)s')
        self.addcleanup(self.driver.quit)
        @data(('', '', u'手机/邮箱/用户名'), ('admin', '', u'请您填写密码'),('admin', 'admin', u'您输入的帐号或密码有误，忘记密码？'))
    @unpack
    def __console(self,level,message):
        fh = logging.FileHandler(self.logname,'a',encoding='urf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.format)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        fh.close()

    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)

if __name__ == '__main__':
    log=Log()
    log.info("-----测试开始----")
    log.info("输入密码")
    log.warning("-----测试结束--------")

