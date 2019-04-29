#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
mouse = WebDriverWait(driver,10).until(lambda x: x.find_element("link text","设置"))
ActionChains(driver).move_to_element(mouse).perform()
WebDriverWait(driver,10).until(lambda x: x.find_element("link text","搜素设置")).click()

s = WebDriverWait(driver,10).until(lambda x: x.find_element("id","nr"))
Select(s).select_by_visible_text("每页显示50条")

js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)

result = EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.acccpt()
else:
    print("alert未弹出")