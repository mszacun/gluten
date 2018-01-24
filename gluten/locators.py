from selenium.webdriver.common.by import By


class Locate(object):
    def __init__(self, selector, by=By.CSS_SELECTOR):
        self.selector = selector
        self.by = by

    def __get__(self, obj, type):
        return obj._find_element(self.by, self.selector)
