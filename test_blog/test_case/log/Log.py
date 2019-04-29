import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler_warm=logging.FileHandler("warning_log.txt")
handler_warm.setLevel(logging.WARNING)

handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warm.setFormatter(formatter)
handler_info.setFormatter(formatter)

logger.addHandler(handler_warm)
logger.addHandler(handler_info)

logger.info('Information')
logger.warning('warning')

def age():
    logger.info('Inside function age()')
    try:
        logger.info('In the try Block')
        age = int(input('请输入你当前年龄'))
        logger.debug('Value of age is %s' %age)
    except ValueError as e:
        logger.critical('Invalid Input',exc_info=True)

class YoutubeSearch(unittest.TestCase):

    def setUp(self):
        logger.info("---xxx---")
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.baidu.com")
        logger.info("====xxxx====")

    def tearDown(self):
        logger.info("-----xxxxx-----")
        self.browser.save_screenshot('xxx.png')
        self.browser.quit()
        logger.info("======xxxxxx======")

    def test_youtube_search(self):
        logger.info("=======xxxxxxx=======")

        try:
            self.assertIn("xxx",self.browser.title)
            searchElement=self.browser.find_element_by_id("xxx")
        except AssertionError:
            logger.critical('xxx',Jexc_info=True)
            self.fail('xxx')
        else:
            searchElement.send_keys("xxxx")
            searchElement.send_keys(Keys.RETURN)
            logger.info("---------xxx---------")



if __name__ == '__main__':
    unittest.main(exit=False,warnings='ignore')
