from gluten.locators import Locate, LocateMany
from gluten.page import Page
from gluten.webelement import WebElement
from tests.utils import get_fixture_url


class BookFieldWebElement(WebElement):
    field_name = Locate('.field-name')
    field_value = Locate('.field-value')


class BookWebElement(WebElement):
    title = Locate('.title', webelement_class=BookFieldWebElement)
    author = Locate('.author', webelement_class=BookFieldWebElement)
    isbn = Locate('.isbn', webelement_class=BookFieldWebElement)
    table_of_contents_header = Locate('.table-title')
    chapters = LocateMany('.chapter')


class BooksPage(Page):
    first_book = Locate('.book', webelement_class=BookWebElement)
    books = LocateMany('.book', webelement_class=BookWebElement)
    books_by_titles = LocateMany('.book', webelement_class=BookWebElement, key=lambda book: book.title.field_value.text)

    def open(self):
        fixture_url = get_fixture_url('test_web_elements_fixture.html')
        self._go_to_url(fixture_url)
