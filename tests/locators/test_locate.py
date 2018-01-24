from selenium.webdriver.common.by import By

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import WebDriverTestCase, get_fixture_url


class DiffrentLocatorsPage(Page):
    located_by_id = Locate('with_id', By.ID)
    located_by_tag_name = Locate('p', By.TAG_NAME)
    located_by_name = Locate('with_name', By.NAME)
    located_by_link_text = Locate('link text', By.LINK_TEXT)
    located_by_class_name = Locate('with_class_name', By.CLASS_NAME)
    located_by_css_selector = Locate('.with_class_name.and_second_class_name')
    located_by_xpath = Locate('//body/ul/*[2]', By.XPATH)

    def open(self):
        fixture_url = get_fixture_url('test_diffrent_locators.html')
        self._go_to_url(fixture_url)


class TestLocate(WebDriverTestCase):
    def setUp(self):
        super(TestLocate, self).setUp()

        self.page = DiffrentLocatorsPage(driver=self.driver)
        self.page.open()

    def test_should_locate_elements_using_diffrent_searching_methods(self):
        self.assertEqual(self.page.located_by_id.text, 'To be located with id')
        self.assertEqual(self.page.located_by_tag_name.text, 'To be located by tag name')
        self.assertEqual(self.page.located_by_name.text, 'To be located by name')
        self.assertEqual(self.page.located_by_link_text.text, 'link text')
        self.assertEqual(self.page.located_by_class_name.text, 'To be located with class name')
        self.assertEqual(self.page.located_by_css_selector.text, 'To be located with css selector')
        self.assertEqual(self.page.located_by_xpath.text, 'To be located with XPath')

    def test_should_return_first_element_when_multiple_elemnts_matches_selector(self):
        self.assertEqual(self.page.located_by_id.text, 'To be located with id')
