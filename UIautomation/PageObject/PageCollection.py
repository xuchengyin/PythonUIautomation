# -*-coding=utf-8-*-
from baiduPage import Baidu
from UIDriver.Broswers import Broswer


class PageCollection(object):

    @staticmethod
    @property
    def Baidu():
        return Baidu(Broswer.WebDriver)