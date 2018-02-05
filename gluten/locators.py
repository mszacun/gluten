from selenium.webdriver.common.by import By

from gluten.webelements.base import WebElement
from gluten.element_wrappers import FoundElementWrapper, ManyFoundElementsListWrapper, DictElementWrapper


class Locate(object):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __get__(self, obj, type):
        return FoundElementWrapper(obj, self.selector, self.by, self.webelement_class)

    def __set__(self, instance, value):
        raise AttributeError


class LocateMany(object):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement, key=None):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class
        self.key = key

    def __get__(self, obj, type):
        if self.key:
            return DictElementWrapper(obj, self.selector, self.by, self.webelement_class, self.key)
        return ManyFoundElementsListWrapper(obj, self.selector, self.by, self.webelement_class)

    def __set__(self, instance, value):
        raise AttributeError
