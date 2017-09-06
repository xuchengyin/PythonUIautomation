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
    def TakeScreenShort(name):
        path=r'D:\UI\PythonUIautomation\TestResult\Tempfile'
        Broswer.WebDriver.save_screenshot(path+name+'.png')

    @staticmethod
    def back():
        Broswer.WebDriver.back()

    @staticmethod
    def forward():
        Broswer.WebDriver.forward()

    @staticmethod
    def refresh():
        Broswer.WebDriver.refresh()
