from selenium.webdriver.remote import webelement

from gluten.search_scope import SearchScope


class WebElement(webelement.WebElement):
    def _get_local_search_scope(self):
        return SearchScope(self)

    def _get_global_search_scope(self):
        return SearchScope(self.parent)
