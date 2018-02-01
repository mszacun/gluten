from gluten.element_wrappers import FoundElementWrapper

from tests.pages.diffrent_locators_page import DiffrentLocatorsPage
from tests.pages.books_page import BooksPage
from tests.utils import WebDriverTestCase


class TestLocate(WebDriverTestCase):
    def setUp(self):
        super(TestLocate, self).setUp()

        self.page = DiffrentLocatorsPage(driver=self.driver)
        self.page.open()

    def test_should_locate_elements_using_diffrent_searching_methods(self):
        self.assertEqual(self.page.located_by_id.text, 'To be located with id')
        self.assertEqual(self.page.located_by_tag_name.text, 'To be located by tag name')
        self.assertEqual(self.page.located_by_name.text, 'To be located by name')
        self.assertEqual(self.page.located_by_link_text.text, 'link text')
        self.assertEqual(self.page.located_by_class_name.text, 'To be located with class name')
        self.assertEqual(self.page.located_by_css_selector.text, 'To be located with css selector')
        self.assertEqual(self.page.located_by_xpath.text, 'To be located with XPath')

    def test_should_return_first_element_when_multiple_elemnts_matches_selector(self):
        self.assertEqual(self.page.located_by_id.text, 'To be located with id')

    def test_should_return_wrapped_found_element(self):
        self.page = BooksPage(driver=self.driver)
        self.page.open()

        element = self.page.first_book
        self.assertTrue(isinstance(element, FoundElementWrapper))

    def test_should_not_allow_to_modify_elements(self):
        with self.assertRaises(AttributeError):
            self.page.located_by_id = None
