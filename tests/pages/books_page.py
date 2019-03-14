from gluten.locators import Locate, LocateMany, LocateGlobal, LocateGlobalMany
from gluten.page import Page
from gluten.webelements.base import WebElement
from tests.utils import get_fixture_url


class FutureWebElement(WebElement):
    title = Locate('.title')
    date = Locate('.date')


class BookFieldWebElement(WebElement):
    field_name = Locate('.field-name')
    field_value = Locate('.field-value')


class ChapterWebElement(WebElement):
    title = Locate('.title')
    first_page = Locate('.first-page')


class BestsellerWebElement(WebElement):
    prompt = Locate('.prompt')
    title = Locate('.title')
    books = LocateGlobalMany('.book')
    future_by_title = LocateGlobalMany('.release .item', webelement_class=FutureWebElement, key=lambda future: future.title.text)


class BookWebElement(WebElement):
    title = Locate('.title', webelement_class=BookFieldWebElement)
    author = Locate('.author', webelement_class=BookFieldWebElement)
    isbn = Locate('.isbn', webelement_class=BookFieldWebElement)
    table_of_contents_header = Locate('.table-title')
    chapters = LocateMany('.chapter', webelement_class=ChapterWebElement)
    chapters_by_title = LocateMany('.chapter', webelement_class=ChapterWebElement,
                                   key=lambda chapter: chapter.title.text)
    availability = Locate('.availability')
    bestseller = LocateGlobal('.bestseller', webelement_class=BestsellerWebElement)


class BooksPage(Page):
    first_book = Locate('.book', webelement_class=BookWebElement)
    books = LocateMany('.book', webelement_class=BookWebElement)
    books_by_titles = LocateMany('.book', webelement_class=BookWebElement, key=lambda book: book.title.field_value.text)
    books_by_titles_with_string_key = LocateMany('.book', webelement_class=BookWebElement, key='title.field_value.text')
    bestseller = Locate('.bestseller', webelement_class=BestsellerWebElement)
    non_existing_books = LocateMany('.non-existing-book')
    non_existing_books_by_title = LocateMany('.non-existing-book', key=lambda book: book.title.field_value.text)

    def open(self):
        fixture_url = get_fixture_url('test_web_elements_fixture.html')
        self._go_to_url(fixture_url)
