# -*-coding=utf-8-*-
from ElementAction import TextField
from ElementAction import clickable
from selenium.webdriver.common.by import By


class Baidu(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def SearchText(self):
        element = self.driver.find_element(By.ID, 'kw')
        return TextField(element)

    @property
    def SearchButton(self):
        element=self.driver.find_element(By.ID, 'su')
        return clickable(element)
