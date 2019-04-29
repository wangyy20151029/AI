#-*-coding:utf-8
from selenium import webdriver
import sys
from time import sleep
from threading import Thread

def test_baidu_search(browser,url):
    driver=None
    if browser=="ie":
        driver=webdriver.Ie()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="chrome":
        driver=webdriver.Chrome()
    if driver==None:
        exit()

    driver.get(url)
    sleep(3)

    driver.find_element_by_id("sw").send_keys(u"baidu")
    sleep(3)

    driver.find_element_by_id("id").click()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    data={"ie":"https://www.baidu.comn",
          "firefox":"https://www.qq.com",
          "chrome":"https://www.163.com"}

    threads=[]
    for b,url in data.items():
        t=Thread(target=test_baidu_search,args=(b,url))
        threads.append(t)

    for thr in threads:
        thr.start()
