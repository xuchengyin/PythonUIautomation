# -*-coding=utf-8-*-

import unittest
import sys
import os
import re
import HTMLTestRunner
import time

def testSuite():
    # path = os.path.abspath(os.path.dirname(sys.argv[0]))
    # filesList = os.listdir(path)
    # test=re.compile('^test',re.IGNORECASE)
    # files=filter(test.search,filesList)
    # print files
    files = ['test01.py', 'test02.py', 'test03.py']
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    mous = map(filenameToModuleName, files)
    mouss = map(__import__, mous)
    load = unittest.defaultTestLoader.loadTestsFromModule
    suite = unittest.TestSuite(map(load, mouss))
    return suite


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    file='D:\\UI\\PythonUIautomation\\TestResult\\'+now+'report.html'
    with(open(file,'wb')) as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test',description='test')
        runner.run(testSuite())

