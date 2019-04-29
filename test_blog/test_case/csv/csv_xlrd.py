#coding:utf-8

import csv,xlrd
from selenium import webdriver
import time as t

def getCsv(file_name):
    rows=[]
    with open(file_name,'rb') as f:
        readers=csv.reader(f,delimiters=',',quotechar='|')
    next(readers,None)
    for row in readers:
        rows.append(row)
    return rows

def getExcel(rowValue,colValue,file_name='test.xlsx'):
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_index(0)
    return sheet.cell_value(rowValue,colValue)

def clickButton(driver):
    driver.find_element_by_xpath("xxx").click()
    t.sleep(2)

def clickLogin(driver,username,password):
    name=driver.find_element_by_id('xxx')
    name.clear()
    name.send_keys(username)
    t.sleep(2)
    passwd=driver.find_element_by_id('xxx')
    passwd.clear()
    passwd.send_keys(password)
    t.sleep(2)
    driver.find_element_by_id('xxx').click()
    t.sleep(2)

def getText(driver):
    return driver.find_element_by_xpath("xxx").text