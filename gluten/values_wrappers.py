class ValuesList(object):
    def __init__(self, values_list):
        self.values_list = values_list

    def values(self, attribute_name):
        return ValuesList(self._get_attribute_from_elements(self.values_list, attribute_name))

    def _get_attribute_from_elements(self, elements, attribute_name):
        return [self._get_attribute_from_element(element, attribute_name) for element in elements]

    def _get_attribute_from_element(self, element, attribute_name):
        if hasattr(element, '__iter__'):
            return self._get_attribute_from_elements(element, attribute_name)
        else:
            return getattr(element, attribute_name)

    def __iter__(self):
        return iter(self.values_list)
