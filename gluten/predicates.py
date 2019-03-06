from selenium.webdriver.common.by import By

from gluten import dynamic_locate


class Predicate(object):
    def __init__(self, predicate_fun=None):
        self.predicate_fun = predicate_fun

    def __call__(self, webelement):
        return self.predicate_fun(webelement)

    def __get__(self, obj, type):
        return self(obj)


class Not(Predicate):
    def __init__(self, predicate_fun):
        super(Not, self).__init__(lambda webelement: not predicate_fun(webelement))


class HasClassPredicate(Predicate):
    def __init__(self, class_to_check):
        super(HasClassPredicate, self).__init__(lambda webelement: webelement.has_class(class_to_check))


class HasElementPredicate(Predicate):
    def __init__(self, selector, by=By.CSS_SELECTOR):
        super(HasElementPredicate, self).__init__(lambda webelement: dynamic_locate(webelement, selector, by).exists())
