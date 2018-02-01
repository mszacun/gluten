from tests.pages.books_page import BooksPage

from tests.utils import WebDriverTestCase


class TestLocateMany(WebDriverTestCase):
    listed_books = [
        "Harry Potter and the Philosopher's Stone",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Da Vinci Code",
        "The Catcher in the Rye"
    ]

    def setUp(self):
        super(TestLocateMany, self).setUp()
        self.page = BooksPage(driver=self.driver)
        self.page.open()

    def test_should_allow_locate_many_elements_from_web_element(self):
        harry_potter_expected_chapters = ['The boy who lived', 'The vanishing glass', '...']

        self.assertEqual([chapter.text for chapter in self.page.first_book.chapters], harry_potter_expected_chapters)

    def test_should_allow_locate_many_elements_from_page_object(self):
        actual_books = [book.title.field_value.text for book in self.page.books]
        self.assertEqual(actual_books, self.listed_books)

    def test_should_allow_to_use_square_brackets_to_get_element(self):
        self.assertEqual(self.page.books[1].title.field_value.text, "The Lord of the Rings: The Fellowship of the Ring")
        self.assertEqual(self.page.books[2].title.field_value.text, "The Da Vinci Code")

    def test_should_allow_to_get_number_of_found_items_using_len_operator(self):
        self.assertEqual(len(self.page.books), 4)

    def test_should_let_access_elements_by_given_key(self):
        for book, book_title in zip(self.page.books, self.listed_books):
            self.assertEqual(book.title.field_value.text, self.page.books_by_titles[book_title].title.field_value.text)

    def test_should_allow_to_get_number_of_found_items_using_len_operator_while_using_dict_wrapper(self):
        self.assertEqual(len(self.page.books_by_titles), 4)

    def test_should_allow_to_use_contains_operator_while_using_dict_wrapper(self):
        self.assertTrue("The Da Vinci Code" in self.page.books_by_titles)
        self.assertFalse("Commenting out tests" in self.page.books_by_titles)

    def test_should_allow_to_iterate_with_keys_method_while_using_dict_wrapper(self):
        for key, book in self.page.books_by_titles.items():
            self.assertEqual(key, book.title.field_value.text)

    def test_should_return_keys_for_keys_method_while_using_dict_wrapper(self):
        self.assertListEqual(self.listed_books, list(self.page.books_by_titles.keys()))

    def test_should_not_allow_to_modify_elements(self):
        with self.assertRaises(AttributeError):
            self.page.books = []
        with self.assertRaises(AttributeError):
            self.page.books_by_titles = {}
