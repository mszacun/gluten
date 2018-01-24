from gluten.webelement import WebElement

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import get_fixture_url


class BookFieldWebElement(WebElement):
    field_name = Locate('.field-name')
    field_value = Locate('.field-value')


class BookWebElement(WebElement):
    title = Locate('.title', webelement_class=BookFieldWebElement)
    author = Locate('.author', webelement_class=BookFieldWebElement)
    isbn = Locate('.isbn', webelement_class=BookFieldWebElement)


class BooksPage(Page):
    first_book = Locate('.book', webelement_class=BookWebElement)

    def open(self):
        fixture_url = get_fixture_url('test_web_elements_fixture.html')
        self._go_to_url(fixture_url)

