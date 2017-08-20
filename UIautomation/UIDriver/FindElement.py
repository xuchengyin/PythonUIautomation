# -*-coding=utf-8-*-
from selenium.webdriver.support.wait import WebDriverWait
from Broswers import Broswer
from support.logging import Log
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

'''
:parameter
locator:By
'''


def GetElement(locator):
    try:
        wait = WebDriverWait(Broswer.WebDriver, 30)
        element = wait.until(EC.visibility_of_element_located(locator), 'element not fond')
        return element
    except Exception as e:
        Log.LogException(e.message)
