import pytest

from gluten import LocateOneOfMany
from gluten.predicates import HasClassPredicate

from tests.pages.books_page import BooksPage, BookWebElement

from tests.utils import WebDriverTestCase


class BooksPageWithOneOfManyLocators(BooksPage):
    new_book_lambda_predicate = LocateOneOfMany('.book', lambda webelement: webelement.has_class('new'),
                                                webelement_class=BookWebElement)
    new_book_class_predicate = LocateOneOfMany('.book', HasClassPredicate('new'), webelement_class=BookWebElement)
    none_element_matching_predicate = LocateOneOfMany('.book', lambda webelement: False,
                                                      webelement_class=BookWebElement)


class TestLocateOneOfMany(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestLocateOneOfMany, cls).setup_class(firefox)
        cls.page = BooksPageWithOneOfManyLocators(driver=cls.firefox)
        cls.page.open()

    def test_should_locate_one_of_many_element_using_lambda_predicate(self):
        assert self.page.new_book_lambda_predicate.title.field_value.text == 'The Catcher in the Rye'

    def test_should_locate_one_of_many_element_using_class_predicate(self):
        assert self.page.new_book_class_predicate.title.field_value.text == 'The Catcher in the Rye'

    def test_should_exists_method_return_false_when_none_element_matches_predicate(self):
        assert not self.page.none_element_matching_predicate.exists()
