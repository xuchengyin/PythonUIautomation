# -*-coding=utf-8-*-
from baiduPage import Baidu
from UIDriver.Broswers import Broswer


class PageCollection(object):
    def __init__(self,driver):
        self.driver=driver

    @property
    def Baidu(self):
        return Baidu(self.driver)