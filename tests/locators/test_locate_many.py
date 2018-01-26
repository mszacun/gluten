from tests.pages.books_page import BooksPage, BookWebElement

from tests.utils import WebDriverTestCase


class TestLocateMany(WebDriverTestCase):
    def setUp(self):
        super(TestLocateMany, self).setUp()
        self.page = BooksPage(driver=self.driver)
        self.page.open()

    def test_should_allow_locate_many_elements_from_web_element(self):
        harry_potter_expected_chapters = ['The boy who lived', 'The vanishing glass', '...']

        self.assertEqual([chapter.text for chapter in self.page.first_book.chapters], harry_potter_expected_chapters)

    def test_should_allow_locate_many_elements_from_page_object(self):
        expected_books = ["Harry Potter and the Philosopher's Stone",
                          "The Lord of the Rings: The Fellowship of the Ring",
                          "The Da Vinci Code",
                          "The Catcher in the Rye",
                          ]
        actual_books = [book.title.field_value.text for book in self.page.books]
        self.assertEqual(actual_books, expected_books)

    def test_should_allow_to_use_square_brackets_to_get_element(self):
        self.assertEqual(self.page.books[1].title.field_value.text, "The Lord of the Rings: The Fellowship of the Ring")
        self.assertEqual(self.page.books[2].title.field_value.text, "The Da Vinci Code")

    def test_should_allow_to_get_number_of_found_items_using_len_operator(self):
        self.assertEqual(len(self.page.books), 4)

