import pytest

from tests.pages.books_page import BooksPage

from tests.utils import WebDriverTestCase


class TestLocateMany(WebDriverTestCase):
    listed_books = [
        "Harry Potter and the Philosopher's Stone",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Da Vinci Code",
        "The Catcher in the Rye"
    ]

    harry_potter_title = "Harry Potter and the Philosopher's Stone"
    lord_of_the_ring_title = "The Lord of the Rings: The Fellowship of the Ring"
    da_vinci_code_title = "The Da Vinci Code"
    the_catcher_title = "The Catcher in the Rye"

    harry_potter_chapters = ['The boy who lived', 'The vanishing glass', 'The letters from no one']
    lord_of_the_rings_chapters = ['A Long-expected Party', 'The shadow of the Past', 'Three is Company']
    da_vinci_code_chapters = ['Chapter 1', 'Chapter 2', 'Chapter 3']
    the_catcher_chapters = ['Chapter 1', 'Chapter 2', '...']

    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestLocateMany, cls).setup_class(firefox)
        cls.page = BooksPage(driver=cls.firefox)
        cls.page.open()

    def test_should_allow_locate_many_elements_from_web_element(self):
        assert [chapter.title.text for chapter in self.page.first_book.chapters] == self.harry_potter_chapters

    def test_should_allow_locate_many_elements_from_page_object(self):
        actual_books = [book.title.field_value.text for book in self.page.books]
        assert actual_books == self.listed_books

    def test_should_allow_to_use_square_brackets_to_get_element(self):
        assert self.page.books[1].title.field_value.text == self.lord_of_the_ring_title
        assert self.page.books[2].title.field_value.text == self.da_vinci_code_title

    def test_should_allow_to_get_number_of_found_items_using_len_operator(self):
        assert len(self.page.books) == 4

    def test_should_let_access_elements_by_given_key(self):
        for book, book_title in zip(self.page.books, self.listed_books):
            assert book.title.field_value.text == self.page.books_by_titles[book_title].title.field_value.text

    def test_should_let_access_elements_by_given_key_when_key_is_given_as_string_with_name_of_attribiute(self):
        for book, book_title in zip(self.page.books, self.listed_books):
            assert book.title.field_value.text == self.page.books_by_titles_with_string_key[book_title].title.field_value.text

    def test_should_allow_to_get_number_of_found_items_using_len_operator_while_using_dict_wrapper(self):
        assert len(self.page.books_by_titles) == 4

    def test_should_allow_to_use_contains_operator_while_using_dict_wrapper(self):
        assert self.da_vinci_code_title in self.page.books_by_titles
        assert 'not existing title' not in self.page.books_by_titles

    def test_should_allow_to_iterate_with_keys_method_while_using_dict_wrapper(self):
        for key, book in self.page.books_by_titles.items():
            assert key == book.title.field_value.text

    def test_should_return_keys_in_dom_order_for_keys_method_while_using_dict_wrapper(self):
        assert self.listed_books == list(self.page.books_by_titles.keys())

    def test_should_not_allow_to_modify_elements(self):
        with pytest.raises(AttributeError):
            self.page.books = []
        with pytest.raises(AttributeError):
            self.page.books_by_titles = {}

    def test_should_allow_to_get_found_elements_attribute_for_each_found_element(self):
        harry_potter_chapters_with_pages = [
            'The boy who lived 5',
            'The vanishing glass 32',
            'The letters from no one 45',
        ]
        assert list(self.page.books[0].chapters.values('text')) == harry_potter_chapters_with_pages

    def test_should_allow_chaining_when_getting_elements_attributes(self):
        expected_availability = ['AVAILABLE', 'AVAILABLE', 'NOT AVAILABLE', 'AVAILABLE']
        assert list(self.page.books.values('availability').values('text')) == expected_availability

        actual_books_titles = list(self.page.books.values('title').values('field_value').values('text'))
        assert actual_books_titles == self.listed_books

    def test_should_allow_using_values_method_to_get_attribute_that_is_list_and_chain_to_get_value_for_each_element(
            self):
        all_books_titles = list(self.page.books.values('chapters').values('title').values('text'))
        assert all_books_titles[0] == self.harry_potter_chapters
        assert all_books_titles[1] == self.lord_of_the_rings_chapters
        assert all_books_titles[2] == self.da_vinci_code_chapters
        assert all_books_titles[3] == self.the_catcher_chapters

    def test_should_allow_chaining_when_getting_key_indexed_elements_attributes(self):
        expected_books_availability = {
            self.harry_potter_title: 'AVAILABLE',
            self.lord_of_the_ring_title: 'AVAILABLE',
            self.da_vinci_code_title: 'NOT AVAILABLE',
            self.the_catcher_title: 'AVAILABLE',
        }
        assert dict(
            self.page.books_by_titles.values('availability').values('text').items()) == expected_books_availability

        expected_books_authors = {
            self.harry_potter_title: 'J. K. Rowling',
            self.lord_of_the_ring_title: 'J. R. R. Tolkien',
            self.da_vinci_code_title: 'Dan Brown',
            self.the_catcher_title: 'Jerome David Salinger',
        }

        actual_authors = dict(self.page.books_by_titles.values('author').values('field_value').values('text').items())
        assert actual_authors == expected_books_authors

    def test_should_allow_using_values_method_on_key_indexed_elements_to_get_attribute_that_is_list_and_chain_to_get_value_for_each_element(self):
        all_books_titles = dict(self.page.books_by_titles.values('chapters').values('title').values('text').items())

        assert all_books_titles[self.harry_potter_title] == self.harry_potter_chapters
        assert all_books_titles[self.lord_of_the_ring_title] == self.lord_of_the_rings_chapters
        assert all_books_titles[self.da_vinci_code_title] == self.da_vinci_code_chapters
        assert all_books_titles[self.the_catcher_title] == self.the_catcher_chapters

    def test_should_allow_using_key_indexed_elements_on_web_element(self):
        harry_potter_chapters_start = {
            'The boy who lived': '5',
            'The vanishing glass': '32',
            'The letters from no one': '45',
        }
        actual_chapters = dict(self.page.first_book.chapters_by_title.values('first_page').values('text').items())
        assert actual_chapters == harry_potter_chapters_start

    def test_should_allow_checking_existance_of_many_located_elements(self):
        assert not self.page.non_existing_books.exists()
        assert not self.page.non_existing_books_by_title.exists()
        assert self.page.books.exists()
        assert self.page.books_by_titles.exists()
