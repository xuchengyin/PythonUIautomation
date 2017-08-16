# -*-coding=utf-8-*-
import unittest
import sys
from UIcommon.Utils import Common
from UIDriver.Broswers import Broswer
from PageObject.PageCollection import PageCollection


class TestDmeo(unittest.TestCase):

    def setUp(self):
        Broswer.CreateDriver(Common.getConfig('Broswer'))
        self.Page = PageCollection(Broswer.WebDriver)
    def tearDown(self):
        Broswer.end()
        print 'after test case'

    def testBaiduSearch(self):
        Broswer.Goto(Common.getConfig('Url'))
        self.Page.Baidu.SearchText.inputValue('baidu')
        self.Page.Baidu.SearchButton.click()
        print Broswer.Title()
        print Broswer.Url()


    def test02(self):
        self.assertEqual((2 + 3), 5)
        print 'TestDmeo_02'



if __name__ == '__main__':
    pass
