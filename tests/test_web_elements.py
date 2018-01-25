from tests.pages.books_page import BooksPage, BookWebElement
from tests.pages.web_element_interaction_page import WebElementInteractionPage

from tests.utils import WebDriverTestCase


class TestLocate(WebDriverTestCase):
    def test_should_allow_to_nest_web_element_inside_another_web_element(self):
        self.page = BooksPage(driver=self.driver)
        self.page.open()

        self.assertEqual(self.page.first_book.title.field_name.text, 'Title:')
        self.assertEqual(self.page.first_book.title.field_value.text, "Harry Potter and the Philosopher's Stone")

        self.assertEqual(self.page.first_book.author.field_name.text, 'Author:')
        self.assertEqual(self.page.first_book.author.field_value.text, 'J. K. Rowling')

        self.assertEqual(self.page.first_book.isbn.field_name.text, 'ISBN:')
        self.assertEqual(self.page.first_book.isbn.field_value.text, '0747532699')

    def test_should_interact_with_web_elements(self):
        self.page = WebElementInteractionPage(driver=self.driver)
        self.page.open()

        self.page.source_input.send_keys('text to copy')
        self.page.copy_button.click()
        self.assertEqual(self.page.copied_text.text, 'text to copy')

        self.assertEqual(self.page.counter.text, '0')
        self.page.increment_button.click()
        self.page.increment_button.click()
        self.page.increment_button.click()
        self.assertEqual(self.page.counter.text, '3')

    def test_should_allow_to_check_web_element_existance(self):
        self.page = WebElementInteractionPage(driver=self.driver)
        self.page.open()

        self.assertTrue(self.page.removed_div.exists())
        self.page.remove_div_button.click()
        self.assertFalse(self.page.removed_div.exists())
