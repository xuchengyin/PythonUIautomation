# -*-coding=utf-8-*-
from UIcommon.Utils import Common
from UIDriver.Broswers import Broswer
from PageObject.PageCollection import PageCollection


def test():
    Page=PageCollection()
    Broswer.CreateDriver(Common.getConfig('Broswer'))
    Broswer.Goto(Common.getConfig('Url'))
    Page.Baidu.SearchText.inputValue('baidu')
    Page.Baidu.SearchButton.click()
    print Page.Baidu.SearchButton.isEnable()
    print Broswer.Title()
    print Broswer.Url()




if __name__ == "__main__":
    test()
