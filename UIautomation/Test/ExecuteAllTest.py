# -*-coding=utf-8-*-

import unittest
import sys
import os
import re


def testSuite():
    # path = os.path.abspath(os.path.dirname(sys.argv[0]))
    # filesList = os.listdir(path)
    # test=re.compile('test\.py{1}quot',re.IGNORECASE)
    files = ['test01.py', 'test02.py', 'test03.py']
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    mous = map(filenameToModuleName, files)
    mouss = map(__import__, mous)
    load = unittest.defaultTestLoader.loadTestsFromModule
    suite = unittest.TestSuite(map(load, mouss))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='testSuite')
