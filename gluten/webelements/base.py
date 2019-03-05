from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains

from gluten.search_scope import SearchScope


class WebElement(webelement.WebElement):
    @classmethod
    def from_selenium_webelement(cls, selenium_webelement):
        selenium_webelement.__class__ = cls
        return selenium_webelement

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

    def double_click(self):
        ActionChains(self.parent).double_click(self).perform()

    def move_to(self):
        self.parent.execute_script("arguments[0].scrollIntoView(true);", self);

