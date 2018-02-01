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

    def test_should_allow_to_get_found_elements_attribute_for_each_found_element(self):
        harry_potter_expected_chapters = ['The boy who lived', 'The vanishing glass', '...']
        self.assertEqual(list(self.page.books[0].chapters.values('text')), harry_potter_expected_chapters)

    def test_should_allow_chaining_when_getting_elements_attributes(self):
        self.assertEqual(list(self.page.books.values('avibility').values('text')),
                         ['Aviable', 'Aviable', 'Not aviable', 'Aviable'])

        actual_books_titles = list(self.page.books.values('title').values('field_value').values('text'))
        self.assertEqual(actual_books_titles, self.listed_books)

    def test_should_allow_using_values_method_to_get_attribute_that_is_list_and_chain_to_get_value_for_each_elem(self):
        harry_potter_expected_chapters = ['The boy who lived', 'The vanishing glass', '...']
        lord_of_the_rings_chapters = ['A Long-expected Party', 'The shadow of the Past', '...']
        da_vinci_code_chapters = ['Chapter 1', 'Chapter 2', '...']
        the_catcher_in_the_rye_chapters = da_vinci_code_chapters

        all_books_titles = list(self.page.books.values('chapters').values('text'))
        self.assertEqual(all_books_titles[0], harry_potter_expected_chapters)
        self.assertEqual(all_books_titles[1], lord_of_the_rings_chapters)
        self.assertEqual(all_books_titles[2], da_vinci_code_chapters)
        self.assertEqual(all_books_titles[3], the_catcher_in_the_rye_chapters)

