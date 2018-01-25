from selenium.webdriver.common.by import By

from gluten.webelement import WebElement
from gluten.element_wrappers import FoundElementWrapper


class Locate(object):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __get__(self, obj, type):
        return FoundElementWrapper(obj, self.selector, self.by, self.webelement_class)
