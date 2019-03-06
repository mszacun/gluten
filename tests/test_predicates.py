import pytest

from gluten import WebElement, LocateMany, dynamic_locate
from gluten.predicates import Predicate, HasClassPredicate, HasElementPredicate, Not

from tests.utils import WebDriverTestCase
from tests.pages.diffrent_locators_page import DiffrentLocatorsPage
from tests.pages.books_page import BooksPage


class BookWebElementWithPredicate(WebElement):
    is_available_predicate_with_passed_lambda = Predicate(lambda elem: dynamic_locate(elem, '.availability').text == 'AVAILABLE')
    is_new_has_class_predicate = HasClassPredicate('new')
    is_not_available_has_element_predicate = HasElementPredicate('.not-available')
    is_available_with_not_has_element_predicate = Not(HasElementPredicate('.not-available'))


class PageWithPredicates(BooksPage):
    books_with_predicates = LocateMany('.book', webelement_class=BookWebElementWithPredicate)


class TestPredicates(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestPredicates, cls).setup_class(firefox)
        cls.page = PageWithPredicates(driver=cls.firefox)
        cls.page.open()

    def test_should_allow_passing_lambda_to_predicate_and_use_it_as_descriptor(self):
        assert self.page.books_with_predicates[0].is_available_predicate_with_passed_lambda
        assert self.page.books_with_predicates[1].is_available_predicate_with_passed_lambda
        assert not self.page.books_with_predicates[2].is_available_predicate_with_passed_lambda
        assert self.page.books_with_predicates[3].is_available_predicate_with_passed_lambda

    def test_has_class_predicate(self):
        assert not self.page.books_with_predicates[0].is_new_has_class_predicate
        assert not self.page.books_with_predicates[1].is_new_has_class_predicate
        assert not self.page.books_with_predicates[2].is_new_has_class_predicate
        assert self.page.books_with_predicates[3].is_new_has_class_predicate

    def test_has_element_predicate(self):
        assert not self.page.books_with_predicates[0].is_not_available_has_element_predicate
        assert not self.page.books_with_predicates[1].is_not_available_has_element_predicate
        assert self.page.books_with_predicates[2].is_not_available_has_element_predicate
        assert not self.page.books_with_predicates[3].is_not_available_has_element_predicate

    def test_negating_predicates(self):
        assert self.page.books_with_predicates[0].is_available_with_not_has_element_predicate
        assert self.page.books_with_predicates[1].is_available_with_not_has_element_predicate
        assert not self.page.books_with_predicates[2].is_available_with_not_has_element_predicate
        assert self.page.books_with_predicates[3].is_available_with_not_has_element_predicate
