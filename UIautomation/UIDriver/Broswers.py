# -*-coding=utf-8-*-
from UIDriver.DriverSetUp import DriverEnvironment
from selenium.webdriver.common.by import By


class Broswer(object):
    WebDriver=""
    # def __init__(self, broswer):
    #     self.broswer = broswer
    #     Broswer.WebDriver =

    @staticmethod
    def CreateDriver(broswer):
        Broswer.WebDriver = DriverEnvironment(broswer).CreateWebDriver()

    # def CreateDriver(self):
    #     self.driver = DriverEnvironment(self.broswer).CreateWebDriver()

    @staticmethod
    def Title():
        return Broswer.WebDriver.title

    @staticmethod
    def Url():
        return Broswer.WebDriver.current_url

    @staticmethod
    def Goto(url):
        Broswer.WebDriver.get(url)

    @staticmethod
    def end():
        Broswer.WebDriver.quit()

    @staticmethod
    def TakeScreenShort(path):
        Broswer.WebDriver.save_screenshot(path)

    @staticmethod
    def back():
        Broswer.WebDriver.back()

    @staticmethod
    def forward():
        Broswer.WebDriver.forward()

    @staticmethod
    def refresh():
        Broswer.WebDriver.refresh()
        #self.WebDriver.find_element(By.ID,'jdjd').send_keys()
