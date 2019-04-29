#!//usr/bin/env python
#coding:utf-8

import csv

def getCsv(value1,value2,file_name='test.csv'):
    rows=[]
    with open(file_name,'rb') as f:
        readers=csv.reader(f,delimiter=',',quotechar='|')
        next(readers,None)
        for row in readers:
            rows.append(row)
            return rows[value1][value2]

def writeCsv(file_name='test.csv'):
    with open(file_name,'wb') as f:
        write=csv.writer(f)
        write.writerow(['Element','system'])
        data=[('selenium','webdriver'),
              ('appium','android'),
              ('appium','ios'),
              ('selenium','python')]
        write.writerow(data)
        f.close()

if __name__ == '__main__':
    writeCsv()
    getCsv()






