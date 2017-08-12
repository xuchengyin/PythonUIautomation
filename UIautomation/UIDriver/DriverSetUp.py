# -*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ChromeOptions
import getpass

user = getpass.getuser()


class DriverEnvironment(object):
    def __init__(self, driverType):
        self.type = driverType
        self.Driver=''

    def CreateWebDriver(self):
        if self.type == 'Chrome':
            driverPath=r'../Lib/chromedriver.exe'
            #options=ChromeOptions()
            self.Driver = webdriver.Chrome(driverPath)
        elif self.type == 'IE':
            Iepath=r'../Lib/IEDriverServer.exe'
            Driver = webdriver.Ie(Iepath)
        elif self.type == 'Firefox':
            profileStr = r"C:\Users\ " + user + " \\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\1fwjeevt.default"
            profileStr = profileStr.replace(" ", "")
            binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            profile = FirefoxProfile(profileStr)
            self.Driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
        self.Driver.maximize_window()
        self.Driver.implicitly_wait(30)
        return self.Driver
