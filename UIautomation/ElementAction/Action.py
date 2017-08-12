# -*-coding=utf-8-*-

class CheckBox(Element):
    def __init__(self,webElement):
        Element.__init__(webElement)

    def Check(self):
        if not self.element.Selected():
            self.element.click()


class Click(Element):
    def __init__(self, webElement):
        Element.__init__(webElement)

    def click(self):
        self.element.click()


class TextField(Element):
    def __init__(self, webElement):
        Element.__init__(webElement)

    def inputValue(self, value):
        self.element.send_keys(value)


class DropdwonList(Element):
    def __init__(self,webElement):
        Element.__init__(webElement)


class Element(object):

    def __init__(self, webElement):
        self.element = webElement

    def isDisplayed(self):
        return self.element.is_displayed()

    def isEnable(self):
        return self.element.is_enabled()


