# -*-coding=utf-8-*-
from support.logging import Log
from UIDriver.Broswers import Broswer
from selenium.common.exceptions import NoSuchElementException
import time
from support.logging import Log
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Element(object):
    def __init__(self, webElement):
        if webElement == None:
            try:
                now = time.strftime('%Y-%m-%d-%H-%M-%S')
                url = Broswer.Url()
                print ('current url %s' % url)
                path = os.path.abspath('\Tempfile' + now + '.png')
                print ('screenshot %s' % path)

            except Exception as e:
                Log.LogException(e.message)
                raise NoSuchElementException()

        self.element = webElement

    def isDisplayed(self):
        try:
            Log.LogAction('is displayed')
            return self.element.is_displayed()
        except Exception as e:
            Log.LogException(e.message)

    def isEnable(self):
        try:
            Log.LogAction('is enableed')
            return self.element.is_enabled()
        except Exception as e:
            Log.LogException(e.message)

    def GetCssValue(self,value):
        Log.LogAction('get css value')
        return self.element.


    def GetAttributeValue(self,value):


    def GetDisplayText(self):

    def MoveToElement(self):

    def ScrollIntoView(self):



class CheckBox(Element):
    def __init__(self, webElement):
        Element.__init__(self, webElement)

    def Check(self):
        if not self.element.Selected():
            self.element.click()


class Click(Element):
    def __init__(self, webElement):
        Element.__init__(self, webElement)

    def click(self):
        self.element.click()


class TextField(Element):
    def __init__(self, webElement):
        Element.__init__(self, webElement)

    def inputValue(self, value):
        self.element.send_keys(value)


class DropdwonList(Element):
    def __init__(self, webElement):
        Element.__init__(self, webElement)
