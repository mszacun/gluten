from selenium.webdriver.common.by import By

from gluten.webelements.base import WebElement
from gluten.element_wrappers import FoundElementWrapper, ManyFoundElementsListWrapper, DictElementWrapper


LOCAL_SCOPE_GETTER = lambda obj: obj._get_local_search_scope()
GLOBAL_SCOPE_GETTER = lambda obj: obj._get_global_search_scope()


def dynamic_locate(context, selector, by=By.CSS_SELECTOR, scope_getter=LOCAL_SCOPE_GETTER, webelement_class=WebElement):
    return FoundElementWrapper(scope_getter(context), selector, by, webelement_class)


def dynamic_locate_many(context, selector, by=By.CSS_SELECTOR, scope_getter=LOCAL_SCOPE_GETTER,
                        webelement_class=WebElement, key=None):
    search_scope = scope_getter(context)
    if key:
        return DictElementWrapper(search_scope, selector, by, webelement_class, key)
    return ManyFoundElementsListWrapper(search_scope, selector, by, webelement_class)


class LocateBase(object):
    search_scope_getter = LOCAL_SCOPE_GETTER

    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement):
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __set__(self, instance, value):
        raise AttributeError


class Locate(LocateBase):
    def __get__(self, obj, type):
        return dynamic_locate(obj, self.selector, self.by, self.__class__.search_scope_getter, self.webelement_class)


class LocateMany(LocateBase):
    def __init__(self, selector, by=By.CSS_SELECTOR, webelement_class=WebElement, key=None):
        super(LocateMany, self).__init__(selector, by, webelement_class)
        self.key = key

    def __get__(self, obj, type):
        return dynamic_locate_many(obj, self.selector, self.by, self.__class__.search_scope_getter,
                                   self.webelement_class, self.key)


class LocateGlobal(Locate):
    search_scope_getter = GLOBAL_SCOPE_GETTER


class LocateGlobalMany(LocateMany):
    search_scope_getter = GLOBAL_SCOPE_GETTER
