# -*-coding=utf-8-*-
import unittest
import sys


class TestDmeo(unittest.TestCase):
    def setUp(self):
        print 'before test case 11111111'

    def tearDown(self):
        print 'after test case'

    def test01(self):
        print 'TestDmeo_01'

    def test02(self):
        self.assertEqual((2 + 3), 5)
        print 'TestDmeo_02'



if __name__ == '__main__':
    pass
