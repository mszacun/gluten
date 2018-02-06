import pytest

from tests.pages.books_page import BooksPage
from tests.utils import WebDriverTestCase


class TestLocateGlobal(WebDriverTestCase):
    da_vinci_code_title = "The Da Vinci Code"

    aginoodle_title = 'Aginoodle - to be or not to be a backlog'
    carbonara_title = 'Ultimate Receips: Spaghetti Carbonara'
    onelte_title = 'The Downfall of Long-Term Evolution (Part 1)'

    aginoodle_date = '08.02.2018'
    carbonara_date = '12.02.2018'
    onelte_date = '15.02.2018'

    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestLocateGlobal, cls).setup_class(firefox)
        cls.page = BooksPage(driver=cls.firefox)
        cls.page.open()

    def test_should_locate_global_element(self):
        first_book = self.page.first_book
        bestseller = first_book.bestseller
        assert bestseller.title.text == self.da_vinci_code_title

    def test_should_locate_global_bestseller_for_all_books(self):
        for b in self.page.books:
            assert b.bestseller.title.text == self.da_vinci_code_title

    def test_should_locate_global_all_books_in_bestseller(self):
        bestseller = self.page.bestseller
        assert len(bestseller.books) == 4

    def test_should_locate_global_many_with_keys(self):
        future_books_dates = dict(self.page.bestseller.future_by_title.values('date').values('text').items())
        assert future_books_dates[self.aginoodle_title] == self.aginoodle_date
        assert future_books_dates[self.carbonara_title] == self.carbonara_date
        assert future_books_dates[self.onelte_title] == self.onelte_date
