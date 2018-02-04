import pytest

from gluten.element_wrappers import FoundElementWrapper

from tests.utils import WebDriverTestCase
from tests.pages.diffrent_locators_page import DiffrentLocatorsPage
from tests.pages.books_page import BooksPage


class TestLocate(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestLocate, cls).setup_class(firefox)
        cls.page = DiffrentLocatorsPage(driver=cls.firefox)
        cls.page.open()

    def test_should_locate_elements_using_diffrent_searching_methods(self):
        assert self.page.located_by_id.text == 'To be located with id'
        assert self.page.located_by_tag_name.text == 'To be located by tag name'
        assert self.page.located_by_name.text == 'To be located by name'
        assert self.page.located_by_link_text.text == 'link text'
        assert self.page.located_by_class_name.text == 'To be located with class name'
        assert self.page.located_by_css_selector.text == 'To be located with css selector'
        assert self.page.located_by_xpath.text == 'To be located with XPath'

    def test_should_return_first_element_when_multiple_elemnts_matches_selector(self):
        assert self.page.located_by_id.text == 'To be located with id'

    def test_should_return_wrapped_found_element(self):
        page = BooksPage(driver=self.firefox)
        page.open()

        assert isinstance(page.first_book, FoundElementWrapper)

    def test_should_not_allow_to_modify_elements(self):
        with pytest.raises(AttributeError):
            self.page.located_by_id = None
