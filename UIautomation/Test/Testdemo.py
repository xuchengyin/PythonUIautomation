# -*-coding=utf-8-*-
from UIcommon.Utils import Common
from UIDriver.Broswers import Broswer
from PageObject.PageCollection import PageCollection
import os
import sys


def test():
    # Broswer.CreateDriver(Common.getConfig('Broswer'))
    # Page = PageCollection(Broswer.WebDriver)
    # Broswer.Goto(Common.getConfig('Url'))
    # Page.Baidu.SearchText.inputValue('baidu')
    # Page.Baidu.SearchButton.click()
    # print Page.Baidu.SearchButton.isEnable()
    # print Broswer.Title()
    # print Broswer.Url()
    path=os.path.abspath(os.path.dirname(sys.argv[0]))
    files=os.listdir(path)
    for file in files:
        print file





if __name__ == "__main__":
    test()
