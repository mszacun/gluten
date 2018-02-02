def get_attribute_from_elements(elements, attribute_name):
    return [get_attribute_from_element(element, attribute_name) for element in elements]

def get_attribute_from_element(element, attribute_name):
    if hasattr(element, '__iter__'):
        return get_attribute_from_elements(element, attribute_name)
    else:
        return getattr(element, attribute_name)


class ValuesList(object):
    def __init__(self, values_list):
        self.values_list = values_list

    def values(self, attribute_name):
        return ValuesList(get_attribute_from_elements(self.values_list, attribute_name))

    def __iter__(self):
        return iter(self.values_list)


class ValuesDict(object):
    def __init__(self, values_dict):
        self.values_dict = values_dict

    def values(self, attribute_name):
        return ValuesDict({key: get_attribute_from_element(value, attribute_name)
                           for key, value in self.values_dict.items()})

    def __iter__(self):
        return iter(self.values_dict.values())

    def items(self):
        return self.values_dict.items()
