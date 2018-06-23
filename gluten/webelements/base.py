from selenium.webdriver.remote import webelement

from gluten.search_scope import SearchScope


class WebElement(webelement.WebElement):
    def _get_local_search_scope(self):
        return SearchScope(self)

    def _get_global_search_scope(self):
        return SearchScope(self.parent)

    @property
    def is_displayed(self):
        return self.value_of_css_property('display') != 'none'

    @property
    def is_visible(self):
        return self.value_of_css_property('visibility') != 'hidden'

    @property
    def classes(self):
        return self.get_attribute('class').split()

    def has_class(self, class_name):
        return class_name in self.classes

