from selenium.common.exceptions import TimeoutException, NoSuchElementException

from gluten.values_wrappers import ValuesList, ValuesDict


class FoundElementWrapper(object):
    def __init__(self, context, selector, by, webelement_class):
        self.context = context
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __getitem__(self, item):
        return self._element[item]

    def exists(self):
        try:
            _ = self._element
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @property
    def _element(self):
        found_element = self.context._find_element(self.by, self.selector)
        found_element.__class__ = self.webelement_class
        return found_element

    def __getattr__(self, attr_name):
        return getattr(self._element, attr_name)


class ManyFoundElementsListWrapper(object):
    def __init__(self, context, selector, by, webelement_class):
        self.context = context
        self.selector = selector
        self.by = by
        self.webelement_class = webelement_class

    def __getitem__(self, key):
        return self._elements[key]

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    @property
    def _elements(self):
        found_elements = self.context._find_elements(self.by, self.selector)
        for element in found_elements:
            element.__class__ = self.webelement_class
        return found_elements

    def values(self, attribute_name):
        return ValuesList(self._elements).values(attribute_name)


class DictElementWrapper(ManyFoundElementsListWrapper):
    def __init__(self, context, selector, by, webelement_class, key):
        super().__init__(context, selector, by, webelement_class)
        self.key = key

    def items(self):
        return self._elements.items()

    def keys(self):
        return self._elements.keys()

    def values(self, attribute_name):
        return ValuesDict(self._elements).values(attribute_name)

    def __contains__(self, key):
        return key in self._elements

    def __iter__(self):
        return iter(self._elements.values())

    @property
    def _elements(self):
        found_elements = super()._elements
        return {self.key(element): element for element in found_elements}
