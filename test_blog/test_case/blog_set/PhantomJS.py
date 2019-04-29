from selenium import webdriver

driver=webdriver.PhantomJS()
driver.get("https://www.qq.com")
data = driver.title
print(data)