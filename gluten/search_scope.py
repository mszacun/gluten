class SearchScope(object):
    def __init__(self, obj):
        self.obj = obj

    def find_element(self, by, selector):
        return self.obj.find_element(by, selector)

    def find_elements(self, by, selector):
        return self.obj.find_elements(by, selector)
