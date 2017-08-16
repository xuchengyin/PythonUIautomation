# -*-coding=utf-8-*-
import unittest
import sys


class TestDmeo2(unittest.TestCase):
    def setUp(self):
        print 'before test case 11111111'

    def tearDown(self):
        print 'after test case'

    def test01(self):
        print 'TestDmeo2_01'

    def test02(self):
        self.assertEqual((2 + 3), 5)
        print 'TestDmeo2_02'



if __name__ == '__main__':
    pass