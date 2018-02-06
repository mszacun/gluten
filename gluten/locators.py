from selenium.webdriver.common.by import By

from gluten.webelements.base import WebElement
from gluten.element_wrappers import FoundElementWrapper, ManyFoundElementsListWrapper, DictElementWrapper


LOCAL_SCOPE_GETTER = lambda obj: obj._get_local_search_scope()
GLOBAL_SCOPE_GETTER = lambda obj: obj._get_global_search_scope()


class LocateBase(object):
    search_scope_getter = LOCAL_SCOPE_GETTER

    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __set__(self, instance, value):
        raise AttributeError

    def _get_search_scope_getter(self, obj):
        return self.__class__.search_scope_getter(obj)


class Locate(LocateBase):
    def __get__(self, obj, type):
        return FoundElementWrapper(self._get_search_scope_getter(obj), self.selector, self.by, self.webelement_class)


class LocateMany(LocateBase):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement, key=None):
        super(LocateMany, self).__init__(selector, by, webelement_class)
        self.key = key

    def __get__(self, obj, type):
        search_scope = self._get_search_scope_getter(obj)
        if self.key:
            return DictElementWrapper(search_scope, self.selector, self.by, self.webelement_class, self.key)
        return ManyFoundElementsListWrapper(search_scope, self.selector, self.by, self.webelement_class)


class LocateGlobal(Locate):
    search_scope_getter = GLOBAL_SCOPE_GETTER


class LocateGlobalMany(LocateMany):
    search_scope_getter = GLOBAL_SCOPE_GETTER
