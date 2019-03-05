import pytest

from selenium.webdriver.common.by import By

from tests.utils import WebDriverTestCase
from tests.pages.books_page import BooksPage, BookWebElement


class TestSeleniumCompatibility(WebDriverTestCase):
    def test_should_allow_creating_gluten_webelements_from_selenium_webelements(self):
        self.page = BooksPage(self.firefox)
        self.page.open()

        first_book_selenium_element = self.firefox.find_element(By.CSS_SELECTOR, '.book')
        gluten_book_element = BookWebElement.from_selenium_webelement(first_book_selenium_element)

        assert gluten_book_element.title.field_value.text == 'Harry Potter and the Philosopher\'s Stone'
