from selenium.webdriver.remote.webelement import WebElement

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import get_fixture_url


class BookWebElement(WebElement):
    pass


class BooksPage(Page):
    first_book = Locate('.book', webelement_class=BookWebElement)

    def open(self):
        fixture_url = get_fixture_url('test_web_elements_fixture.html')
        self._go_to_url(fixture_url)

