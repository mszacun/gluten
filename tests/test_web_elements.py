from tests.pages.books_page import BooksPage, BookWebElement
from tests.utils import WebDriverTestCase


class TestLocate(WebDriverTestCase):
    def setUp(self):
        super(TestLocate, self).setUp()

        self.page = BooksPage(driver=self.driver)
        self.page.open()

    def test_should_allow_to_nest_web_element_inside_another_web_element(self):
        self.assertEqual(self.page.first_book.title.field_name.text, 'Title:')
        self.assertEqual(self.page.first_book.title.field_value.text, "Harry Potter and the Philosopher's Stone")

        self.assertEqual(self.page.first_book.author.field_name.text, 'Author:')
        self.assertEqual(self.page.first_book.author.field_value.text, 'J. K. Rowling')

        self.assertEqual(self.page.first_book.isbn.field_name.text, 'ISBN:')
        self.assertEqual(self.page.first_book.isbn.field_value.text, '0747532699')

