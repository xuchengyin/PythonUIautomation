# -*-coding=utf-8-*-
from ElementAction.Action import TextField
from ElementAction.Action import Click
from selenium.webdriver.common.by import By
import UIDriver.FindElement as FindElement


class Baidu(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def SearchText(self):
        element = FindElement.GetElement((By.ID, 'kw'))
        return TextField(element) if element is not None else None

    @property
    def SearchButton(self):
        element = FindElement.GetElement((By.ID, 'su'))
        return Click(element) if element is not None else None
