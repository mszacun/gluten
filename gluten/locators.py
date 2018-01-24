from selenium.webdriver.common.by import By

from gluten.webelement import WebElement


class Locate(object):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __get__(self, obj, type):
        found_element = obj._find_element(self.by, self.selector)
        found_element.__class__ = self.webelement_class

        return found_element
