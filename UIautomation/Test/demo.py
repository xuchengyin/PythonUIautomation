# -*-coding=utf-8-*-
import xlrd
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from UIDriver.Broswers import Broswer


# filepath='E:\\old\\TestData_Default.xlsx'
# xls=xlrd.open_workbook(filepath)

def test():
    print 'cessssss'
    te = lambda x: True if len(x) == 5 else False
    return te('sss')


Broswer.CreateDriver('Firefox')
Broswer.Goto('Http://www.baidu.com')
element=WebDriverWait(Broswer.WebDriver, 30).until(EC.visibility_of_element_located((By.ID, 'kw')),'fail')
element.send_keys('test')
