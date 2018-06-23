from selenium.webdriver.remote.webelement import WebElement

from gluten.search_scope import SearchScope


class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver._web_element_cls = WebElement

    def _go_to_url(self, url):
        self.driver.get(url)

    def _get_local_search_scope(self):
        return SearchScope(self.driver)

    def _get_global_search_scope(self):
        raise NotImplemented("Global scope is default for page object - please don't use global locators")
