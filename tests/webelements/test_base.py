from tests.pages.books_page import BooksPage
from tests.pages.web_element_interaction_page import WebElementInteractionPage

from tests.utils import WebDriverTestCase


class TestLocate(WebDriverTestCase):
    def test_should_allow_to_nest_web_element_inside_another_web_element(self):
        page = BooksPage(driver=self.firefox)
        page.open()

        assert page.first_book.title.field_name.text == 'Title:'
        assert page.first_book.title.field_value.text == "Harry Potter and the Philosopher's Stone"

        assert page.first_book.author.field_name.text == 'Author:'
        assert page.first_book.author.field_value.text == 'J. K. Rowling'

        assert page.first_book.isbn.field_name.text == 'ISBN:'
        assert page.first_book.isbn.field_value.text == '0747532699'

    def test_should_interact_with_web_elements(self):
        page = WebElementInteractionPage(driver=self.firefox)
        page.open()

        page.source_input.send_keys('text to copy')
        page.copy_button.click()
        assert page.copied_text.text == 'text to copy'

        assert page.counter.text == '0'
        page.increment_button.click()
        page.increment_button.click()
        page.increment_button.click()
        assert page.counter.text == '3'

    def test_should_allow_to_check_web_element_existance(self):
        page = WebElementInteractionPage(driver=self.firefox)
        page.open()

        assert page.removed_div.exists()
        page.remove_div_button.click()
        assert not page.removed_div.exists()
