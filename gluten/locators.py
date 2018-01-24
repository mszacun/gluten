from selenium.webdriver.common.by import By


class Locate(object):
    def __init__(self, selector):
        self.selector = selector

    def __get__(self, obj, type):
        return obj._find_element(By.CSS_SELECTOR, self.selector)
