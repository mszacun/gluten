from tests.pages.books_page import BooksPage
from tests.pages.web_element_interaction_page import WebElementInteractionPage
from tests.pages.existance_and_visibility_page import ExistanceAndVisibilityPage

from tests.utils import WebDriverTestCase


class TestBaseWebelement(WebDriverTestCase):
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

    def test_should_allow_to_check_element_visibility(self):
        page = ExistanceAndVisibilityPage(driver=self.firefox)
        page.open()

        assert page.to_not_be_visible_element.is_visible
        assert page.to_not_be_displayed.is_visible
        assert page.to_be_removed.is_visible

        page.make_not_visible_button.click()
        assert not page.to_not_be_visible_element.is_visible

        page.make_not_visible_button.click()
        assert page.to_not_be_visible_element.is_visible

    def test_should_allot_to_check_if_element_is_displayed(self):
        page = ExistanceAndVisibilityPage(driver=self.firefox)
        page.open()

        assert page.to_not_be_visible_element.is_displayed
        assert page.to_not_be_displayed.is_displayed
        assert page.to_be_removed.is_displayed

        page.make_not_displayed_button.click()

        assert not page.to_not_be_displayed.is_displayed

    def test_should_return_list_of_elements_classes(self):
        page = WebElementInteractionPage(driver=self.firefox)
        page.open()

        assert page.dynamic_classes_div.classes == []
        assert not page.dynamic_classes_div.has_class('class1')

        page.add_class_button.click()
        assert page.dynamic_classes_div.classes == ['class1']
        assert page.dynamic_classes_div.has_class('class1')
        assert not page.dynamic_classes_div.has_class('class2')

        page.add_class_button.click()
        assert page.dynamic_classes_div.classes == ['class1', 'class2']
        assert page.dynamic_classes_div.has_class('class1')
        assert page.dynamic_classes_div.has_class('class2')

    def test_should_double_click_element(self):
        page = WebElementInteractionPage(driver=self.firefox)
        page.open()

        assert page.double_click_text_changing_div.text == 'This text will change on double click'
        page.double_click_text_changing_div.double_click()
        assert page.double_click_text_changing_div.text == 'double clicked'
