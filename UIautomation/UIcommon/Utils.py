# -*-coding=utf-8-*-
from ConfigParser import ConfigParser


class Common(object):
    @classmethod
    def getConfig(cls, name):
        cp = ConfigParser()
        cp.read('../confige/confige.ini')
        value = cp.get('testBase', name)
        return value


if __name__ == "__main__":
    print (Common.getConfig('Broswer'))
    print (Common.getConfig('Url'))
